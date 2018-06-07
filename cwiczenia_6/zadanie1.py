# Dictreader czyta w ten sposób że czyta dane wierszami i kazdy
# element wiersza nazywa nazwą kolumny z pierwszego wiersza.
# Sam reader czyta dane wierszami ale nie nazywa elementów

#zadanie1
import csv

with open('data-text.csv', 'r') as file:
    tab = csv.DictReader(file)

    tab1 = []

    # for i in tab:
    #     wyświetlamy konkretne kolumny
        # print(i['Year'], i['Country'])

    print("\n\n\ndane sex:\n\n")

    for i in tab:
        tab1.append(i['Sex'])

    for i in tab1:
        print(i)

