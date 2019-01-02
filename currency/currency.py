#coding:utf-8

"""
数据来源, 东方财富 http://data.eastmoney.com/cjsj/moneysupply.aspx?p=1
API : http://data.eastmoney.com/DataCenter_V3/Chart/cjsj/China.ashx?isxml=false&type=GJZB&style=ZGZB&mkt=11&r=0.2980607212649313
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', sep='\t', skiprows=1, names=['mon', 'm2', 'a', 'b', 'm1', 'c', 'd', 'm0', 'e','f'])

df = df.sort_values(by='mon')
cols = ['m2', 'm1', 'm0']
df = df.set_index('mon')[cols]

df.plot(grid='on', figsize = (10,6))
f = plt.gcf()
f.savefig('data.svg')


def md_table(df):
    sb = '<table><thead><tr><td>时间</td>'
    cols = df.columns
    for col in cols:
        sb += '<th>' + col + '</th>'
    sb += '</tr></thead><tbody>'
    for row in df.iterrows():
        sb += '<tr>'
        sb += '<td>' + str(row[0]) + '</td>'
        for c in cols:
            sb += '<td>' + str(row[1][c]) + '</td>'
        sb += '</tr>'
    sb += '</tbody></table>'
    return sb

fp = open('data.html', 'w')
fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
         'type="text/css">' \
         'table {border-collapse: collapse;}' \
         'th, td {border: 1px solid;}' \
         '</style>')

fp.write(open('data.svg').read())
fp.write( md_table(df) )
