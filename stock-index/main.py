#coding:utf-8

import pandas as pd
import matplotlib.pyplot as plt
import pyecharts.options as opts
from pyecharts.charts import Line

df = pd.read_csv(u'标普500市盈率历史数据.txt', sep='\t')
y =  df['市盈率 (PE Ratio)']

plt.plot(y.values)
plt.show()