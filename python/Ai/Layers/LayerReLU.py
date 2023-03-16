import numpy as np
from Layers.Layer import Layer

class LayerReLU(Layer):
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.maximum(0, inputs)
        return self.output
    
    def backward_propagation(self, output_error, _):
        return np.where(self.inputs > 0, 1, 0) * output_error