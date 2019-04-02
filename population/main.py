#coding:utf-8
"""人口数据
数据来源: 国家统计局 <http://data.stats.gov.cn/easyquery.htm?cn=C01>
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('population.csv', sep='\t')
df['增长率'] = (df['年末总人口(万人)']/df['年末总人口(万人)'].shift(-1) - 1)*100
df['性别比'] = df['男性人口(万人)'] / df['女性人口(万人)']
df['城镇化率'] = (df['城镇人口(万人)'] / df['年末总人口(万人)'])*100
df_plt = df.sort_values('时间').set_index('时间')

## 总人口
ax = df_plt['年末总人口(万人)'].plot(kind='bar', figsize=(12, 6), grid='on', legend=[u'年末总人口(万人)'])
ax2 = ax.twinx()
ax2.spines['right'].set_position(('axes', 1.0))
df_plt['增长率'].plot(ax=ax2, style='r.-')
plt.legend([u'年增长率(右轴)'])
plt.title(u'人口')
f = plt.gcf()
f.savefig('data.svg')

## 城乡结构
f = plt.figure(figsize=(12, 6))
ax = f.gca()
df_plt['城镇人口(万人)'].plot(kind='bar', legend=[u'城镇人口(万人)'], grid='on', ax=ax)
ax2 = ax.twinx()
ax2.spines['right'].set_position(('axes', 1.0))
df_plt['城镇化率'].plot(ax=ax2, style='r.-')
plt.legend([u'城镇化率'], loc='right')
plt.title(u'城乡结构')
f.savefig('data2.svg')

with open('data.html', 'w') as fp:
    fp.write('<meta content="text/html; charset=utf-8" http-equiv="content-type" /><style ' \
             'type="text/css">' \
             'table {border-collapse: collapse; margin-top:20px;}' \
             'th, td {border: 1px solid;}' \
             '</style>')
    fp.write(open('data.svg').read())
    fp.write(open('data2.svg').read())
    fp.write(df.to_html().encode('utf-8'))


## 年龄结构
df = pd.read_csv('age.csv', sep='\t')
df['0-14岁'] = df['0-14岁人口(万人)'] / df['年末总人口(万人)'] * 100
df['15-64岁'] = df['15-64岁人口(万人)'] / df['年末总人口(万人)'] * 100
df['65岁及以上'] = df['65岁及以上人口(万人)'] / df['年末总人口(万人)'] * 100


df_plt = df.sort_values('时间').set_index('时间')
ax = df_plt[['0-14岁', '15-64岁', '65岁及以上']].plot.bar(figsize=(12, 6), grid='on', stacked=True, legend=False)
patches, labels = ax.get_legend_handles_labels()
ax.legend(patches, labels, loc=[0.01, 0.4])


ax2 = ax.twinx()
ax2.spines['right'].set_position(('axes', 1.0))
df_plt[['总抚养比(%)','少儿抚养比(%)','老年抚养比(%)']].plot(ax=ax2, style='.-',
                                    color=['#000000', '#3333FF','#AAFFAA'])
patches, labels = ax2.get_legend_handles_labels()
ax2.legend(patches, labels, loc=[0.5, 0.7])
plt.title(u'年龄结构')
f = plt.gcf()
f.savefig('data3.svg')




with open('data.html', 'a') as fp:
    fp.write(open('data3.svg').read())
    fp.write(df.to_html().encode('utf-8'))


## 年龄结构2

df = pd.read_csv('age2.csv', sep='\t')
cols = "0-4岁人口数(人口抽样调查)(人)	5-9岁人口数(人口抽样调查)(人)	10-14岁人口数(人口抽样调查)(人)	15-19岁人口数(人口抽样调查)(人)	20-24岁人口数(人口抽样调查)(人)	25-29岁人口数(人口抽样调查)(人)	30-34岁人口数(人口抽样调查)(人)	35-39岁人口数(人口抽样调查)(人)	40-44岁人口数(人口抽样调查)(人)	45-49岁人口数(人口抽样调查)(人)	50-54岁人口数(人口抽样调查)(人)	55-59岁人口数(人口抽样调查)(人)	60-64岁人口数(人口抽样调查)(人)	65-69岁人口数(人口抽样调查)(人)	70-74岁人口数(人口抽样调查)(人)	75-79岁人口数(人口抽样调查)(人)	80-84岁人口数(人口抽样调查)(人)	85-89岁人口数(人口抽样调查)(人)	90-94岁人口数(人口抽样调查)(人)	95岁以上人口数(人口抽样调查)(人)".split()
newcols = []
for c in cols:
    nc = c.replace('人口数(人口抽样调查)(人)', '')
    newcols.append(nc)
    df[nc] = df[c] / df['人口数(人口抽样调查)(人)'] * 100

df_plt = df.sort_values('时间').set_index('时间')
ax = df_plt[newcols].plot.bar(figsize=(12, 6), grid='on', stacked=True)
plt.title(u'年龄结构')
f = plt.gcf()
f.savefig('data4.svg')




with open('data.html', 'a') as fp:
    fp.write(open('data4.svg').read())
    fp.write(df.to_html().encode('utf-8'))


## 教育结构
df = pd.read_csv('edu7.csv').sort_values('时间', ascending=False)
df['高等学校入学率'] = df['普通高等学校招生数(万人)'] / (df['职业高中招生数(万人)'].shift(-3) + df['高中招生数(万人)'].shift(-3)) * 100
df['高等学历占比'] = df['普通高等学校招生数(万人)'] / df['普通小学招生数(万人)'].shift(-12) * 100
df['博士学历累积'] = df.sort_values('时间').set_index('时间')['博士招生数(万人)'].cumsum().reset_index().sort_values('时间', ascending=False).reset_index()['博士招生数(万人)']
df['博士学历占比'] = df['博士招生数(万人)'] / df['普通小学招生数(万人)'].shift(-19) * 100
df['研究生学历占比'] = df['研究生招生数(万人)'] / df['普通小学招生数(万人)'].shift(-16) * 100
df['研究生学历累积'] = df.sort_values('时间').set_index('时间')['研究生招生数(万人)'].cumsum().reset_index().sort_values('时间', ascending=False).reset_index()['研究生招生数(万人)']
df['本科入学率'] = df['普通本科招生数(万人)'] / df['高中招生数(万人)'].shift(-3) * 100
df['本科学历占比'] = df['普通本科招生数(万人)'] / df['普通小学招生数(万人)'].shift(-12) * 100
df['本科学历累积'] = df.sort_values('时间').set_index('时间')['普通本科招生数(万人)'].cumsum().reset_index().sort_values('时间', ascending=False).reset_index()['普通本科招生数(万人)']
df['高中学历占比'] = df['高中招生数(万人)'] / df['普通小学招生数(万人)'].shift(-9) * 100
df_plt = df.sort_values('时间').set_index('时间')


cols1 = ['普通小学招生数(万人)','职业高中招生数(万人)','高中招生数(万人)','普通高等学校招生数(万人)',   '普通本科招生数(万人)']
df_plt[cols1].plot.area(figsize=(12, 6), grid='on', stacked=False, alpha=1)
plt.title(u'教育结构-招生')
f = plt.gcf()
f.savefig('data5.svg')

cols1 = ['本科学历累积','研究生学历累积','博士学历累积']
df_plt[cols1].plot.area(figsize=(12, 6), grid='on', stacked=False, alpha=1)
plt.title(u'教育结构-存量(万人)')
f = plt.gcf()
f.savefig('data6.svg')


cols1 = ['本科学历占比','研究生学历占比','博士学历占比']
df_plt[30:][cols1].plot(figsize=(12, 6), grid='on', style='.-')
plt.title(u'教育结构-增量')
f = plt.gcf()
f.savefig('data7.svg')

with open('data.html', 'a') as fp:
    fp.write(open('data5.svg').read())
    fp.write(open('data6.svg').read())
    fp.write(open('data7.svg').read())
    fp.write(df.to_html().encode('utf-8'))

