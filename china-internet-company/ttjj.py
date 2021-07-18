# coding:utf-8
import json
import pandas as pd
import time
import matplotlib.pyplot as plt


def read_acc_value(f) :
    data = open(f).read()
    accValues = json.loads(data)['accValues']
    X = []
    Y = []
    for x, y in accValues:
        t = time.localtime(x / 1000)
        x = time.strftime("%Y-%m-%d", t)
        X.append(x)
        Y.append(y)
    df = pd.DataFrame({
        'date': X,
        'value': Y
    })
    return df


def plot(name, title=""):
    file_name = name + '.json'

    df = read_acc_value(file_name)
    assert isinstance(df, pd.DataFrame)

    fig = plt.figure()
    df = df.set_index('date')
    df.plot(figsize=(12,6))
    plt.legend([])
    plt.title(title)
    plt.savefig('output/{}.svg'.format(name))

    print(df.describe())
    max_value = df.value.max()
    max_return = df.value.values[-1] / max_value - 1

    print("""
    最大值: {}
    最大回撤: {:.1f}%
    """.format(max_value, max_return*100))

    return df