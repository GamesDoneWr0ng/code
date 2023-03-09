from Layers.Layer import Layer
import numpy as np

class LayerSoftmax(Layer):
    def forward(self, inputs):
        inputs = np.dot(inputs, self.weights) + self.biases
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities