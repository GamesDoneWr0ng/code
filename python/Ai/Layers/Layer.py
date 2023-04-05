import numpy as np

class Layer:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases  = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.dot(self.inputs, self.weights) + self.biases
        return self.output
    
    # computes dE/dW, dE/dB for a given output_error=dE/dY. Returns input_error=dE/dX.
    def backward_propagation(self, output_error, learning_rate):
        iErrors = []
        for i in output_error:
            input_error   = np.dot(i, self.weights.T)
            for j in self.inputs:
                weights_error = np.multiply.outer(j, i)
                self.weights -= learning_rate * weights_error

            # dBias = output_error

            # update parameters
            
            self.biases  -= learning_rate * i
            #return input_error
            iErrors.append(input_error)
        return np.array(iErrors)