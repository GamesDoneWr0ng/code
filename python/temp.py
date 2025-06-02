import matplotlib.pylab as plt

with open('/Users/askborgen/Downloads/microbit (1).csv') as f:
    data = f.readlines()

t_values = []
reading_values = []

for i in data[1:]:
    t,reading = i.split(",")
    t_values.append(float(t))
    reading_values.append(float(reading))

plt.plot(t_values, reading_values, "r-")
plt.show()