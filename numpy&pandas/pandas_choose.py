import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])
print s

dates = pd.date_range('20180419', periods=6)
df = pd.DataFrame(np.random.rand(6, 4),
                  index=dates,
                  columns=['A', 'B', 'C', 'D'])

print df['A']
print df.A
print df[0:3]
print df['20180419':'20180422']
