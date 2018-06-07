import json

json_plik = open('data-text.json').read()
tab = json.loads(json_plik)

for i in tab:
    print(i)

