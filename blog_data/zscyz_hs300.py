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
xf = read_acc_value('xf.json')

zscyz.to_csv('zscyz.csv', sep='\t')
hs300.to_csv('hs300.csv', sep='\t')
xf.to_csv('xf.csv', sep='\t')

df = zscyz.set_index('date').join(hs300.set_index('date'), how='inner', lsuffix='_zq', rsuffix='_hs300')\
        .join(xf.set_index('date'), how='inner', rsuffix='_xf')
df.to_csv('zq_hs_xf.csv', sep='\t')
df[::5].to_csv('zq_hs_xf_week.csv', sep='\t')

print df.head()
df.columns=['zq', 'hs300', 'xf']
df['zq'] /= df['zq'][0]
df['hs300'] /= df['hs300'][0]
df['xf'] /= df['xf'][0]

# plot
import matplotlib.pyplot as plt
df[::5].plot(figsize=(12,6))
fig = plt.gcf()
plt.legend([u'招商产业债',u'工银沪深300',u'汇添富中证主要消费',])
plt.ylabel(u'归一化累积净值')
plt.xlabel(u'时间')
fig.savefig('zq_hs_xf.svg')


