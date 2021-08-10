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
        'id': '005827',
        'name': u'易方达蓝筹精选'
    }, {
        'id': '513050',
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
    }, {
        'id': '008763',
        'name': u'天弘越南市场股票(QDII)A'
    }, {
        'id': '513000',
        'name': u'易方达日经225ETF'
    }, {
        'id': '164824',
        'name': u'工银印度基金人民币'
    }, {
        'id': '513030',
        'name': u'华安德国30(DAX)ETF'
    }, {
        'id': '118002',
        'name': u'易方达标普消费品指数A'
    }, {
        'id': '004877',
        'name': u'汇添富全球医疗混合人民币'
    }, {
        'id': '159807',
        'name': u'易方达中证科技50ETF'
    }, {
        'id': '588080',
        'name': u'易方达上证科创板50成份ETF'
    }, {
        'id': '159781',
        'name': u'易方达中证科创创业50ETF'
    }, {
        'id': '009265',
        'name': u'易方达消费精选股票'
    }, {
        'id': '163406',
        'name': u'兴全合润'
    }, {
        'id': '501311',
        'name': u'嘉实港股通新经济指数A'
    }, {
        'id': '001832',
        'name': u'易方达瑞恒灵活配置混合'
    }, {
        'id': '007412',
        'name': u'景顺长城绩优成长混合'
    }, {
        'id': '513010',
        'name': u'易方达恒生科技'
    }, {
        'id': '010736',
        'name': u'易方达沪深300指数增强A'
    }, {
        'id': '110037',
        'name': u'易方达纯债债券A'
    }, {
        'id': '110038',
        'name': u'易方达纯债债券C'
    }, {
        'id': '000148',
        'name': u'易方达高等级信用债债券C'
    }, {
        'id': '001832',
        'name': u'易方达瑞恒灵活配置混合'
    }, {
        'id': '260108',
        'name': u'景顺长城新兴成长混合'
    }, {
        'id': '001631',
        'name': u'天弘中证食品饮料指数A'
    }, {
        'id': '002549',
        'name': u'嘉实稳祥纯债债券A'
    }, {
        'id': '161716',
        'name': u'招商双债增强债券(LOF)C'
    }, {
        'id': '001868',
        'name': u'招商产业债券C'
    }, {
        'id': '004615',
        'name': u'鹏扬利泽债券C'
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
        date = map(_timestamp_to_date, value[:, 0] / 1000)
        net_value = value[:, 1]
        series = pd.Series(net_value, index=date)
        acc_net_value[name] = series

    return acc_net_value


def get_fund_acc_return_by_time():
    df = pd.read_csv(DATA_DIR + '/fund.csv')
    acc_net_value = []
    for i, row in df.iterrows():
        name = row['name']
        value = np.array(json.loads(row['acc_return']))
        date = map(_timestamp_to_date, value[:, 0] / 1000)
        net_value = value[:, 1]/100.0 + 1
        series = pd.Series(net_value, index=date, name=name)
        acc_net_value.append(series)

    return pd.concat(acc_net_value, axis=1)


def norm(df):
    df.dropna(inplace=True)
    df = df / df.ix[0]
    cols = df.ix[-1].sort_values(ascending=False).index
    return df[cols]


def sort_by_fund_last_value(df):
    assert isinstance(df, pd.DataFrame)
    cols = df.ix[-1].sort_values(ascending=False).index
    return df[cols]


def max_drawdown(x):
    if isinstance(x, pd.Series):
        x = x.dropna()
    x = list(x)
    if len(x) <= 1:
        return 0
    mid = len(x) // 2
    md_left = max_drawdown(x[:mid])
    md_right = max_drawdown(x[mid:])

    max_left = max(x[:mid])
    min_right = min(x[mid:])
    md_curr = 1.0 * (max_left - min_right) / max_left

    return max(md_left, md_right, md_curr)


def parse_time(s):
    return pd.datetime.strptime(s, '%Y-%m-%d')

def growth_ratio(y):
    assert isinstance(y, pd.Series)
    y = y.dropna()
    dy = y.iloc[-1]/y.iloc[0]
    dt = parse_time(y.index[-1]) - parse_time(y.index[0])
    dt_years = dt.days/365.0

    sign = np.sign(dy)
    dy = np.abs(dy)
    r = np.exp((np.log(dy))/dt_years) - 1
    r = r * sign
    return r

def corr_coef(x, y):
    assert x.size == y.size
    x = x - np.mean(x)
    y = y - np.mean(y)

    return np.sum(x * y) / np.sqrt(np.sum(x * x)) / np.sqrt(np.sum(y * y))


def fund_corr_coef(x, y, diff=1):
    tmp = pd.DataFrame({
        'x': x,
        'y': y
    }).dropna().diff(diff).dropna()

    coef = corr_coef(tmp.x.values, tmp.y.values)
    return coef

if __name__ == '__main__':
    print(get_fund_acc_net_value_by_time())

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 7, 4, 5, 3]
    print(max_drawdown(x))
    import matplotlib.pyplot as plt

    plt.plot(x)
    plt.show()
