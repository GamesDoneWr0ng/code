from matplotlib import pyplot as plt
import numpy as np
 
# Konstanter 
m = 0.400                 # massen av gjenstanden, kg
theta = np.radians(30)    # vinkel for skråplanet
my = 100                  # friksjonstall
g = 9.81                  # tyngdeakselerasjon, m/s^2

# Konstante krefter 
Gx = m*g*np.sin(theta)  # tyngdekraft langs skråplanet, N
Gy = m*g*np.cos(theta)  # tyngdekraft normalt på skråplanet, N
N = Gy                  # normalkraft på gjenstanden, N

# Variable krefter, utregning av kraftsum og akselerasjon 
def a(v):
    R = -np.sign(v)*my*N    # friksjonskraft, motsatt retning av fart
    sum_F = -Gx             # kraftsum, N
    if np.sign(v+(sum_F+R)/m*dt) != np.sign(v): # Friksjon er ikke større en resten av summen av kreftene
        return -v/dt
    else:
        sum_F += R
    aks = sum_F/m        # akselerasjon, m/s
    return aks

# Startverdier 
s = 0                   # startposisjon, m
v = 3.20                # startfart, m/s
t = 0                   # starttid, s
 
# Lister for lagring av data 
s_verdier = [s]
v_verdier = [v]
t_verdier = [t]

# Simulering av bevegelse 
dt = 0.001              # tidssteg i simulering, s

while t<10:             # krav for stopp av simulering
    v += a(v)*dt        # regner ut ny fart
    s += v*dt           # regner ut ny posisjon
    t += dt             # går til neste tidspunkt

    # Lagring av verdier 
    v_verdier.append(v)
    s_verdier.append(s)
    t_verdier.append(t)

# Tegning av graf
plt.figure(1)
plt.plot(t_verdier, v_verdier)            # lager grafen
plt.xlabel("$t$ / s")                     # x-akse-tittel
plt.ylabel("$v$ / (m/s)")                 # y-akse-tittel
plt.title("Fartsgraf langs skråplan")     # tittel på grafen
plt.grid()                                # legger til rutenett

plt.figure(2)
plt.plot(t_verdier, s_verdier)            # lager grafen
plt.xlabel("$t$ / s")                     # x-akse-tittel
plt.ylabel("$s$ / m")                     # y-akse-tittel
plt.title("Posisjonsgraf langs skråplan") # tittel på grafen
plt.grid()                                # legger til rutenett

plt.show()                                # viser grafen