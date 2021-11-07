# coding:utf-8
import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt
import os

__ROOT__ = os.path.dirname(__file__)
df = ak.stock_zh_a_hist(symbol="600036", start_date="20210101",
                        end_date='20210813',adjust='qfq')
print(df)
assert isinstance(df, pd.DataFrame)

df.plot(kind='line', x='日期', y='收盘', figsize=(12,5))
plt.legend(['cmbchina'])
plt.grid()
fig = plt.gcf()
fig.savefig(__ROOT__ + '/images/zh.svg')