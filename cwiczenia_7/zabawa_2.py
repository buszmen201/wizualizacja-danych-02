# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 201)
y = []
for i in x:
    y.append(np.cos(i))

y1 = []
for i in x:
    y1.append(2*np.sin(i))

fig, (ax1, ax2) = plt.subplots(2, sharey=True)

ax1.plot(x, y, 'g-.', label='wykres cos')
ax1.set(title='label1')
legend = ax1.legend(loc='upper left', fontsize='x-large')
legend.get_frame().set_facecolor('white')

ax2.plot(x, y1, 'r.-', label='wykres sin')
ax2.set(title='label2', xlabel='time', ylabel='high')
legend = ax2.legend(loc='upper left', fontsize='x-large')
legend.get_frame().set_facecolor('white')
ax2.grid(True)

plt.show()