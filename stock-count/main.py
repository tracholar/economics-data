#coding:utf-8
"""A股新增开户数
数据来源:
    1. https://legulegu.com/stockdata/a_shares_new_account
    2. https://legulegu.com/stockdata/a_shares_new_account/geta_shares_new_account
    3. http://data.eastmoney.com/cjsj/yzgptjnew.html
"""

import pandas as pd
import json
from datetime import datetime
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')


## 大图
df_plt = df.sort_values('date').set_index('date')
ax = (df_plt['sharesNewAccount']/10000).plot(figsize=(12, 6), grid='on')
plt.ylabel(u'万人')

df_plt['close'].plot(ax=ax,secondary_y=True, style='r', figsize=(12, 6), grid='on')

ax.legend([ax.get_lines()[0], ax.right_ax.get_lines()[0]],[u'新增开户数', u'上证指数'])
f = plt.gcf()
f.savefig('data.svg')
plt.close()

## 近期图
df_plt = df.sort_values('date')[-52:].set_index('date')
ax = (df_plt['sharesNewAccount']/10000).plot(figsize=(12, 6), grid='on', style='.-')
plt.ylabel(u'万人')

df_plt['close'].plot(ax=ax,secondary_y=True, style='r.-', figsize=(12, 6), grid='on')

ax.legend([ax.get_lines()[0], ax.right_ax.get_lines()[0]],[u'新增开户数', u'上证指数'])
f = plt.gcf()
f.savefig('data2.svg')


with open('data.html', 'w') as fp:
    fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
             'type="text/css">' \
             'table {border-collapse: collapse; margin-top:20px;}' \
             'th, td {border: 1px solid;}' \
             '</style>')
    fp.write(open('data2.svg').read())
    fp.write(open('data.svg').read())
    fp.write(df.to_html().encode('utf-8'))