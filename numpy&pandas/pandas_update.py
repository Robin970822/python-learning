# coding=utf-8
import pandas as pd
import numpy as np

dates = pd.date_range('20180420', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)),
                  index=dates,
                  columns=['A', 'B', 'C', 'D'])
print df
df.iloc[2, 2] = 1111
df.loc['20180422', 'B'] = 2222
print df
df.B[df.A > 4] = 0
print df
df['F'] = np.nan
print df

df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
