#coding:utf-8

"""
数据来源, 汇率 https://cn.investing.com/currencies/usd-cny-historical-data

"""

import pandas as pd
import matplotlib.pyplot as plt


def p2f(x):
    return float(x.strip('%'))


df0 = pd.read_csv('data.csv', sep='\t')

df = df0.sort_values(by='日期')
df = df.set_index('日期')

df[['收盘']].plot(grid='on', figsize = (12,6))
f = plt.gcf()
f.savefig('data.svg')

df[['收盘']][-365:].plot(grid='on', figsize = (12,6))
f = plt.gcf()
f.savefig('data2.svg')

def md_table(df):
    return df.to_html(index=False).encode('utf-8', 'ignore')

fp = open('data.html', 'w')
fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
         'type="text/css">' \
         'table {border-collapse: collapse;}' \
         'th, td {border: 1px solid;}' \
         '</style>')


fp.write(open('data2.svg').read())
fp.write(open('data.svg').read())
fp.write( md_table(df0) )
fp.close()
