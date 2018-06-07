# polecenia input, stdin potrafi zwrócić tylko i wyłącznie string

#zadanie1
zdanie = input("Wprowadz zdanie:\n")
print(zdanie.count(" "))

#zadanie2
import sys
print("Podaj wartosci:\n")
liczba1 = int(sys.stdin.readline())
liczba2 = int(sys.stdin.readline())
print(u"Twój wynik to:\n")
wynik = liczba1 * liczba2
sys.stdout.write(str(wynik))

#zadanie3
liczba = int(input(u"Wprowadź liczbę:\n"))
if liczba >= 0:
    print(liczba)
else:
    print(liczba * (-1))

#zadanie4
a = int(input(u"Wprowadż liczbę:\n"))
b = int(input(u"Wprowadż liczbę:\n"))
c = int(input(u"Wprowadż liczbę:\n"))
if (0 < (a and b and c) <= 10) and (a > b or b > c):
    print(u"Warunek został spełniony")
else:
    print(u"Warunek nie został spełniony")

#zadanie5
for i in range(0, 101, 5):
    print(i)

#zadanie6
for i in range(0, 10+1):
    liczba = int(input(u"Wprowadź liczbę:\n"))
    print(liczba**2)

#zadanie7
import random
random.seed()
liczba = random.randint(0, 10)
tablica = []
while liczba != 2:
    tablica.append(liczba)
    liczba = random.randint(0, 3)
else:
    print(u"Znalazłam zagubioną liczbę! :) ")
print(tablica)

#zadanie8
liczba = input(u"Wprowadź liczbę:\n")
if len(liczba) > 1:
    i = 0
    temp = 0
    while i < len(liczba):
        temp += liczba[i]
        i += 1
    else:
        print(temp)
else:
    print(liczba)
