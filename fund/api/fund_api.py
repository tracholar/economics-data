# coding:utf-8
import abc


class FundApi(object):
    # return FundData
    def find_fund_data(self, fund_id):
        raise NotImplementedError()


class FundData(object):
    @property
    def acc_net_value(self):
        raise NotImplementedError()

    @property
    def acc_return(self):
        raise NotImplementedError()
