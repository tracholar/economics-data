# coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('zq_hs.csv', sep='\t')
df = df[100::].reset_index()

def strategy_test(stock_ratio = 0.5):
    value = 1.0
    zq_value = value * (1-stock_ratio)
    stock_value = value * stock_ratio
    zq_num = 0  # 初始份额
    stock_num = 0

    X = []
    Y = []
    for n, r in df.iterrows():
        value_zq, value_stock = r['value_zq'], r['value_hs300']

        if n == 0: # 初始化
            zq_num = zq_value / value_zq
            stock_num = stock_value / value_stock

        # 更新净值
        zq_value = zq_num * r['value_zq']
        stock_value = stock_num * r['value_hs300']
        value = zq_value + stock_value
        X.append(r['date'])
        Y.append(value)

    return pd.DataFrame({
        'date' : X,
        'value' : Y
    })

outdf = strategy_test(0.0).set_index('date')
for r in [0.5, 1.0]:
    outdf = outdf.join(strategy_test(r).set_index('date'), how='inner', rsuffix='_{}%'.format(int(r*100)))

outdf[::5].to_csv('zq_hs_package_00_100.csv',sep='\t')

outdf[::5].plot(figsize=(12,6), color=['b', 'g', 'r'])
fig = plt.gcf()
plt.legend([u'招商产业债', u'招商产业债+沪深300等比例配置', u'工银沪深300'])
plt.ylabel(u'累积净值')
plt.xlabel(u'时间')
plt.title(u'股债不同比例回测结果：招商产业债+沪深300')
fig.savefig('zq_hs_package_00_100.svg')