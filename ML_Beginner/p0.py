import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

inputs = [1, 5, 2]
weights = [3, 2, 8]
bias = 3

output = np.sum(np.multiply(inputs, weights)) + bias

print(output)