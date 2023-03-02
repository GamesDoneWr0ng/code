from Node import Node
import random

class Network:
    def __init__(self, input_size, output_size, hidden_sizes):
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_sizes = hidden_sizes
        self.nodes = []
        self.layers = []
        
        # Create input nodes
        layer = []
        for i in range(input_size):
            node = Node(0, {})
            self.nodes.append(node)
            layer.append(node)
        self.layers.append(layer.copy())

        # Create hidden nodes
        for i, size in enumerate(hidden_sizes):
            layer = []
            for i in range(size):
                node = Node(i+1, {})
                self.nodes.append(node)
                layer.append(node)
            self.layers.append(layer.copy())

        # Create output nodes
        layer = []
        for i in range(output_size):
            node = Node(-1, {})
            self.nodes.append(node)
            layer.append(node)
        self.layers.append(layer.copy())

        # Connect nodes
        for i, node in enumerate(self.nodes):
            if node.layer == -2:
                continue
                
            for next_node in self.nodes:
                if next_node.layer == node.layer + 1 or next_node.layer == -1:
                    weight = random.uniform(-1, 1)
                    node.connections[next_node] = weight
    
    def activate(self, inputs):
        # reset deltas
        for node in self.nodes:
            node.delta = 0.0

        # input layer
        for node, input in self.layers[0], inputs:
            node.delta = input
            node.activate()

        # Propagate values forward, one layer at a time
        for layer in self.layers[1:]:
            for node in layer:
                node.activate()