# coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('zq_hs.csv', sep='\t')
df = df[100::].reset_index()

def strategy_test(stock_ratio = 0.5, update_period=30):
    value = 1.0
    zq_value = value * (1-stock_ratio)
    stock_value = value * stock_ratio
    zq_num = 0  # 初始份额
    stock_num = 0

    month = '2012-03'
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

        # 不调仓
        if (n+1) % update_period != 0:
            continue

        # 调仓
        print '调仓...'
        zq_value = value * (1-stock_ratio)
        stock_value = value * stock_ratio
        zq_num = zq_value/r['value_zq']
        stock_num = stock_value / r['value_hs300']

    return pd.DataFrame({
        'date' : X,
        'value' : Y
    })

outdf = strategy_test(0.0).set_index('date')
for r in [(0.5, 30), (0.5, 1000000000), (1.0, 30)]:
    ratio, T = r
    outdf = outdf.join(strategy_test(ratio, T).set_index('date'), how='inner', rsuffix='_{}%'.format(int(ratio*100)))

outdf[::5].to_csv('zq_hs_00_100.csv',sep='\t')

outdf[::5].plot(figsize=(12,6))
fig = plt.gcf()
plt.legend([u'纯债券', u'股票50%动态平衡',u'股票50%不做调整',u'纯股票'])
plt.ylabel(u'累积净值')
plt.xlabel(u'时间')
plt.title(u'股债不同比例回测结果：招商产业债+沪深300')
fig.savefig('zq_hs_00_100.svg')