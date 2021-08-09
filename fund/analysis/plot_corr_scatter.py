# coding:utf-8
# 绘制相关性散点图
# 确定一组坐标基，选取3个相关性较弱的基金做基：纳斯达克，沪深300，招商产业债
from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value_by_time, fund_corr_coef
from os.path import dirname

__ROOT__ = dirname(__file__)

df = pd.read_csv(__ROOT__ + '/data/fund_corr.csv', index_col=0)
print(df)

x = '中欧医疗健康混合A'
y = '汇添富中证主要消费ETF'
# df[y] = np.sign(df[y]) * np.sqrt(np.abs(df[y]))
ax = df.plot(kind='scatter', x=x, y=y, figsize=(10,7))
for name, row in df.iterrows():
    ax.annotate(name.decode('utf-8'), (row[x], row[y]))
plt.grid()
plt.ylim(-0.2, 1.1)
#plt.xlim(0.5,1)
#plt.ylim(0.5,1.1)

plt.gcf().savefig(__ROOT__ + '/image/fund_corr_scatter1.svg')