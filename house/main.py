#coding:utf-8
"""
数据来源 http://data.stats.gov.cn/easyquery.htm?cn=A01
"""
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv('devarea.csv', sep='\t')
#df.transpose().to_csv('data.csv')

df = pd.read_csv('data.csv')

df_plt = df.sort_values('时间').set_index('时间')[['商品住宅施工面积-累计值(万平方米)','商品住宅新开工施工面积-累计值(万平方米)', '商品住宅竣工面积-累计值(万平方米)']]

print df_plt

df_plt.plot()
plt.show()