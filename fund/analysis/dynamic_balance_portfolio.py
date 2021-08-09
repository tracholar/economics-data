# coding:utf-8
# 寻找基金组合，一次加入新基金

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value_by_time, norm, max_drowdown
from os.path import dirname

__ROOT__ = dirname(__file__)
df = get_fund_acc_net_value_by_time()

target_fund = ['国泰纳斯达克100ETF', '华安创业板50ETF']
df = df[target_fund].dropna()


def gen_weight(topk, size=len(target_fund)):
    assert topk <= size
    w = np.array([1] * topk + [0] * (size - topk), dtype=float)
    w = w / np.sum(w)
    return w


df = norm(df)
for n in range(2, len(target_fund) + 1):
    weight = gen_weight(n)
    df['组合{}'.format(n - 1)] = np.sum(df[target_fund] * weight, axis=1)

print(df.head())
assert isinstance(df, pd.DataFrame)

print(df.head())

df.plot(figsize=(10, 5))
plt.gcf().savefig(__ROOT__ + '/image/find_fund_porfolio.svg')

df.to_csv(__ROOT__ + '/data/find_fund_porfolio.csv')

print(df.apply(max_drowdown, axis=0))
