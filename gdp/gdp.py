#coding:utf-8
"""
数据来源: http://data.eastmoney.com/cjsj/gdp.html

注意, 官方公布的GDP数据是名义GDP数据, 但是公布的GDP增速是GDP平减指数, 也就是减掉了物价指数之后的增速
"""

import pandas as pd
import matplotlib.pyplot as plt

names = ['季度']
for a in ['国内生产总值', '第一产业', '第二产业', '第三产业']:
    for b in ['绝对值(亿元)', '同比']:
        names.append(a + '-' + b)
df = pd.read_csv('./data.csv', header=None, names=names, sep=r'\s+')

df.set_index('季度')['国内生产总值-绝对值(亿元)'][::-4].plot(figsize=(10, 6), grid='on')
f = plt.gcf()
f.savefig('data.svg')

html = df.to_html(index=False)

gdp = pd.read_csv('gdp.csv')
gdp_sort = gdp.sort_values(by='时间').set_index('时间')
(gdp_sort[['第一产业增加值(亿元)','第二产业增加值(亿元)','第三产业增加值(亿元)']].apply(lambda x: x/gdp_sort['国内生产总值(亿元)'])).plot.bar(stacked=True, figsize=(12, 5), grid='on')
plt.title(u'GDP各产业结构')
f = plt.gcf()
f.savefig('gdp-struct.svg')

gdp_sort[-30:].plot(grid='on', figsize=(10, 6))
f = plt.gcf()
f.savefig('gdp.svg')
gdp_html = gdp.to_html(index=False)

gdp_inc = (gdp_sort / gdp_sort.shift(1) - 1)*100
gdp_inc = gdp_inc[['国内生产总值(亿元)']][-20:]
gdp_inc.columns = ['同比增长']
gdp_inc.plot(grid='on', figsize=(10, 6), style='o-')
plt.title(u'名义GDP年增长率')
f = plt.gcf()
f.savefig('gdp_inc.svg')

with open('data.html', 'w') as fp:
    fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
             'type="text/css">' \
             'table {border-collapse: collapse; margin-top:20px;}' \
             'th, td {border: 1px solid;}' \
             '</style>')
    fp.write(open('data.svg').read())
    fp.write(open('gdp.svg').read())
    fp.write(open('gdp_inc.svg').read())
    fp.write(open('gdp-struct.svg').read())
    fp.write(gdp_html.encode('utf-8', 'ignore'))
    fp.write(html.encode('utf-8', 'ignore'))


