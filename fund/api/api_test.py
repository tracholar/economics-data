# coding:utf-8
import requests as rq
import time
import json

def parse_headers(ctx):
    assert isinstance(ctx, str)
    arr = ctx.strip().split('\n')
    arr = [x.split(':', 2) for x in arr]
    arr = {x[0]: x[1] for x in arr}
    return dict(arr)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Referer': 'http://fund.eastmoney.com/',
}

url = 'http://api.fund.eastmoney.com/pinzhong/LJSYLZS?fundCode=270002&indexcode=000300&type=se&callback=&_={ts}'
url = url.format(ts=long(time.time()*1000))
data = json.loads(rq.get(url, headers=headers).content)

data_arr = data['Data']
first_data = data_arr[0]
print(first_data)