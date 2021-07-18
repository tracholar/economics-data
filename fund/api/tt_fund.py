# coding:utf-8
from fund_api import FundApi, FundData
import time
import requests as rq
import json
import re
import os


class TTFundApi(FundApi):
    def __init__(self, root='http://fund.eastmoney.com'):
        self._root = root
        self._fund_basic_api = '{root}/pingzhongdata/{fund_id}.js?v={version_id}'

    @property
    def _version_id(self):
        return long(time.time())

    def find_fund_data(self, fund_id):
        url = self._fund_basic_api.format(root=self._root,
                                          fund_id=fund_id,
                                          version_id=self._version_id)
        data = TTFundData.from_js_data(rq.get(url).content)
        return data


class TTFundData(FundData):
    _save_file = os.path.dirname(__file__) + '/data/tt_fund.json'

    def __init__(self, ):
        pass

    def __getitem__(self, k):
        return self._data[k]

    def save(self):
        if os.path.exists(self._save_file):
            data = json.loads(open(self._save_file).read())
        else:
            data = dict()

        if data is None or len(data) == 0:
            data = dict()

        fund_id = self['fS_code'].replace('"', '').replace(' ', '')
        data[fund_id] = self._data

        with open(self._save_file, 'w') as fp:
            json.dump(data, fp)

    @staticmethod
    def load(fund_id):
        data = json.loads(open(TTFundData._save_file).read())
        if fund_id in data:
            return data[fund_id]
        return dict()

    # 累积净值
    @property
    def acc_net_value(self):
        return self['Data_ACWorthTrend']

    @staticmethod
    def from_js_data(js_data):
        _data = TTFundData()

        group = re.findall(r'var\s+([\w_\d]+)\s*=(.+?);', js_data)
        group = dict(group)
        _data._data = group

        return _data

    def __str__(self):
        return str(self._data)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print(u'usage: tt_fund.py <基金ID>')
        sys.exit(1)

    fund_id = sys.argv[1]

    api = TTFundApi()
    data = api.total_net_value(sys.argv[1])
    data = TTFundData.load(sys.argv[1])
    print(data)