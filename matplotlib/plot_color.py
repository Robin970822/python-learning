#!/usr/bin/python
import getopt
import sys
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D


def usage():
    print "-i: "
    print "\t name of input file, only excel is supported now;"
    print "-o: "
    print "\t name of output file;"
    print "-h"
    print "\t get help"
    return


opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
input_file = ""
output_file = ""
for op, value in opts:
    if op == "-i":
        input_file = value
    elif op == "-o":
        output_file = value
    elif op == "-h":
        usage()
        sys.exit()

if input_file == "":
    print "Please input a filename!"
    sys.exit()

data = pd.DataFrame(pd.read_excel(input_file))
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

if output_file == "":
    plt.savefig('fig.png', bbox_inches='tight')
else:
    plt.savefig(output_file, bbox_inches='tight')

plt.show()
