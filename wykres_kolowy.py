import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs' #dajemy nazwy dla każdej "partii"
sizes = [15, 30, 45, 10] #dzielimy wykres kołowy na części(procentowo)
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs') to są "wysunięcia"


plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()