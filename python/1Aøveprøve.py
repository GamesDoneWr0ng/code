# %%
import math

# %%
# Oppgave 1
a = int(input("tall1: "))
b = int(input("tall2: "))
c = int(input("tall3: "))
print(sum((a,b,c)))

# %%
# Oppgave 2
r = float(input("Radius: "))
jorda = 6371_000 # m
volum = (4/3) * math.pi * r**3
omkrets = 2 * math.pi * r

print(volum, omkrets)
print(f"Jorda omkrets: {2 * math.pi * jorda}")
print(f"Jorda+1 omkrets: {2 * math.pi * (jorda+1)}")

# %%
# Oppgave 3
fornavn = input("Skriv inn fornavn: ")
etternavn = input("Skriv inn etternavn: ")
print(f"{etternavn}, {fornavn} - {fornavn[0]}. {etternavn[0]}.")

# %%
# - er opperasjon og ikke tilat i variabelnavn: Expression cannot be assignment target
# fire.billeter forventer en variabel fire og prøver å nå dens billeter: "fire" is not defined
# resultatet er en SyntaxError

billet-pris = 120
fire.billeter = 120*4

print("Prisen for fire billeter er", fire.billeter)


