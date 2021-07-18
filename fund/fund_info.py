# coding:utf-8
# 基配置信息
import pandas as pd
import numpy as np
import json
from os.path import dirname

_fund_list = [
    {
        'id': '513100',
        'name': u'国泰纳斯达克100ETF'
    }, {
        'id': '513500',
        'name': u'博时标普500ETF'
    }, {
        'id': '161128',
        'name': u'易方达标普信息科技人民币'
    }, {
        'id': '510300',
        'name': u'华泰柏瑞沪深300ETF'
    }, {
        'id': '510500',
        'name': u'南方中证500ETF'
    }, {
        'id': '159901',
        'name': u'易方达深证100ETF'
    }, {
        'id': '510050',
        'name': u'华夏上证50ETF'
    }, {
        'id': '159915',
        'name': u'易方达创业板ETF'
    }, {
        'id': '512010',
        'name': u'易方达沪深300医药ETF'
    }, {
        'id': '159928',
        'name': u'汇添富中证主要消费ETF'
    }, {
        'id': '161725',
        'name': u'招商中证白酒A'
    }, {
        'id': '161005',
        'name': u'富国天惠成长混合LOF'
    }, {
        'id': '110011',
        'name': u'易方达中小盘混合'
    }, {
        'id' : '005827',
        'name': u'易方达蓝筹精选'
    }, {
        'id' : '513050',
        'name': u'易方达中概互联50ETF'
    }, {
        'id': '217022',
        'name': u'招商产业债券A'
    }, {
        'id': '000171',
        'name': u'易方达裕丰回报债券'
    }, {
        'id': '001182',
        'name': u'易方达安心回馈混合'
    }, {
        'id': '118001',
        'name': u'易方达亚洲精选'
    }, {
        'id': '159949',
        'name': u'华安创业板50ETF'
    }, {
        'id': '003095',
        'name': u'中欧医疗健康混合A'
    }, {
        'id': '110008',
        'name': u'易方达稳健收益债券B'
    }, {
        'id': '515650',
        'name': '富国中证消费50ETF'
    }, {
        'id': '110022',
        'name': u'易方达消费行业股票'
    }, {
        'id': '110003',
        'name': u'易方达上证50增强A'
    }, {
        'id': '270002',
        'name': u'广发稳健增长混合A'
    }, {
        'id': '501057',
        'name': u'汇添富中证新能源汽车A'
    }, {
        'id': '510900',
        'name': u'易方达恒生国企ETF'
    }, {
        'id': '070009',
        'name': u'嘉实超短债债券C'
    }, {
        'id': '000147',
        'name': u'易方达高等级信用债债券A'
    }
]

FUND_LIST = _fund_list

__ROOT__ = dirname(__file__)
DATA_DIR = __ROOT__ + '/data'


def get_fund_acc_net_value():
    df = pd.read_csv(DATA_DIR + '/fund.csv')
    df['total_net_value'] = np.array(df['total_net_value'])
    return df

def _timestamp_to_date(t):
    import time
    t = time.localtime(t)
    x = time.strftime("%Y-%m-%d", t)
    return x

def get_fund_acc_net_value_by_time():
    df = pd.read_csv(DATA_DIR + '/fund.csv')
    acc_net_value = pd.DataFrame()
    for i, row in df.iterrows():
        name = row['name']
        value = np.array(json.loads(row['total_net_value']))
        date = map(_timestamp_to_date, value[:, 0]/1000)
        net_value = value[:, 1]
        series = pd.Series(net_value, index=date)
        acc_net_value[name] = series

    return acc_net_value


def norm(df):
    df.dropna(inplace=True)
    df = df/df.ix[0]
    cols = df.ix[-1].sort_values(ascending=False).index
    return df[cols]


if __name__ == '__main__':
    print(get_fund_acc_net_value_by_time())