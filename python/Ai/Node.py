import random

single_output = False

class Node:
    def __init__(self, layer, connections):
        # layer 0 = input, numbers = layer, -1 = output, -2 = bias
        self.layer = layer
        self.connections = connections
        self.delta = 0.0
        self.active = False
        if layer == -2:
            self.activationReq = -1
        else:
            self.activationReq = random.uniform(0.5, 5)
    
    def activate(self):
        if self.layer == -1:
            if single_output:
                return self.delta
            else:
                return self.delta > self.activationReq

        if self.delta > self.activationReq:
            for i in self.connections:
                i.receive_power(self.connections[i])
    
    def receive_power(self, power):
        self.delta += power