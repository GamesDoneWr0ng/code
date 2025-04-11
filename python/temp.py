import matplotlib.pylab as plt

with open("/Users/askborgen/Downloads/microbit.csv") as f:
    data = f.readlines()

t_values = []
x_values = []
y_values = []
z_values = []

for i in data[1:]:
    t,x,y,z = i.split(",")
    t_values.append(float(t))
    x_values.append(float(x))
    y_values.append(float(y))
    z_values.append(float(z))

plt.plot(t_values, x_values, "r-")
plt.plot(t_values, y_values, "b-")
plt.plot(t_values, z_values, "g-")
plt.show()