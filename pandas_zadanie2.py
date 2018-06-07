import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx = pd.ExcelFile('Najpopularniejsze-imiona-w-Polsce-w-latach-2000-2017.xlsx') #zmiennej o nazwie xlsx przypisujemy plik (?!) rób wg tego schematu xD
df = pd.read_excel(xlsx, 'Arkusz1') #zmienna df przechowuje zawartośc naszego pliku o rozszerzeniu xmlx(nazwa zmiennej - w tym przypadku xlsx, nazwa arkusza)

# newdf = df[df['Liczba'] > 1000]
liczba_imion_wieksza_niz_1000 = df.query('Liczba > 1000') #do zmiennej przypisujemu zmienną df z warunkiem liczba większa od 1000
#print(liczba_imion_wieksza_niz_1000)


moje_imie = df.query(u"Imię == 'KLAUDIA'")
#print(moje_imie)


rok = 2007
rok_2007 = df.query('Rok == @rok')
# print(rok_2007)
liczba_dzieci = sum(rok_2007['Liczba'])
#print(liczba_dzieci)


rok_2000_2005 = df.query('Rok >= 2000 and Rok <= 2005')
licba_dziecii = sum(rok_2000_2005['Liczba'])
#print(licba_dziecii)
# print(rok_2000_2005)S
# print(df.iloc[10]['Rok']) wyświetlamy konkretną komórkę


chlopcy_i_dziewczynki = df.query(u"(Płeć) == 'M' and (Płeć) == 'K'")
liczba_chlopcow_i_dziewczynek = sum(chlopcy_i_dziewczynki['Liczba'])
#print(chlopcy_i_dziewczynki)


imiona_chlopca = df.query(u"Płeć == 'M' and Rok == 2002")
grouped = imiona_chlopca.sort_values(by='Liczba')
print(u"Najczęściej występujące imiona chłopca: ", grouped.iloc[0][u'Imię'], " i ",
      grouped.iloc[1][u"Imię"])
imiona_dziewczyny = df.query(u"Płeć == 'K' and Rok == 2004")
groupedk = imiona_dziewczyny.sort_values(by='Liczba')
print(u"Najczęściej występujące imiona dziewczynek z roku 2004: ", groupedk.iloc[0][u'Imię'], " i ",
      groupedk.iloc[1][u'Imię'])






# book = xlrd.open_workbook('Najpopularniejsze-imiona-w-Polsce-w-latach-2000-2017.xlsx')
# sh = book.sheet_by_name('Arkusz1')
#
# for i in range(sh.nrows):
#     print(sh.row(i))

