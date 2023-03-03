import numpy as np

#random = np.random.randn(4,4)

n_inputs = 5
n_neurons = 2
random = np.array([np.random.uniform(-1,1, n_inputs) for i in range(n_neurons)])

print(random)