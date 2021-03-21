# coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('zq_hs_xf.csv', sep='\t')
print df.head()

def strategy_test(stock_ratio = 0.5):
    value = 1.0
    zq_value = value * (1-stock_ratio)
    stock_value = value * stock_ratio
    zq_num = 0  # 初始份额
    stock_num = 0

    month = '2012-03'
    X = []
    Y = []
    for n, r in df.iterrows():
        value_zq, value_stock = r['value_zq'], r['value']

        if n == 0: # 初始化
            zq_num = zq_value / value_zq
            stock_num = stock_value / value_stock

        # 更新净值
        zq_value = zq_num * value_zq
        stock_value = stock_num * value_stock
        value = zq_value + stock_value
        X.append(r['date'])
        Y.append(value)

        # 不调仓
        if (n+1) % 5 != 0:
            continue

        # 调仓
        print '调仓...'
        zq_value = value * (1-stock_ratio)
        stock_value = value * stock_ratio
        zq_num = zq_value / value_zq
        stock_num = stock_value / value_stock


    return pd.DataFrame({
        'date' : X,
        'value' : Y
    })

outdf = strategy_test(0.0).set_index('date')
for r in [0.3, 0.5,0.7, 1.0]:
    outdf = outdf.join(strategy_test(r).set_index('date'), how='inner', rsuffix='_{}%'.format(int(r*100)))

outdf[::5].to_csv('zq_xf_00_100.csv',sep='\t')

outdf[::5].plot(figsize=(12,6))
fig = plt.gcf()
plt.legend([u'纯债券',u'股票30%',u'股票50%',u'股票70%',u'纯股票'])
plt.ylabel(u'累积净值')
plt.xlabel(u'时间')
plt.title(u'股债不同比例回测结果：招商产业债+中证主要消费')
fig.savefig('zq_xf_00_100.svg')