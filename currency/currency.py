#coding:utf-8

"""
数据来源, 东方财富 http://data.eastmoney.com/cjsj/moneysupply.aspx?p=1
API : http://data.eastmoney.com/DataCenter_V3/Chart/cjsj/China.ashx?isxml=false&type=GJZB&style=ZGZB&mkt=11&r=0.2980607212649313
"""

import pandas as pd
import matplotlib.pyplot as plt
from common import Template, df_to_dict
from common.echart_fig import *


def p2f(x):
    return float(x.strip('%'))


df = pd.read_csv('data.csv', sep='\t', converters={'M2同比' : p2f, 'M1同比' : p2f, 'M0同比': p2f})

df = df.sort_values(by='月份')
df = df.set_index('月份')

df1 = df[['M2数量（亿元）', 'M1数量（亿元）', 'M0数量（亿元）']]



df2 = df[['M2同比', 'M1同比', 'M0同比']]


def md_table(df):
    return df.to_html(index=False).encode('utf-8', 'ignore')

tpl = Template("货币供应量")
tpl.add_fig(Line(df_to_dict(df1), xlabel="月份", ylabel="数量", title="货币供应量"))
tpl.add_fig(Line(df_to_dict(df2), xlabel="月份", ylabel="增长率", title="货币供应量增长率", zoom_start=0))
tpl.add_section(md_table(df.reset_index().sort_values(by='月份', ascending=False)) )


fp = open('data.html', 'w')
fp.write(tpl.render())
fp.close()
