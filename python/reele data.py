from pylab import *
from numpy import loadtxt

#def convert(s):
#    return s.replace(b',', b'.')

hopen = loadtxt("resources/weater.csv", delimiter=";", skiprows=1, usecols=(2,3), 
                #converters={3: convert})
                converters={3: lambda s: s.replace(b',', b'.')})
aar = hopen[:, 0]
temp = hopen[:, 1]

plot(aar, temp)
xlabel("år")
ylabel("temp")

show()