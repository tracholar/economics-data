# coding:utf-8
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('zq_hs.csv', sep='\t')

def strategy_test(stock_ratio = 0.5):
    value = 1.0
    zq_value = value * (1-stock_ratio)
    stock_value = value * stock_ratio
    zq_num = zq_value/1.000  # 初始份额
    stock_num = stock_value / 1.1001

    month = '2012-03'
    X = []
    Y = []
    for n, r in df.iterrows():
        # 更新净值
        zq_value = zq_num * r['value_zq']
        stock_value = stock_num * r['value_hs300']
        value = zq_value + stock_value
        X.append(r['date'])
        Y.append(value)

        # 不调仓
        if r['date'][:7] == month:
            continue

        # 调仓
        month = r['date'][:7]
        zq_value = value * (1-stock_ratio)
        stock_value = value * stock_ratio
        zq_num = zq_value/r['value_zq']
        stock_num = stock_value / r['value_hs300']

    return pd.DataFrame({
        'date' : X,
        'value' : Y
    })

outdf = strategy_test(0.0).set_index('date')
for r in [0.15,0.3,0.5,0.7,1.0]:
    outdf = outdf.join(strategy_test(r).set_index('date'), how='inner', rsuffix='_{}'.format(int(r*100)))

outdf[::5].to_csv('zq_hs_00_100.csv',sep='\t')

outdf[::5].plot(figsize=(16,8))
fig = plt.gcf()
fig.savefig('zq_hs_00_100.svg')