# coding:utf-8
# 绘制基金净值图
from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value
from os.path import dirname

__ROOT__ = dirname(__file__)

df = get_fund_acc_net_value()
print(df.head())
df.plot()
fig = plt.gcf()
fig.savefig(__ROOT__ + '/image/acc_net_value.svg')
