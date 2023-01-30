import math
from pylab import *

delta_x = 1E-8

def f(graf, x):
  if type(x) != np.ndarray:
    y = graf.replace("x", f"({str(x)})")
    y = eval(y)
    return y

  y_values = []

  for i in x:
    y = graf.replace("x", f"({str(i)})")
    y = eval(y)
    y_values.append(y)
      
  return np.array(y_values)

def df(graf, x):
  return (f(graf, x + delta_x) - f(graf, x)) / delta_x

def nyX(graf, x1):
  return x1 - f(graf, x1) / df(graf, x1)

graf = input("Graf: ")
x = int(input("X0: "))

while f(graf, x) > delta_x:
  x = nyX(graf, x)
  print(f"Bedre x: {x}, f(x): {f(graf, x)}")

print(f"Beste x: {x}, f(x): {f(graf, x)}")

x_values = linspace(-5, 5, 101)
y_values = f(graf, x_values)

plot(x_values, y_values)
scatter([x], [0], color="red", zorder = 10)

grid(True)
xlabel("x")
ylabel("y")
axhline(y=0, color="k", zorder=0)
axvline(x=0, color="k", zorder=0)

show()