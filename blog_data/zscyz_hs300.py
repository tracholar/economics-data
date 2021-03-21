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
        t = time.localtime(x/1000)
        x = time.strftime("%Y-%m-%d", t)
        X.append(x)
        Y.append(y)
    df =pd.DataFrame({
        'date' : X,
        'value' : Y
    })
    return df



zscyz = read_acc_value('zscyz.json')
hs300 = read_acc_value('hs300.json')

zscyz.to_csv('zscyz.csv', sep='\t')
hs300.to_csv('hs300.csv', sep='\t')

df = zscyz.set_index('date').join(hs300.set_index('date'), how='inner', lsuffix='_zq', rsuffix='_hs300')
df.to_csv('zq_hs.csv', sep='\t')
df[::5].to_csv('zq_hs_week.csv', sep='\t')


