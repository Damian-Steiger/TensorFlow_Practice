import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

inputs = [1, 2, 3, 2.5]
weights = [[.2, .8, -.5, 1], [.5, -.91, .26, -.5], [-.26,-.27, .17, .87]]
biases = [2, 3, .5]


outputs = np.dot(weights, inputs) + biases

print(outputs)
    