import matplotlib.pyplot as plt
import numpy as np

def a(v):
    L = k * v**2
    sum_F = G - L
    aks = sum_F / m
    return aks

m = 79
k = 0.32
t_slutt = 10.0
dt = 0.01

g = 9.81
G = m * g

s = 0.0
v = 0.0
t = 0.0

steps = int(t_slutt / dt)
s_verdier = np.zeros(steps)
v_verdier = np.zeros(steps)
t_verdier = np.zeros(steps)

for step in range(1,steps):
    s += v * dt
    v += a(v) * dt
    t += dt

    s_verdier[step] = s
    v_verdier[step] = v
    t_verdier[step] = t

plt.plot(t_verdier, s_verdier)
plt.plot(t_verdier, v_verdier)
plt.title("Strekning som funksjon av tid")
plt.xlabel("tid [s]")
plt.ylabel("strekning [m]")
plt.grid()
plt.show()