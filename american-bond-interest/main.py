#coding:utf-8
"""
美国国债收益率数据
数据来源: https://cn.investing.com/rates-bonds/usa-government-bonds?maturity_from=40&maturity_to=290
"""


import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame()
for n in ['1mon.csv', '3mon.csv', '1year.csv', '5year.csv', '10year.csv']:
    df = pd.read_csv(n, sep='\t', header=None, names=['日期','收盘','开盘','高','低','变动百分比']).set_index('日期')
    data[n[:-4]] = df['收盘']
df = data
df_plt = df.reset_index().sort_values(by='日期').set_index('日期')


df_plt[-100:].plot(figsize=(12, 5), grid='on')
plt.title(u'美国国债收益率')
f = plt.gcf()
f.savefig('data-recent.svg')

df_plt[-500:].plot(figsize=(12, 5), grid='on')
plt.title(u'美国国债收益率')
f = plt.gcf()
f.savefig('data-recent2.svg')

df_plt.plot(figsize=(12, 5), grid='on')
plt.title(u'美国国债收益率')
f = plt.gcf()
f.savefig('data.svg')
# plt.show()

df_plt2 = df_plt['10year'] - df_plt['1mon']
df_plt2.name = '10year - 1mon'
df_plt2.to_frame().plot(figsize=(12, 5), grid='on')
plt.title(u'美国国债收益率利差')
f = plt.gcf()
f.savefig('data-delta.svg')

df_plt2.to_frame()[-400:].plot(figsize=(12, 5), grid='on')
plt.title(u'美国国债收益率利差')
f = plt.gcf()
f.savefig('data-delta2.svg')

df_plt2.to_frame()[-100:].plot(figsize=(12, 5), grid='on')
plt.title(u'美国国债收益率利差')
f = plt.gcf()
f.savefig('data-delta3.svg')


html = df.reset_index().to_html(index=False).encode('utf-8', 'ignore')

with open('data.html', 'w') as fp:
    fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
             'type="text/css">' \
             'table {border-collapse: collapse;}' \
             'th, td {border: 1px solid;}' \
             '</style>')

    fp.write(open('data-delta3.svg').read())
    fp.write(open('data-delta2.svg').read())
    fp.write(open('data-delta.svg').read())
    fp.write(open('data-recent.svg').read())
    fp.write(open('data-recent2.svg').read())
    fp.write(open('data.svg').read())
    fp.write(html)


