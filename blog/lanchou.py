# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

from ttjj import read_acc_value

file_name = 'data/hs300.json'

df = read_acc_value(file_name)
assert isinstance(df, pd.DataFrame)

df.set_index('date').plot(figsize=(12,6))
plt.legend([])
plt.savefig('output/hs300.svg')
