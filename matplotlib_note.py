# https://blog.techbridge.cc/2018/05/11/python-data-science-and-machine-learning-matplotlib-tutorial/
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.rcParams['lines.linewidth'] = 5
mpl.rcParams['lines.color'] = 'r'
mpl.rcParams['figure.figsize'] = (10, 10)
plt.gcf().set_size_inches(10, 10)

x = pd.period_range(pd.datetime.now(), periods=200, freq='d')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(200, 3).cumsum(0)

plt.title('Random Trends')
plt.xlabel('Date')
plt.ylabel('Cum. Sum')
plt.figtext(0.995, 0.01, 'CopyRight', ha='right', va='bottom')
plt.tight_layout()
plots = plt.plot(x, y)
plt.legend(plots, ('Apple', 'Facebook', 'Google'), loc='best', framealpha=0.5, prop={'size': 'large', 'family': 'monospace'})
plt.show()
plt.savefig('plt.svg')

fig = plt.figure(figsize=(8, 4), dpi=200, tight_layout=True, linewidth=1, edgecolor='r')

# Primary axes and Secondary axes
fig = plt.figure(figsize=(8, 4))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #['x distance', 'y distance', 'x length', 'y length']
ax.set_title('Main Axes with Insert Child Axes')
ax.plot(x, y[:, 0])  # choose one set of y
ax.set_xlabel('Date')
ax.set_ylabel('Cum. sum')

# Add another axes
ax = fig.add_axes([0.15, 0.1, 0.5, 0.3])
ax.plot(x, y[:, 1], color='g') # choose another set of y
ax.set_xticks([]) # without [] will show x ticks - too crowded

# https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4]) # input a list for default (y), automatically generate x values [0, 1, 2, 3] (python ranges start with 0
plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) # input list for x, y
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') # 'ro' for line style, default is 'b-' as blue line
plt.axis([0, 6, 0, 20]) # set y axis
plt.ylabel('some numbers') # set name of y axis
plt.xlabel('some numbers') # set name of x axis
plt.show() # show the figure
import numpy as np
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')  # input three sets of numpy arrarys
# Provide an object with the data keyword argument
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
plt.scatter('a', 'b', c='c', s='d', data=data) # c for color, s for size
# Plotting with categorical variables
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()


