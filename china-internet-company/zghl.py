# coding:utf-8
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

from ttjj import read_acc_value, plot

df1=plot('513050', u'易方达中概互联50ETF')
df2=plot('513100', u'广发纳斯达克100ETF')

df3 = 0.5 * (df1 + df2 / 1.812)

print(df3)

dfplot = pd.DataFrame({
    u"中概互联+纳斯达克" : df3.value,
    u"中概互联": df1.value,
    u"纳斯达克" : df2.value / 1.812
})


fig = plt.figure()
dfplot.iloc[868:].plot(figsize=(12,6))

#plt.xlim([868,2000])
plt.title(u'中概互联+纳斯达克')
plt.savefig('output/zuhe.svg')
