import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from neuron import Neuron
from network import Network

netParams = np.array([[1.], [2.]]), np.array([0., 0.]), 0.1, 0.1, 1, 0, 0.55

print('Initializing nn and results list...')
nn = Network(*netParams)
results = [deepcopy(nn.potentials)]
print('Now executing experiment...')
for x in range(99):
    nn.evolve(np.array([0.3]))
    results.append(deepcopy(nn.potentials))
print('Processing results...')
results = np.array(results).T
print(f'Here are the results:\n{results.T}')
x = np.arange(100)
plt.plot(x, results[0], label = "neuron 0")
plt.plot(x, results[1], label = "neuron 1")
plt.legend()
plt.show()
