# coding=utf-8
import pandas as pd
import numpy as np

df = pd.DataFrame({'name': np.array(list('aabb')),
                   'classes': np.array([1, 2, 3, 4]),
                   'price': np.array([11, 22, 33, 44])},
                  index=np.array(list('0123')))

# 带有条件判断时，返回类型pd.Series，带索引
price = df.loc[df.classes == 1, 'price']
print price
print type(price)
print price.values[0]

# 直接取值式，返回值不带索引
price = df.loc['0', 'price']
print price
print type(price)
