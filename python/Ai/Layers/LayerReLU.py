import numpy as np
from Layers.Layer import Layer

class LayerReLU(Layer):
    def forward(self, inputs):
        self.output = np.maximum(0, np.dot(inputs, self.weights) + self.biases)