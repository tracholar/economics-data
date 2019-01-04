#coding:utf-8
"""
数据来源 http://www.shibor.org/shibor/web/DataService.jsp



[Shibor 的作用和意义是什么？- 李淼的回答](https://www.zhihu.com/question/20078836/answer/13902097)
Shibor的意义在于，这是一个了解银行资金是否充足的晴雨表：每每当央行上调存准率或者有上调预期时，shibor会有一定幅度的上升。而一旦Shibor下行，意味着银行资金充足，市场偏宽松 ---- 有可能是央行进行公开市场操作的结果。这就为投资业在进行市场资金面分析时提供了一个重要的指标。

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

names = [
    '日期'
]
for a in ['隔夜', '1W', '2W', '1M', '3M', '6M', '9M', '1Y']:
    for b in ['5日均值', '10日均值', '20日均值']:
        names.append( a + '-' + b )

df = [pd.read_csv(f, sep=r'\s+', skiprows=4, header=None, na_values=['---'], names=names)
      for f in glob.glob('./*.txt')
      ]
df = pd.concat(df)
df = df.sort_values(by='日期').set_index('日期')

df[['隔夜-5日均值', '1W-5日均值', '1M-5日均值', '1Y-5日均值']].plot(grid='on', figsize = (12,6))
fig = plt.gcf()
fig.savefig('data.svg')

df[['隔夜-5日均值', '1W-5日均值', '2W-5日均值', '1M-5日均值', '1Y-5日均值']][-365:].plot(grid='on', figsize = (12,6))
fig = plt.gcf()
fig.savefig('data_short.svg')


html = df.reset_index().sort_values(by='日期', ascending=False).to_html(index=False)

with open('data.html', 'w') as fp:
    fp.write(open('data_short.svg').read())
    fp.write(open('data.svg').read())
    fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
             'type="text/css">' \
             'table {border-collapse: collapse;}' \
             'th, td {border: 1px solid;}' \
             '</style>')
    fp.write(html.encode('utf-8', 'ignore'))
