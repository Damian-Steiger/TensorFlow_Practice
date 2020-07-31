import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

inputs = [1, 2, 3, 2.5]
weights1 = [.2, .8, -.5, 1]
weights2 = [.5, -.91, .26, -.5]
weights3 = [-.26,-.27, .17, .87]

bias1 = 2
bias2 = 3
bias3 = .5

output = [np.sum(np.multiply(inputs, weights1)) + bias1, np.sum(np.multiply(inputs, weights2)) + bias2, np.sum(np.multiply(inputs, weights3)) + bias3 ]

print(output)

