# coding:utf-8
# 易方达纯债 vs 易方达高等级信用债券
from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value_by_time, norm, fund_corr_coef
from os.path import dirname

__ROOT__ = dirname(__file__)

df = get_fund_acc_net_value_by_time()
df = norm(df[['易方达纯债债券C', '易方达高等级信用债债券C']].dropna()[100:])

df.plot(figsize=(10,5))
plt.grid()
plt.title(u'基金累积净值')
fig = plt.gcf()
fig.savefig(__ROOT__ + '/image/yifangda_chunzhai_vs_gaodengji.svg')

x = range(1,100)
y = []
for xi in x:
    yi = fund_corr_coef(df['易方达纯债债券C'], df['易方达高等级信用债债券C'], xi)
    y.append(yi)
fig = plt.figure(figsize=(10,5))
plt.plot(x, y)
plt.grid()
plt.xlabel('diff days')
plt.ylabel('correlation')
fig.savefig(__ROOT__ + '/image/yifangda_chunzhai_vs_gaodengji_corr.svg')
print(zip(x, y))