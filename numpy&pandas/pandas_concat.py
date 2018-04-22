# coding=utf-8
import pandas as pd
import numpy as np

# 定义资料集
columns = ['a', 'b', 'c', 'd']
df1 = pd.DataFrame(np.zeros((3, 4)), columns=columns)
df2 = pd.DataFrame(np.ones((3, 4)), columns=columns)
df3 = pd.DataFrame(np.zeros((3, 4))*2, columns=columns)

# concat纵向合并
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print res