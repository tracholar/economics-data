#coding:utf-8
"""
数据来源 http://data.eastmoney.com/cjsj/foreign_0_4.html
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', sep='\t')

print df
df_plt = df.sort_values(by='发布日期')[['时期','现值']]
df_plt['现值'] = df_plt['现值'].map(lambda x: float(x[:-1]))
df_plt.set_index('时期').plot(figsize=(12, 5), grid='on', style='.-')

plt.title(u'美国失业率')
f = plt.gcf()
f.savefig('data.svg')


html = df.to_html(index=False).encode('utf-8', 'ignore')

with open('data.html', 'w') as fp:
    fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
             'type="text/css">' \
             'table {border-collapse: collapse;}' \
             'th, td {border: 1px solid;}' \
             '</style>')
    fp.write(open('data.svg').read())
    fp.write(html)
