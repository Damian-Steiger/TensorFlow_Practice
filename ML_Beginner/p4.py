import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

X = [[1, 2, 3, 2.5], [2, 5, -1, 2], [-1.5, 2.7, 3.3, -.8]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = .1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4, 5)
layer2 = Layer_Dense(5, 2)
layer3 = Layer_Dense(2, 10)

layer1.forward(X)
layer2.forward(layer1.output)
layer3.forward(layer2.output)

print(layer3.output)