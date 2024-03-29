# coding:utf-8
# 绘制基金净值图
from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value_by_time
from os.path import dirname

__ROOT__ = dirname(__file__)

df = get_fund_acc_net_value_by_time()
dt = df.index >= '2017-01-01'
df = df[dt]
df.dropna(axis=1, inplace=True)
print(df.tail(5))
df = df/df.ix[0]
cols = df.ix[-1].sort_values(ascending=False).index
df = df[cols]

df.plot(figsize=(10,5))
plt.grid()
plt.title(u'基金累积净值')
fig = plt.gcf()
fig.savefig(__ROOT__ + '/image/acc_net_value.svg')
