# coding:utf-8
from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value_by_time, fund_corr_coef
from os.path import dirname

__ROOT__ = dirname(__file__)

df = pd.read_csv(__ROOT__ + '/data/fund_corr.csv', index_col=0)
print(df)

df['华泰柏瑞沪深300ETF'].sort_values().plot(kind='bar')
plt.grid()
plt.ylim(-0.2, 1)

plt.gcf().savefig(__ROOT__ + '/image/fund_corr_hs300.svg')