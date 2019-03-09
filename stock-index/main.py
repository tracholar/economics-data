#coding:utf-8

import pandas as pd
df = pd.read_csv(u'标普500市盈率历史数据.txt', sep='\t')
print  df['市盈率 (PE Ratio)'].describe()