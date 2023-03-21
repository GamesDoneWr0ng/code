import numpy as np

class Layer:
    def __init__(self, n_inputs, n_neurons):
        self.weights = np.array([np.random.uniform(-1,1, n_inputs) for _ in range(n_neurons)])
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.dot(self.inputs, self.weights.T) + self.biases
        return self.output
    
    # computes dE/dW, dE/dB for a given output_error=dE/dY. Returns input_error=dE/dX.
    def backward_propagation(self, output_error, learning_rate):
        input_error = np.dot(output_error.T, self.weights)
        weights_error = np.dot(self.inputs.T, output_error.T)
        # dBias = output_error

        # update parameters
        self.weights -= (learning_rate * weights_error).T
        self.biases -= learning_rate * output_error
        return input_error