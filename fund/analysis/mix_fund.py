# coding:utf-8
# 科技板块基金对比
from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value_by_time, norm, fund_corr_coef, max_drawdown
from os.path import dirname

__ROOT__ = dirname(__file__)

fund = ['易方达安心回馈混合', '广发稳健增长混合A']
df = get_fund_acc_net_value_by_time()
df = norm(df[fund].dropna()[30:])

for fi in fund:
    print(fi, max_drawdown(df[fi]))

df.plot(figsize=(10,5))
plt.grid()
plt.title(u'基金累积净值')
fig = plt.gcf()
fig.savefig(__ROOT__ + '/image/mix_fund.svg')

x = range(1,100)
y = []
for xi in x:
    yi = fund_corr_coef(df[fund[0]], df[fund[1]], xi)
    y.append(yi)
fig = plt.figure(figsize=(10,5))
plt.plot(x, y)
plt.grid()
plt.xlabel('diff days')
plt.ylabel('correlation')
plt.title(' vs '.join(fund).decode('utf-8'))
fig.savefig(__ROOT__ + '/image/mix_fund_corr.svg')
