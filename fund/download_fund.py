# coding:utf-8
# 下载目标基金
from __future__ import print_function
import pandas as pd
from os.path import dirname
from api.tt_fund import TTFundApi, TTFundData
from fund_info import FUND_LIST

__ROOT__ = dirname(__file__)
api = TTFundApi()

fid_list = []
fname_list = []
total_net_value = []
acc_return = []
for fund in FUND_LIST:
    fid, fname = fund['id'], fund['name']

    print(fid, fname)
    fid_list.append(fid)
    fname_list.append(fname)

    fund_data = api.find_fund_data(fid)
    total_net_value.append(fund_data.acc_net_value)
    acc_return.append(fund_data.acc_return)

df = pd.DataFrame({
    'id' : fid_list,
    'name' : fname_list,
    'total_net_value' : total_net_value,
    'acc_return' : acc_return
})

print(df.head())

file_name = __ROOT__ + '/data/fund'
df.to_csv(file_name + '.csv', encoding='utf-8')
df.to_excel(file_name + '.xlsx', encoding='utf-8')
