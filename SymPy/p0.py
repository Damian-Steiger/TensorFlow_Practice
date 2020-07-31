import numpy as np 
from sympy import *

class Neuron:
    def __init__(self):
        self.weights = []
        self.bias = 0
        self.out = 0

    def ReLu(self):
        return max(0, self.out)

    def Sigmoid(self):
        return (1 / 1 + np.exp ^ (-self.out))

class Layer:
    def __init__(self):
        self.neurons = []
    
    def add(self, neuron):
        self.neurons.append(neuron)

    def print(self):
        for x in range(len(self.neurons)):
            print(self.neurons[x].out)
    
    def magnitude(self):
        return len(self.neurons)
    
    def inti_first(self, data):
        for x in range(len(data)):
            self.neurons[x].out = data[x]
    
    def populate(self, data):
        for y in range(len(data)):
            self.neurons[y].weights.append(.5)
        for x in range(self.magnitude()):
            self.neurons[x].out = np.dot(self.neurons[x].weights, data) + self.neurons[x].bias


def makeLayer(size):
    layer = Layer()
    for x in range(size):
        layer.add(Neuron())
    return layer

def main():
    data = [1, 2, 3, 4]
    layer0 = makeLayer(4)
    layer1 = makeLayer(8)
    layer2 = makeLayer(16)
    layer3 = makeLayer(8)
    layer4 = makeLayer(4)

    layer0.inti_first(data)
    layer1.populate(layer0.neurons)
    layer2.populate(layer1.neurons)
    layer3.populate(layer2.neurons)
    layer4.populate(layer3.neurons)

if __name__ == "__main__":
    main()


    