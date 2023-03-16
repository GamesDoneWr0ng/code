from Layers.Layer import Layer
import numpy as np

class LayerTanh(Layer):
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.tanh(self.inputs)
        return self.output
    
    def backward_propagation(self, output_error, _):
        return (1-np.tanh(self.inputs)**2).T * output_error