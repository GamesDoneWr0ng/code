from pylab import *

x = [-3, -2, -1, 0, 1, 2, 3, 4]
f = [9, 4, 1, 0, 1, 4, 9, 16]

n =len(x)
g = zeros(n)

for i in range(0, n-1):
  g[i] = (f[i+1] - f[i]) / (x[i+1] - x[i])

plot(x[0 : n-1], f[0 : n-1])
plot(x[0 : n-1], g[0 : n-1])
grid()
show()