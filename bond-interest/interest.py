#coding:utf-8
"""
数据来源: http://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery

"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', sep='\t')

df_plt = pd.DataFrame()
for name in ['中债国债收益率曲线', '中债商业银行普通债收益率曲线(AAA)', '中债中短期票据收益率曲线(AAA)']:
    df_plti = df[df['曲线名称'] == name].drop('曲线名称', axis=1)
    df_plt[name] = df_plti.sort_values(by='日期').set_index('日期')['3月']

df_plt.plot(figsize=(12, 5), grid='on')
plt.title(u'3月期收益率曲线')
f = plt.gcf()
f.savefig('data_risk.svg')
# plt.show()


df_plt = df[df['曲线名称'] == '中债国债收益率曲线'].drop('曲线名称', axis=1)

df_plt.sort_values(by='日期').set_index('日期')[['3月', '1年', '10年']][-365:].plot(figsize=(12, 5), grid='on')
plt.title(u'中债国债收益率曲线')
f = plt.gcf()
f.savefig('data.svg')

df_plt.sort_values(by='日期').set_index('日期')[['3月', '1年', '10年']].plot(figsize=(12, 5), grid='on')
plt.title(u'中债国债收益率曲线')
f = plt.gcf()
f.savefig('data2.svg')

html = df.to_html(index=False).encode('utf-8', 'ignore')

with open('data.html', 'w') as fp:
    fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
             'type="text/css">' \
             'table {border-collapse: collapse;}' \
             'th, td {border: 1px solid;}' \
             '</style>')
    fp.write(open('data.svg').read())
    fp.write(open('data2.svg').read())
    fp.write(html)

with open('data_month.html', 'w') as fp:
    df_plt['月份'] = df_plt['日期'].map(lambda x: x[:7])
    df_plt = df_plt.drop('日期', axis=1)
    df_plt = df_plt.sort_values(by='月份').groupby('月份').mean().reset_index().sort_values(by='月份', ascending=False)
    html = df_plt.to_html(index=False).encode('utf-8', 'ignore')

    fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
             'type="text/css">' \
             'table {border-collapse: collapse;}' \
             'th, td {border: 1px solid;}' \
             '</style>')
    fp.write(html)