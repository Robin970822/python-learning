# coding=utf-8
import pandas as pd

# 定义资料集并打印出
left = pd.DataFrame({'key1': ['k0', 'k1', 'k2', 'k3'],
                     'key2': ['k0', 'k1', 'k2', 'k3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']},
                    index=['N0', 'N1', 'N2', 'N3'])

right = pd.DataFrame({'key1': ['k0', 'k1', 'k2', 'k3'],
                      'key2': ['k0', 'k0', 'k0', 'k0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                     index=['N0', 'N2', 'N3', 'N4'])

print left
print right

# 数据库联接
res = pd.merge(left, right, on='key1')
print res
res = pd.merge(left, right, on='key2')
print res
# 数据库內联接
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print res
# 数据库外联接
res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print res
# 数据库左联接
res = pd.merge(left, right, on=['key1', 'key2'], how='left')
print res
# 数据路右联接
res = pd.merge(left, right, on=['key1', 'key2'], how='right')
print res
# 将合并的记录放在新的一列
res = pd.merge(left, right, on=['key1', 'key2'], how='outer', indicator='Indicator')
print res
# 根据左右资料集的index进行合并
res = pd.merge(left, right, how='outer', on=['key1', 'key2'],
               left_index=True, right_index=True, indicator='Indicator')
print res
res = pd.merge(left, right, how='inner', on=['key1', 'key2'],
               left_index=True, right_index=True, indicator='Indicator')
print res
# 使用suffixes解决overlapping的问题
res = pd.merge(left, right, on='key1', suffixes=['_boy', '_girl'], how='inner')
print res
