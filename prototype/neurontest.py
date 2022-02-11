from neuron import neuron
import numpy as np
import matplotlib.pyplot as plt
from random import uniform
print('Now simulating full sending of 0.3 strength input')
n = neuron(np.array([1]), 0, 0.1, 0.1, 2, 0.1)
n.potential
outputs = []
for x in range(1000):
    n.evolve(np.array([0.3]))
    print(n.potential)
    outputs.append(n.potential)
plt.plot(range(1000), outputs)
print('Now showing results of full sending of 0.3 strength input')
plt.show()
print('Now simulating equally spread out 30 iteration long 0.3 strength input stimulation every 100 iterations')
n = neuron(np.array([1]), 0, 0.1, 0.1, 2, 0.1)
n.potential
outputs = []
for x in range(1000):
    n.evolve(np.array([((x % 100) > 70) * 0.3]))
    print(n.potential)
    outputs.append(n.potential)
plt.plot(range(1000), outputs)
print('Now showing results of equally spread out 30 iteration long 0.3 strength input stimulation every 100 iterations')
plt.show()
print('Now simulating random strength stimulation')
n = neuron(np.array([1]), 0, 0.1, 0.1, 2, 0.1)
n.potential
outputs = []
for x in range(1000):
    n.evolve(np.array([uniform(0, 1)]))
    print(n.potential)
    outputs.append(n.potential)
plt.plot(range(1000), outputs)
print('Now showing results of random strength stimulation')
plt.show()
print('Now simulating inhibitory stimulation')
n = neuron(np.array([-1]), 0, 0.1, 0.1, 2, 0.1)
n.potential
outputs = []
for x in range(1000):
    n.evolve(np.array([uniform(0, 1)]))
    print(n.potential)
    outputs.append(n.potential)
plt.plot(range(1000), outputs)
print('Now showing results of inhibitory stimulation')
plt.show()
