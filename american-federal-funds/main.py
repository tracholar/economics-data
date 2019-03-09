#coding:utf-8
"""
数据来源 https://www.macrotrends.net/2015/fed-funds-rate-historical-chart
https://apps.newyorkfed.org/markets/autorates/fed%20funds
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('fed-funds-rate-historical-chart.csv')

df_plt = df.sort_values(by='date')


df_plt[-3650:].set_index('date').plot(figsize=(12, 5), grid='on', style='-')

plt.title(u'联邦基准利率')
f = plt.gcf()
f.savefig('data.svg')


df_plt.set_index('date').plot(figsize=(12, 5), grid='on', style='-')

plt.title(u'联邦基准利率')
f = plt.gcf()
f.savefig('data2.svg')





html = df.sort_values('date', ascending=False).to_html(index=False).encode('utf-8', 'ignore')

with open('data.html', 'w') as fp:
    fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
             'type="text/css">' \
             'table {border-collapse: collapse;}' \
             'th, td {border: 1px solid;}' \
             '</style>')
    fp.write(open('data.svg').read())
    fp.write(open('data2.svg').read())
    fp.write(html)

