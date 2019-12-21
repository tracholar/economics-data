#coding:utf-8
import requests as rq
import time
import json


api = 'http://api.fund.eastmoney.com/f10/lsjz?fundCode=110020&pageIndex=1&pageSize=2000&startDate=2014-09-01&endDate=&_={ts}'.format(ts=int(time.time()))
headers = {
    "Referer" : "http://fundf10.eastmoney.com/jjjz_110020.html"
}
rsp = rq.get(api, headers=headers)
f = open('hs300.json', 'w')
f.write(rsp.content)
f.close()