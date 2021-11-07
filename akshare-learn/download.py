# coding:utf-8
from stock_info import _stock_list
import akshare as ak
import pandas as pd
from datetime import datetime
import os

__ROOT__ = os.path.dirname(__file__)

start_date = '20130101'
end_date = datetime.now().strftime('%Y%m%d')
adjust = 'qfq'
print(start_date, end_date, adjust)

data = pd.DataFrame()
for stock in _stock_list:
    symbol = stock['id']
    name = stock['name']
    print(symbol, name)
    try:
        df = ak.stock_zh_a_hist(symbol=symbol, start_date=start_date,
                                end_date=end_date,adjust=adjust)
        assert isinstance(df, pd.DataFrame)
        df = df.set_index('日期')
        data[name] = df['收盘']
    except Exception as e:
        print('>>>> Get stock {name} data failed!'.format(name=name))

df = pd.DataFrame(data)
print(df.tail(10))
df.to_csv(__ROOT__ + '/data/stocks.csv', sep='\t')
