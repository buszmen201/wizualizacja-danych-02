# Komenda do zainstalowania biliotek(wymaga uorawnień administratora):
# python -mpip install -U nazwabiblioteki

# IMPORTOWANIE PLIKÓW CSV
# import csv

# with open('data-text.csv', 'r') as file:
#     tab = csv.DictReader(file)
#     tab1 = []
    # for i in tab:
    #     wyświetlamy konkretne kolumny
        # print(i['Year'], i['Country'])
#    print("\n\n\ndane sex:\n\n")

#    for i in tab:
#        tab1.append(i['Sex'])

#    for i in tab1:
#        print(i)



# RYSOWANIE WYKRESÓW
# import matplotlib.pyplot as plt

# Tytuł wykresu:
# plt.title('')

# Etykiety:
# plt.xlabel('')
# plt.ylabel('')

# Początek układu współrzędnych:
# plt.axis([2, 2, 3, 1])

# Legenda do wykresów:
# legend = plt.legend()
#   Tu określamy np. gdzie ramka legendy ma się znajdować, rozmiar czcionki
#       tu określam położenie legendy
#       loc='upper center'
#       tu określam wielkość czcionki
#       fontsize='x-large'
#       określam cień obramowaia
#       shadow='True'
#       inne właściwości są opisane pod adresem w następnej linii:
#       https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

# Rysownie siatki:
# plt.grid(True)