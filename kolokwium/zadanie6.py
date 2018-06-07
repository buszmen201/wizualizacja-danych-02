import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# axis - kolumny to axis=0 a jeśli wiersze to axis=1


# index_col zmienia domyślny sposób nazywania kolun na tę kolumnę przez nas wskazaną(musi mieć unikalne!!!)
df = pd.read_csv("wig_od_2015.csv", index_col='Data')
#konwersja kolunmy na typ daty
df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
# tworzymy nową kolumnę która ma taką samą zawartość co kolumna Zamkniecie
df['Dane'] = df['Zamkniecie']

# print(df)

# wybieramy nazwy wierszy(indeksy)
# zmienia z specyficznego formatu danych modułu Pandas na zwykłą pythonową listę
# i wybieramy index czyli Data ponieważ musi jednoznacznie określać każdy wiersz
# danych i słupek na wykresie
label = df.index.tolist()
wartosci = df['Dane'].tolist()
dlugosc = np.arange(len(label))
plt.bar(dlugosc, wartosci)
plt.xlabel('Data')
plt.ylabel(u"Zamknięcie")
plt.title("Klaudia i Jareeeeek :*")
plt.xticks(dlugosc, label, rotation=30, fontsize=5)
plt.show()

# df['MA100'] = df['Wolumen'].rolling(window=100).mean() - wartość krocząca dla kolumny wolumen