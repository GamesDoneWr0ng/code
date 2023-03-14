from Layers.Layer import Layer
from Layers.LayerReLU import LayerReLU
from Layers.LayerTanh import LayerTanh
import numpy as np

types = {0: LayerReLU,
         1: LayerTanh}

class Network:
    def __init__(self, input_size, hidden_sizes, output_size, layerTypes=[]):
        self.size = [input_size] + hidden_sizes + [output_size]
        if layerTypes == []:
            layerTypes = [0] * (len(self.size) - 1) + [1]
        self.layers = []
        for index, layer in enumerate(hidden_sizes):
            if (index == 0):
                self.layers.append(Layer(input_size, hidden_sizes[0]))
                self.layers.append(types[layerTypes[index]](hidden_sizes[0], hidden_sizes[0]))
            else:
                self.layers.append(Layer(hidden_sizes[index-1], layer))
                self.layers.append(types[layerTypes[index]](layer, layer))
        self.layers.append(types[layerTypes[-1]](hidden_sizes[-1], output_size))

    # Set loss function to use
    def use(self, loss, loss_prime):
        self.loss = loss
        self.loss_prime = loss_prime

    # run the network
    def forward(self, inputs):
        output = inputs
        for layer in self.layers:
            output = layer.forward(output)
        return output
    
    # train the network
    def fit(self, inputs, expected, epochs, learning_rate = 0.1):
        # sample dimension first
        samples = len(inputs)

        # training loop
        for _ in range(epochs):
            for i in range(samples):
                # forward propagation
                output = inputs[i]
                for layer in self.layers:
                    output = layer.forward(output)

                # backward propagation
                error = self.loss_prime(expected[i], output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, learning_rate)