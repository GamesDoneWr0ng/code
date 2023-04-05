from Layers.Layer import Layer
import numpy as np

class LayerTanh(Layer):
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.tanh(self.inputs)
        self.output = 0.5 * (self.output + 1)
        return self.output

    def backward_propagation(self, output_error, _):
        return 0.5 * np.apply_along_axis(np.multiply, 0, (1-np.tanh(self.inputs)**2), output_error.T)