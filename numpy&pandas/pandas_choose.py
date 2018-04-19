import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])
print s

dates = pd.date_range('20180419', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates,
                  columns=['A', 'B', 'C', 'D'])

print df['A']
print df.A
print df[0:3]
print df['20180419':'20180422']

print df.loc['20180419']
print df.loc[:, ['A', 'B']]
print df.loc['20180419', ['A', 'B']]

print df.iloc[3, 1]
print df.iloc[3:5, 1:3]
print df.iloc[[1, 3, 5], 1:3]

print df.ix[:3, ['A', 'C']]
print df[df.A > 8]
