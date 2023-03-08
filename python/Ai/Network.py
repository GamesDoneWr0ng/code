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

    """def Loss_CategoricalCrossentropy(self, Y_pred, Y_true):
        samples = len(Y_pred)
        y_pred_clipped = np.clip(Y_pred, 1e-7, 1-1e-7)

        if len(Y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), Y_true]
        else:
            correct_confidences = np.sum(y_pred_clipped*Y_true, axis=1)

        negative_log_likelihoods = -np.log(correct_confidences)

        data_loss = np.mean(negative_log_likelihoods)
        return data_loss"""