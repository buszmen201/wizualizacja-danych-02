# krotki (niezmienialne tablice)
# listy (tablice)
# słowniki (tablice par), klucz - indeks
# literał (string)
# literał unicode (string obsługujący polskie litery), np: u"Jarek"

from math import *

#zadanie2 i zadanie3
znak = input("Wprowadz liczbe")

if znak == "+":
    print("dodawanie:", 3+3)

elif znak == "-":
    print("odejmowanie", 3-3)

elif znak == "*":
    print("mnozenie: ", 3*3)

elif znak == "/":
    print("dzielenie: ", 3/3)

elif znak == "**":
    print("potega: ", 3**3)

elif znak == "%":
    print("wyswietla reszte: ", 3%3)

#zadanie4
from math import exp, log, sin
print(exp(10))
print(log(5 + (sin(8))**2))
print(floor(3.55))
print(ceil(4.8))

#zadanie5
imie = "klaudia"
nazwisko = "rutkowska"
print(imie.upper(), nazwisko.capitalize())

#zadanie6
ciag_znakow = "la la la"
print(ciag_znakow.count("la"))

#zadanie7
slowo = "słoik"
temp = len(slowo)
print(slowo[1], slowo[temp-1])

#zadanie8
wyraz = "Jarek, bardzo Cię lubię!"
print(wyraz.split(" "))

#zadanie9
szesnastkowe = hex(44)
print(szesnastkowe)

#zadanie10
lista = ["Jarek", "alaudia", "aaaaa"]
lista.sort()
print(lista)

nowa=[5,3,2,6,1,3,2]
nowa.sort()
print('Nowa lista po zmianach:\n',nowa)

#zadanie11
tab = [sin(0), cos(0), tan(0), 1/tan(0)]
print(tab)

#zadanie12
zdanie = u"Bardzo lubię spędzać czas z Jarkiem!"
lista = []
lista = zdanie.split(" ")
print(lista)

#zadanie13
slownik = {"Buszu" : u"Jarosław Buszowiecki", "Klaudia" : "Klaudia Rutkowska", u"Połek" : u"Patrym Połoniewicz"}
print(slownik["Buszu"], ", ", slownik['Klaudia'])

#zadanie15
slownik1 = {"I" : "Jeden", "II" : "Dwa", "III" : "Trzy", "IV" : "Cztery", "V" : u"Pięć", "VI" : u"Sześć",
            "VII" : "Siedem", "VIII" : "Osiem", "IX" : u"Dziewięć", "X" : u"Dziesięć"}
print(slownik1['I'])

#zadanie16
slownik2 = {"TheSims2" : "Gra strategiczna", "TheSims3" : "Gra strategiczna", "TransForMice" : "Gra serek!"}
print(len(slownik2))
k = 0
for i in slownik2:
    k+=1
print(k)