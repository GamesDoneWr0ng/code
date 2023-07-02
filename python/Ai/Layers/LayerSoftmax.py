from Layers.Layer import Layer
import numpy as np

class LayerSoftmax(Layer):
    def forward(self, inputs):
        self.inputs = inputs
        shiftInputs = inputs - np.max(inputs, axis=1, keepdims=True)
        exps = np.exp(shiftInputs)
        self.output = exps / np.sum(exps, axis=1, keepdims=True)
        return self.output

    def backward_propagation(self, output_error, _):
        error = (-np.outer(self.output, self.output) + np.diag(self.output.flatten())) * output_error
        return error