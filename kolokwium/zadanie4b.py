import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# axis - kolumny to axis=0 a jeśli wiersze to axis=1

df = pd.read_csv("zamowienia.csv", sep=";")

# zazwyczaj funkcje agregujące otaczamy nawiasem kwadratowym i możemy wtedy użyć więcej agregacji(do innych kolumn)
# a jeśli tego nie zrobimy to nie może ich być więcej i nie nazywa też tej kolumny tą funkcją agregującą
sprzedawcy = df.groupby('Sprzedawca').agg({'idZamowienia' : 'count'})
sprzedawcy = sprzedawcy.sort_values(by='idZamowienia', ascending=False).head(3)
#sortujemy zamowienia malejąco, dlatego ascending to false

label = sprzedawcy.index.tolist()
wartosci = sprzedawcy['idZamowienia'].tolist()
index = np.arange(len(wartosci))
print(wartosci)