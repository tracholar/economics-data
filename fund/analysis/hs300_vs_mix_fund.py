# coding:utf-8
# 对比沪深300与股债混合基金
from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_return_by_time, \
    norm, sort_by_fund_last_value, max_drawdown
from os.path import dirname

__ROOT__ = dirname(__file__)
df = get_fund_acc_return_by_time()

target_fund = ['华泰柏瑞沪深300ETF', '广发稳健增长混合A', '易方达安心回馈混合',
               '易方达裕丰回报债券', '易方达稳健收益债券B', '招商产业债券A']

df = df[target_fund]
assert isinstance(df, pd.DataFrame)
df = df.fillna(method='ffill').fillna(method='bfill')

print(df.head())

df = df[df.index > '2012-01-01']

df = norm(df)

df = sort_by_fund_last_value(df)
df.plot(figsize=(10, 5))
plt.grid()
plt.gcf().savefig(__ROOT__ + '/image/hs300_vs_mix_fund.svg')
