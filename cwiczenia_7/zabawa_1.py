import matplotlib.pyplot as plt

x = []
y = []

for i in range(-4, 5):
    x.append(i)

for i in x:
    y.append(i**2)

plt.plot(x, y, 'b-', label='y')
plt.xlabel('OX')
plt.ylabel('OY')

y1 = []

for i in x:
    y1.append(i**3)

plt.plot(x, y1, 'r-', label='y1')
legend = plt.legend(loc='upper center', shadow=False, fontsize='x-large')
legend.get_frame().set_facecolor('white')
plt.title(u'Wykresy funkcji')

plt.show()