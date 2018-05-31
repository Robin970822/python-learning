import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 61)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5), )
plt.plot(x, y, )

ax = plt.gca()

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

index = np.where(x >= 1)
index = index[0][0]

plt.plot([x[index], x[index]], [0, y[index]], 'k--', linewidth=2.5)
plt.scatter([x[index]], [y[index]], s=50, color='b')

plt.annotate(r'$2x+1=%s$' % y[index], xy=(x[index], y[index]), xycoords='data',
             xytext=(+30, -30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3, rad=.2"))

plt.text(-3.7, 3, r'$This\ is\ the\ some\ text.$',
         fontdict={'size': 16, 'color': 'r'})

plt.show()
