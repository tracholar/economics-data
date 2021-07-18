# coding:utf-8
# 绘制基金净值图
from __future__ import print_function
import pandas as pd
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value_by_time
from os.path import dirname

__ROOT__ = dirname(__file__)

df = get_fund_acc_net_value_by_time()
cols = [u'招商产业债券A', u'易方达裕丰回报债券', u'易方达稳健收益债券B',
        u'嘉实超短债债券C', u'易方达高等级信用债债券A']
df = df[cols]

df.plot(figsize=(10,5))
plt.grid()
plt.title(u'基金累积净值')
fig = plt.gcf()
fig.savefig(__ROOT__ + '/image/bound_acc_net_value.svg')