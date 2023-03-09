from Layers.LayerReLU import LayerReLU
from Layers.LayerSoftmax import LayerSoftmax
import numpy as np

types = {0: LayerReLU,
         1: LayerSoftmax}

class Network:
    def __init__(self, input_size, hidden_sizes, output_size, layerTypes=[]):
        self.size = [input_size] + hidden_sizes + [output_size]
        if layerTypes == []:
            layerTypes = [0] * (len(self.size) - 1) + [1]
        self.layers = []
        for index, layer in enumerate(hidden_sizes):
            if (index == 0):
                self.layers.append(types[layerTypes[index]](input_size, hidden_sizes[0]))
            else:
                self.layers.append(types[layerTypes[index]](hidden_sizes[index-1], layer))
        self.layers.append(types[layerTypes[-1]](hidden_sizes[-1], output_size))

    def run(self, inputs):
        lastout = self.layers[0].forward(self, inputs)
        for layer in self.layers[1:]:
            lastout = layer.forward(lastout)
        return lastout