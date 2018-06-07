import matplotlib.pyplot as plt

x = []
y = []

for i in range(-5, 6):
    x.append(i)

for i in x:
    y.append(i**3+3)

plt.plot(x, y, 'b-', label='y')
plt.xlabel('OX')
plt.ylabel('OY')


legend = plt.legend(loc='lower right', shadow=False, fontsize='x-large')
legend.get_frame().set_facecolor('white')
plt.title(u'Wykresy funkcji')

xi = [x for x in range(0,11,2)]

plt.xticks(x, xi)
#plt.axis([-100, 100, -100, 100])
plt.show()