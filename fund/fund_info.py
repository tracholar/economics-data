# coding:utf-8
# 基配置信息
import pandas as pd
from os.path import dirname

_fund_list = [
    {
        'id' : 513100,
        'name' : u'国泰纳斯达克100ETF'
    },{
        'id' : 513500,
        'name' : u'博时标普500ETF'
    },{
        'id' : 161128,
        'name' : u'易方达标普信息科技人民币'
    },{
        'id' : 510300,
        'name' : u'华泰柏瑞沪深300ETF'
    },{
        'id' : 510500,
        'name' : u'南方中证500ETF'
    },{
        'id' : 159901,
        'name' : u'易方达深证100ETF'
    },{
        'id' : 510050,
        'name' : u'华夏上证50ETF'
    },{
        'id' : 159915,
        'name' : u'易方达创业板ETF'
    },{
        'id' : 512010,
        'name' : u'易方达沪深300医药ETF'
    },{
        'id' : 159928,
        'name' : u'汇添富中证主要消费ETF'
    },{
        'id' : 161725,
        'name' : u'招商中证白酒A'
    },{
        'id' : 161005,
        'name' : u'富国天惠成长混合LOF'
    },{
        'id' : 110011,
        'name' : u'易方达中小盘混合'
    }
]


FUND_LIST = _fund_list

__ROOT__ = dirname(__file__)
DATA_DIR = __ROOT__ + '/data'

def get_fund_acc_net_value():
    return pd.read_csv(DATA_DIR + '/fund.csv')
