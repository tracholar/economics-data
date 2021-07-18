# coding:utf-8
# 找到资产配置最佳组合
from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fund.fund_info import get_fund_acc_net_value_by_time, norm
from os.path import dirname

__ROOT__ = dirname(__file__)
df = get_fund_acc_net_value_by_time()

target_fund = ['汇添富中证主要消费ETF', '易方达沪深300医药ETF', '中欧医疗健康混合A', '易方达蓝筹精选',
               '易方达中概互联50ETF', '国泰纳斯达克100ETF',
               '易方达安心回馈混合', '易方达裕丰回报债券', '招商产业债券A', '嘉实超短债债券C']
df = norm(df[target_fund].dropna())

x = np.random.rand(len(target_fund))
x = x/sum(x)

df[u'组合1'] = np.sum(df * x, axis=1)
df = norm(df)
df.plot(figsize=(10, 5))

plt.gcf().savefig(__ROOT__ + '/image/fund_porfolio.svg')