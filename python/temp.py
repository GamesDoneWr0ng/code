import pandas as pd # "pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool"
import numpy as np # matte ting + arrays
import matplotlib.pyplot as plt # grafer

# leser inn csv filen med , som desimal ; som verdi seperator og . for blanke verdier
f = pd.read_csv("/Users/askborgen/Desktop/code/python/kpi/tabell.csv", encoding="utf-8-sig", decimal=",", sep=";", na_values=".")
f.head() # øverste 5 rader

# Alle veridene i en linje så [jan 1931, feb 1931, mar 1931, ..., des 2024]
# [::-1,1:] er en 2 dimensjonal slice som returnerer radene baklengs via ::-1 og exscluderer første colone via 1:
flatvalues = f.to_numpy()[::-1,2:].flatten()
print(flatvalues)
plt.plot(np.linspace(f["Årstall"][93], f["Årstall"][0], flatvalues.size), flatvalues) # ploter
plt.show()