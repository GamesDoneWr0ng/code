from matplotlib import pylab as plt

# henter inn data samlet fra microbit
with open("/Users/askborgen/Desktop/code/python/microbit/my_data.csv") as f:
    data = f.read().split("\n")

# lager lister for lagring av data
t_verdier = []
aks_verdier = []

# for hver logget verdi
for line in data:
    # henter data
    t, aks = line.split(",")

    # legger verdier til i listene
    t_verdier.append(float(t))
    aks_verdier.append(float(aks))

plt.plot(t_verdier, aks_verdier)
plt.show()