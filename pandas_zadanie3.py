import pandas as pd
import numpy as np
import csv

#lista unikalnych nazwisk sprzedawców
df = pd.read_csv("zamowienia.csv", sep=";") #ramka danych
df['rokzamowienia'] = pd.DatetimeIndex(df['Data zamowienia']).year


print(df.groupby(["Sprzedawca"]).agg({'Utarg' : ['max']})) #prupujemy po sprzedawcach i wybieram kolumnę Utarg i z niej wartości minimalne


#5 najwyższych wartości warości zamówień
utarg = df.sort_values(by='Utarg')
print(utarg.head(5)) #wypisuje 5 wierszy od góry
                     # tail()

#dokumentacja sort_values:
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html


#ilość zamównień złożonych przez każdego sprzedawcę
print(df.groupby('Sprzedawca').agg({'idZamowienia' : ['count']}))

# typy agregacji:
# https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/


#suma zamówień dla każdego kraju
print(df.groupby('Kraj').agg({'idZamowienia' : ['count']}))


#suma zamówień dla roku 2005, dla sprzedawców z Polski
# sprzedawcy_z_polski = df.query("Kraj == 'Polska' and rokzamowienia == 2005 ")
sprzedawcy_z_polski = df.query('rokzamowienia == 2005').groupby('Kraj').agg({'Sprzedawca': ['count']})
# print(df.groupby('rok zamowienia'))
print(sprzedawcy_z_polski.iloc[[1]]) #jeśli wybieramy wiersz to musimy dwa nawiady kwadratowe dać




# with open('zamowienia.csv', 'r', encoding='utf-8-sig') as file:
#     zamowienia = csv.DictReader(file, delimiter=';')
#
#     for i in zamowienia:
#         print(i)
#
        # df = pd.read_csv("zamowienia.csv", sep=";")
        # print(df.groupby(["Sprzedawca"]).agg({"Kraj": ["max"]}))