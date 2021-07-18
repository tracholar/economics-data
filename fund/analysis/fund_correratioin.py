# coding:utf-8
# 计算基金的相关系数
from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value_by_time
from os.path import dirname

__ROOT__ = dirname(__file__)


def corr_coef(x, y):
    assert x.size == y.size
    x = x - np.mean(x)
    y = y - np.mean(y)

    return np.sum(x * y) / np.sqrt(np.sum(x * x)) / np.sqrt(np.sum(y * y))


df = get_fund_acc_net_value_by_time()
fund_names = df.columns.values

corr = {}
for fund1 in fund_names:
    corr_fund1 = {}
    for fund2 in fund_names:
        tmp = pd.DataFrame({
            'x': df[fund1],
            'y': df[fund2]
        }).dropna().diff(1).dropna()

        coef = corr_coef(tmp.x.values, tmp.y.values)

        corr_fund1[fund2] = coef
    corr[fund1] = corr_fund1

corr_df = pd.DataFrame(corr)
print(corr_df.head())
corr_df.to_csv(__ROOT__ + '/data/fund_corr.csv')
corr_df.to_excel(__ROOT__ + '/data/fund_corr.xlsx')
