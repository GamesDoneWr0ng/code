import numpy as np

class Layer:
    def __init__(self, n_inputs, n_neurons):
        self.weights = np.array([np.random.uniform(-1,1, n_inputs) for i in range(n_neurons)])
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        pass