# coding:utf-8
# 找到资产配置最佳组合
from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value_by_time, norm, max_drowdown
from os.path import dirname

__ROOT__ = dirname(__file__)
df = get_fund_acc_net_value_by_time()
df = df[df.index >= '2017-01-01']

target_fund = ['汇添富中证主要消费ETF', '易方达沪深300医药ETF', '中欧医疗健康混合A', '易方达蓝筹精选',
               '易方达中概互联50ETF', '国泰纳斯达克100ETF',
               '易方达安心回馈混合', '易方达裕丰回报债券', '招商产业债券A', '嘉实超短债债券C']
df = norm(df[target_fund].fillna(method='bfill'))

x = np.random.rand(len(target_fund))
x = x/sum(x)
print('组合1：', x)

df['组合1'] = np.sum(df[target_fund] * x, axis=1)

x = np.array([1, 0.5, 1.5, 4,
     2, 6,
     1, 2, 2, 1], dtype=float)
print(sum(x) * 500 * 50)
x = x/sum(x)
df['我的组合'] = np.sum(df[target_fund] * x, axis=1)

df = norm(df)

cols = ['汇添富中证主要消费ETF','国泰纳斯达克100ETF', '易方达安心回馈混合', '我的组合', '组合1', '招商产业债券A']
cols = df[cols].ix[-1].sort_values(ascending=False).index
df[cols].plot(figsize=(10, 5))

plt.gcf().savefig(__ROOT__ + '/image/fund_porfolio.svg')

assert isinstance(df, pd.DataFrame)
max_drowdown_df = df.apply(max_drowdown, axis=0).sort_values(ascending=False)
max_drowdown_df.to_excel(__ROOT__  + '/data/fund_porfolio_max_drowdown.xlsx')
plt.figure()
max_drowdown_df.plot(kind='bar', figsize=(10, 5))
plt.gcf().savefig(__ROOT__ + '/image/fund_porfolio_max_drowdown.svg')

print(max_drowdown_df)