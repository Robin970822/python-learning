import pandas as pd
import numpy as np

df = pd.DataFrame({'name': np.array(list('aabb')),
                   'classes': np.array([1, 2, 3, 4]),
                   'price': np.array([11, 22, 33, 44])},
                  index=np.array(list('qwer')))
price = df.loc[df.classes == 1, 'price']
print price
price = df.loc['q', 'price']
print price
