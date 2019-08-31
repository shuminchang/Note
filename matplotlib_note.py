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
# Controling line properties, matplotlib.lines.Line2D
plt.plot(x, y, linewidth=2.0)

line, = plt.plot(x, y, '-')
line.set_antialiased(False) # turn off antialiasing
# setp()
lines = plt.plot(x1, y1, x2, y2)
# use keyword args
plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
# get a list of settable line properties
plt.setp(lines)

# Working with multiple figures and axes
# All plotting commands apply to the current axes.
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
# Another example
# The commas in the subplot command are optional if numrows*numcols<10. So subplot(211) is identical to subplot(2, 1, 1).
# axes(), Axes Demo, Basic Subplot Demo
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])

plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.plot([6, 7, 8])          # This will create a new line on the subplot(211)
plt.title('Easy as 1, 2, 3') # subplot 211 title
# clf() - clear current figure
# cla() - clear current axes
# Artist tutorial
'''
the memory required for a figure is not completely released until the figure is explicitly closed with close(). 
Deleting all references to the figure, and/or using the window manager to kill the window in which the figure 
appears on the screen, is not enough, because pyplot maintains internal references until close() is called.
'''
# Working with text - xlabel(), ylabel(), title(), text(), Text in Matplotlib Plots
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

t = plt.xlabel('my data', fontsize=14, color='red')
# Using mathematical expressions in text, matplotlib accepts TeX equation expressions in any text expression
plt.title(r'$\sigma_i=15$')
# Writing mathematical expressions
Text rendering With LaTeX
# Annotating text


