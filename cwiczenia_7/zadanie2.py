import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 1000)

n = []

for i in range(1, 5):
    n.append(i)

y1 = []
y2 = []
y3 = []
y4 = []

for i in x:
    y1.append(2*np.sin(i*i))
plt.plot(x, y1, '#FFFF00', label=u'Wykres 1')

for i in x:
    y2.append(np.sin(i*2))
plt.plot(x, y2, 'go--', label=u'Wykres 2')

for i in x:
    y3.append(0.5*np.sin((i**3)+3))
plt.plot(x, y3, 'b--', label=u'Wykres 3')

for i in x:
    y4.append(np.sin(i))
plt.plot(x, y4, '#FF69B4', label=u'Wykres 4')

plt.title('Wykresy funkcji')
plt.xlabel(u'Oś OX')
plt.ylabel(u'Oś OY')

legend = plt.legend(loc='upper left', shadow='True', fontsize='x-large')
legend.get_frame().set_facecolor('white')

plt.show()