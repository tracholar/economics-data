#coding:utf-8
"""
数据来源: http://yield.chinabond.com.cn/cbweb-pbc-web/pbc/showHistory?locale=cn_ZH

"""

import pandas as pd
import matplotlib.pyplot as plt
from common import Template, df_to_dict
from common.echart_fig import *

tpl = Template("债券利率")
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

df_data = df_plt.sort_values(by='日期').set_index('日期')[['3月', '1年', '10年']]
line = Line(df_to_dict(df_data), xlabel='日期', ylabel='收益率(%)', title="中债国债收益率曲线")
tpl.add_fig(line)


df_plt3 = df_plt.set_index('日期')
df_plt3 = df_plt3['10年'] - df_plt3['3月']
df_plt3.name = '10年 - 3月'
df_data = df_plt3.to_frame().reset_index().sort_values(by='日期').set_index('日期')
line = Line(df_to_dict(df_data), xlabel='日期', ylabel='利差(%)', title="中债国债收益率利差")
tpl.add_fig(line)

tpl.add_section(df.to_html(index=False).encode('utf-8', 'ignore'))

with open('data.html', 'w') as fp:
    fp.write(tpl.render())

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