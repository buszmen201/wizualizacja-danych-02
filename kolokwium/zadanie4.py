import pandas as pd
import matplotlib.pyplot as plt
# axis - kolumny to axis=0 a jeśli wiersze to axis=1

df = pd.read_csv("zamowienia.csv", sep=";") #ramka danych
print(df)
# lambda pozwala nam modyfikować przecinki na wiersze w kolumnie utarg
df['Utarg'] = df.apply(lambda row: row['Utarg'].replace(',', '.'), axis=1)
df["Utarg"] = df["Utarg"].astype(float)
udzial = df.groupby('Kraj').agg({'Utarg' : ['sum']})

labels = ['Polska', 'Niemcy']
plt.pie(udzial, labels=labels, autopct="%1.1f%%")
plt.show()

