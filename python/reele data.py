from numpy import loadtxt

#def convert(s):
#    return s.replace(b',', b'.')

hopen = loadtxt("resources/weather.csv", delimiter=";", skiprows=1, usecols=(2,3), 
                converters={3: lambda s: s.replace(b',', b'.')})
                #converters={3: convert})
år = hopen[:, 0]
temp = hopen[:, 1]




import pandas as pd

hopen = pd.read_csv('resources/weather.csv', decimal=",",  sep=";", usecols=(2,3), skiprows=1)

år = hopen.values[:, 0]
temp = hopen.values[:, 1]


import matplotlib.pyplot as plt
plt.plot(år, temp)
plt.title("Historisk temperatur")
plt.grid(True)
plt.xlabel("år")
plt.ylabel("temp")

plt.show()