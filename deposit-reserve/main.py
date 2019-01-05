#coding:utf-8
"""
数据来源: http://data.eastmoney.com/cjsj/reserverequirementratio.aspx?p=1

存款准备金率决定了货币乘数
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', sep=r'\s+')
print df[:2]
cols = ['生效日期', '大型金融机构-调整前', '大型金融机构-调整后', '大型金融机构-调整幅度','中小型-调整前','中小型-调整后','中小型-调整幅度']
print df[cols]
df[cols].set_index('生效日期').plot()
plt.show()