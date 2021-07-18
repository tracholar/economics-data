# coding:utf-8
import json
import pandas as pd
import time


def read_acc_value(f):
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
