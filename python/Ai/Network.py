from Layers.LayerReLU import LayerReLU
from Layers.LayerSoftmax import LayerSoftmax
import numpy as np

class Network:
    def __init__(self, input_size, hidden_sizes, output_size):
        self.size = [input_size] + hidden_sizes + [output_size]
        self.layers = []
        for index, layer in enumerate(hidden_sizes):
            if (index == 0):
                self.layers.append(LayerReLU(input_size, hidden_sizes[0]))
            else:
                self.layers.append(LayerReLU(hidden_sizes[index-1], layer))
        self.layers.append(LayerSoftmax(hidden_sizes[-1], output_size))

    def run(self, inputs):
        lastout = self.layers[0].forward(self, inputs)
        for layer in self.layers[1:]:
            lastout = layer.forward(lastout)
        return lastout
