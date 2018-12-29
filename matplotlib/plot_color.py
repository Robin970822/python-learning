#!/usr/bin/python
import sys
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filename = sys.argv[1]
data = pd.DataFrame(pd.read_excel(filename))
print data

fig = plt.figure()
ax = Axes3D(fig)

columns = data.columns.values.tolist()
ax.scatter(data.iloc[:, 0], data.iloc[:, 1], data.iloc[:, 2], color=data.index)

# Label for color
# for index, row in data.iterrows():
#     ax.text(row[columns[0]], row[columns[1]], row[columns[2]], s=index, color=index)

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

ax.set_xlabel(columns[0])
ax.set_ylabel(columns[1])
ax.set_zlabel(columns[2])

plt.show()

