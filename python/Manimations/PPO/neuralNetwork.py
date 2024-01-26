from manim import *
np.random.seed(0)

class NeuralNetworkMobject(VGroup):
    def __init__(self, neural_network_architecture, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.layers = self.create_layers(neural_network_architecture)
        self.neurons = VGroup(*[neuron for layer in self.layers for neuron in layer])
        self.add(self.layers)
        self.connections = self.create_connections(neural_network_architecture)
        self.add(self.connections)

    def create_layers(self, neural_network_architecture):
        layers = VGroup()
        for layer_index, layer_size in enumerate(neural_network_architecture):
            layer = VGroup(*[Circle(radius=0.5) for _ in range(layer_size)])
            layer.arrange(DOWN, buff=0.5)
            layer.set_fill(ManimColor((112,56,105)), opacity=1)
            layer.set_z_index(1)
            layers.add(layer)
        layers.arrange(RIGHT, buff=1)
        return layers

    def create_connections(self, neural_network_architecture):
        connections = VGroup()
        for layer_index in range(len(neural_network_architecture) - 1):
            layer = VGroup()
            for neuron_index_pre, neuron_pre in enumerate(self.layers[layer_index]):
                for neuron_index_post, neuron_post in enumerate(self.layers[layer_index + 1]):
                    line = Line(neuron_pre.get_center(), neuron_post.get_center())
                    line.set_z_index(-1)
                    colorValue = np.random.randint(0,255)
                    line.set_color(ManimColor((colorValue, 0, 255-colorValue)))
                    layer.add(line)
            connections.add(layer)
        return connections

class NeuralNetworkScene(Scene):
    def construct(self):
        architecture = [4, 3, 2]  # Example architecture: 3 input, 4 hidden, 2 output neurons
        neural_network = NeuralNetworkMobject(architecture)
        
        # Animate the creation of the network
        for layer in neural_network.layers:
            self.play(Create(layer, lag_ratio=0.2))
            self.wait(0.2)  # Small wait time between layer draws

        # Animate the creation of the network
        for layer in neural_network.connections:
            self.play(Create(layer, lag_ratio=0.2))
            self.wait(0.2)  # Small wait time between layer draws

        self.wait(1)  # Wait for 1 second at the end