#coding:utf-8

"""
数据来源, 汇率 https://cn.investing.com/currencies/usd-cny-historical-data

"""

import pandas as pd
import matplotlib.pyplot as plt
from common import Template, df_to_dict
from common.echart_fig import *


def p2f(x):
    return float(x.strip('%'))


df0 = pd.read_csv('data.csv', sep='\t')

df = df0.sort_values(by='日期')
df = df.set_index('日期')

df_plt = df[['收盘']]

def md_table(df):
    return df.to_html(index=False).encode('utf-8', 'ignore')


tpl = Template("人民币-美元汇率")

line = Line(df_to_dict(df_plt), xlabel='日期', ylabel='汇率', title="人民币-美元汇率")
line.ylim('dataMin', 'dataMax')

tpl.add_fig(line)
tpl.add_section(md_table(df0))


fp = open('data.html', 'w')
fp.write(tpl.render())
fp.close()
