import numpy as np

tablica = np.arange(1, 21, 1)  #tworzę wektor 20-elementowy, skok co 1
np.random.shuffle(tablica) # shuffle to losowanie
tablica = tablica.reshape([5, 4]) # przepkształcenie wektora na macierz
print(tablica)
suma = tablica.sum(axis=0) # suma wartości w kolumnach
print("\n\n")
print(suma)
tablica_floatow = tablica.astype('float') # zmieniamy typ na float
print("\n\n")
print(tablica_floatow)
tablica_floatow = tablica_floatow**(1/3) # podnosimy wszystkie elementy macieży do potęgi 1/3
print("\n\n")
print(tablica_floatow)
print("\n\n")
vektor = tablica_floatow.flatten() # z macierzy robimy wektor
print(np.sort(vektor)) # po czym sortujemy