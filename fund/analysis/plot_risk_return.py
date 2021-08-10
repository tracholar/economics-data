# coding:utf-8
# 基金风险收益图
from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value_by_time, norm, \
    fund_corr_coef, max_drawdown, growth_ratio
from os.path import dirname

__ROOT__ = dirname(__file__)

df = get_fund_acc_net_value_by_time()[-200:]
fund_bound = ['易方达高等级信用债债券A', '易方达纯债债券A', '嘉实稳祥纯债债券A', '嘉实超短债债券C', '招商产业债券A',
        '易方达裕丰回报债券','鹏扬利泽债券C', '招商双债增强债券(LOF)C']
fund_consumer = ['易方达消费行业股票', '汇添富中证主要消费ETF', '易方达消费精选股票',
                 '富国中证消费50ETF', '招商中证白酒A', '天弘中证食品饮料指数A']
fund_tech = ['华安创业板50ETF', '易方达创业板ETF', '易方达中证科技50ETF', '易方达上证科创板50成份ETF']
fund = fund_tech
df = df[fund]
df_basic = pd.DataFrame({
    'max_drawdown': df.apply(max_drawdown, axis=0),
    'growth_ratio': df.apply(growth_ratio, axis=0)
})
print(df_basic)
x,y = 'max_drawdown', 'growth_ratio'
ax = df_basic.plot(kind='scatter', x=x,y=y, figsize=(10,6))
for name, row in df_basic.iterrows():
    ax.annotate(name.decode('utf-8'), (row[x], row[y]))
plt.grid()
plt.gcf().savefig(__ROOT__ + '/image/plot_risk_return_tech.svg')