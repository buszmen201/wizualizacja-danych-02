import matplotlib.pyplot as plt

x = []
n = []

for i in range(-10, 11):
    x.append(i)

for i in range(1, 5):
    n.append(i)

for i in n:
    y = []
    for j in x:
        y.append((i*j)/(1+(i**5)*(j**2)))
    plt.plot(x, y, label=u'Wykres ' + str(i))

plt.title("Wykresy funkcji")
plt.xlabel(u"Oś OX")
plt.ylabel(u'Oś OY')

legend = plt.legend(loc='upper left', shadow='True', fontsize='x-large')
legend.get_frame().set_facecolor('white')

plt.show()