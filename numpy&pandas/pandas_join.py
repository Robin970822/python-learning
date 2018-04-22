# coding=utf-8
import pandas as pd
import numpy as np

# 定义资料集
df1 = pd.DataFrame(np.zeros((3, 4)),
                   columns=['a', 'b', 'c', 'd'],
                   index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)),
                   columns=['b', 'c', 'd', 'e'],
                   index=[2, 3, 4])

# 纵向“外”合并df1与df2
res = pd.concat([df1, df2], axis=0, join='outer', ignore_index=True)
print res

# 纵向“内”合并df1与df2
res = pd.concat([df1, df2], axis=0, join='inner', ignore_index=True)
print res

# 依照'df1.index'进行纵向合并
res = pd.concat([df1, df2], axis=0, join_axes=[df1.columns])
print res
