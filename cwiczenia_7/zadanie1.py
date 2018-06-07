import matplotlib.pyplot as plt

x = []
n = []

for i in range(1, 11):
    x.append(i)

for i in range(1, 5):
    n.append(i)


for i in n:
    iterator = i
    y = []
    for j in x:
        y.append((1/(j**i)))
    #plt.plot(x, y, label=f'Wykres {iterator}')
    plt.plot(x, y, label='Wykres ' + str(i))
    #plt.annotate('wskauje', xy=(3, 0.4), xytext=(5, 0.8), arrowprops=dict(fcecolor='black', shrink=0.05))

plt.title(u'Wykresy funkcji:')
plt.xlabel(u'Oś OX')
plt.ylabel(u'Oś OY')


legend = plt.legend(loc='upper center', fontsize='x-large')
legend.get_frame().set_facecolor('white')
plt.grid(True)
plt.axis([-1, 10, 0, 5])
plt.show()
#fig.savefig('path/to/save/image/to.png')