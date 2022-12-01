#Lag en kode til en kalkulator som beregner omkretsen til en valgfri geometrisk figur
#(sirkel, kvadrat, rektangel, trekant, parallellogram eller rombe). Brukeren bestemmer figur
#og legger inn nødvendige mål. Programmet beregner omkretsen til figuren med
#måleenheten brukeren valgte. Omkretsen presenteres i mm, cm, dm, m og km.
 
import math
figur = input("hvilken figur vil du ha? (sirkel, kvadrat, rektangel, trekant, parallellogram eller rombe) ").lower()
ArealEllerOmkrets = input("Areal eller Omkrets? ").lower()
 
#areal
if ArealEllerOmkrets == "areal":
   #sirkel
   if figur == "sirkel":
       r = int(input("radius = "))
       print("Arealet er:", math.pi*r*r)
   #kvadrat
   elif figur == "kvadrat":
       l = int(input("lengde = "))
       print("Arealet er:",l**2)
   #rektangel
   elif figur == "rektangel":
       l = int(input("lengde = "))
       b = int(input("bredde = "))
       print("Arealet er:", l*b)
   #trekant
   elif figur == "trekant":
       g = int(input("grunnflate = "))
       h = int(input("høyde = "))
       print("Arealet er:",g*h/2)
   #parallellogram
   elif figur == "parallellogram":
       g = int(input("grunnflate = "))
       h = int(input("høyde = "))
       print("Arealet er:",g*h)
   #rombe
   elif figur == "rombe":
       g = int(input("grunnflate = "))
       h = int(input("høyde = "))
       print("Arealet er:",g*h)
   else:
       print("bli bedre pa a skrive!!!")
#omkrets
elif ArealEllerOmkrets == "omkrets":
   #sirkel
   if figur == "sirkel":
       r = int(input("radius = "))
       print("Omkretsen er:",2*math.pi*r)
   #kvadrat
   elif figur == "kvadrat":
       l = int(input("lengde = "))
       print("Omkretsen er:",l*4)
   #rektangel
   elif figur == "rektangel":
       l = int(input("lengde = "))
       b = int(input("bredde = "))
       print("Omkretsen er:",l+l+b+b)
   #trekant
   elif figur == "trekant":
       l = int(input("lengde = "))
       print("Omkretsen er:",3*l)
   #parallellogram
   elif figur == "parallellogram":
       g = int(input("grunnflate = "))
       s = int(input("sidelengde = "))
       print("Omkretsen er:",2*g+2*s)
   #rombe
   elif figur == "rombe":
       l = int(input("lengde = "))
       print("Omkretsen er:",4*l)
   else:
       print("bli bedre pa a skrive!!!")
