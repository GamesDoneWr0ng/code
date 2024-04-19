import pandas as pd

usecols = [1,2,3,7]
file = pd.read_csv("/Users/askborgen/Desktop/code/python/eksamen høst 2023/Global YouTube Statistics.csv", encoding= "ISO-8859-1", usecols=usecols)
countries = {} # dictonary of countries

for index, i in enumerate(file["Country"]): # loop through all countries in the file and add them to the dictonary
    if i in countries: # allready found country
        countries[i] += file.values[index]
    else:
        countries[i] = file.values[index]

print(countries)