import numpy as np

class Network:
    def __init__(self, structure):
        self.structure = structure
        self.num_layers = len(structure) 
        self.biases = [np.random.randn(l, 1) for l in structure[1:]] 

        self.weights = [np.random.randn(l, next_l) for l, next_l in zip(structure[:-1], structure[1:])]

    def backprop(self, x, y):
        # forward
        მJⳆმBₙₛ = [np.zeros(b.shape) for b in self.biases]
        მJⳆმWₙₛ = [np.zeros(W.shape) for W in self.weights]

        preActivations = []
        activations = []
        for b, W in zip(self.biases, self.weights):
            z = W.T @ activation + b if preActivations else W.T @ x + b
            activation = sigma(z)
            preActivations.append(z)
            activations.append(activation)

        # backward
        H = self.num_layers-2
        for layer in range(H, -1, -1):
            delta =  sigmaPrime(preActivations[layer]) * (self.weights[layer+1] @ delta) if layer != H else ᐁC(activations[layer], y) * sigmaPrime(preActivations[layer])
            მJⳆმBₙₛ[layer] = delta
            მJⳆმWₙₛ[layer] = activations[layer-1] @ delta.T if layer != 0 else x @ delta.T

        return (მJⳆმBₙₛ, მJⳆმWₙₛ)

    def gradient_descent(self, mini_batch, λ):
        მJⳆმBₙ= [np.zeros(b.shape) for b in self.biases]
        მJⳆმWₙ = [np.zeros(W.shape) for W in self.weights]

        for x, y in mini_batch:
            მJⳆმBₙₛ, მJⳆმWₙₛ = self.backprop(x, y)
            მJⳆმBₙ = [მJⳆმb + მJⳆმbₛ for მJⳆმb, მJⳆმbₛ in zip(მJⳆმBₙ, მJⳆმBₙₛ)]
            მJⳆმWₙ = [მJⳆმW + მJⳆმWₛ for მJⳆმW, მJⳆმWₛ in zip(მJⳆმWₙ, მJⳆმWₙₛ)]

        d = len(mini_batch)
        self.weights = [W - λ/d * მJⳆმW for W, მJⳆმW in zip(self.weights, მJⳆმWₙ)]
        self.biases = [b - λ/d * მJⳆმb for b, მJⳆმb in zip(self.biases, მJⳆმBₙ)]

    def train(self, epochs, training_data, λ):
        for _ in range(epochs):
            for mini_batch in training_data:
                self.gradient_descent(mini_batch, λ)       


def ᐁC(aᴺ, y):
    return (aᴺ-y)                 #so we can easily change the cost.


def sigma(z):
    return 1.0/(1.0+np.exp(-z))


def sigmaPrime(z):
    return sigma(z)*(1-sigma(z))


my_net = Network([3, 2 ,2])
print("Initial Weights:")
print(my_net.weights[0])
#the following generates a list of cnt vectors of length dim.
random_vectors = lambda dim, cnt: [np.random.normal(size=(dim, 1)) for _ in range(cnt)]
#random_batch= list(zip(random_vectors(3, 64) , random_vectors(2, 64)))
#my_net.gradient_descent(random_batch, 3.0)
data = [list(zip(random_vectors(3, 64) , random_vectors(2, 64))) for _ in range(5)]
my_net.train(1000, data, 3.0)
print("Optimized Weights:")
print(my_net.weights[0])