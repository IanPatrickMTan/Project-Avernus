from neuron import Neuron
import numpy as np
import matplotlib.pyplot as plt
from random import uniform
params = (np.array([1]), 0, 0.1, 0.1, 1, 0, 0.55)
print('Now simulating full sending of 0.3 strength input')
n = Neuron(*params)
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
n = Neuron(*params)
n.potential
outputs = []
for x in range(1000):
    n.evolve(np.array([((x % 100) > 95) * 0.3]))
    print(n.potential)
    outputs.append(n.potential)
plt.plot(range(1000), outputs)
print('Now showing results of equally spread out 30 iteration long 0.3 strength input stimulation every 100 iterations')
plt.show()
print('Now simulating random strength stimulation')
n = Neuron(*params)
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
n = Neuron(*params)
n.potential
outputs = []
for x in range(1000):
    n.evolve(np.array([-uniform(0, 1)]))
    print(n.potential)
    outputs.append(n.potential)
plt.plot(range(1000), outputs)
print('Now showing results of inhibitory stimulation')
plt.show()
print('Now commencing simulation of mixed stimulation')
n = Neuron(*params)
n.potential
outputs = []
for x in range(199):
    n.evolve(np.array([0]))
    print(n.potential)
    outputs.append(n.potential)
n.evolve(np.array([0.2]))
print(n.potential)
outputs.append(n.potential)
for x in range(199):
    n.evolve(np.array([0]))
    print(n.potential)
    outputs.append(n.potential)
n.evolve(np.array([0.4]))
print(n.potential)
outputs.append(n.potential)
for x in range(190):
    n.evolve(np.array([0]))
    print(n.potential)
    outputs.append(n.potential)
for x in range(10):
    n.evolve(np.array([0.2]))
    print(n.potential)
    outputs.append(n.potential)
for x in range(197):
    n.evolve(np.array([0]))
    print(n.potential)
    outputs.append(n.potential)
n.evolve(np.array([1]))
print(n.potential)
outputs.append(n.potential)
n.evolve(np.array([0]))
print(n.potential)
outputs.append(n.potential)
n.evolve(np.array([1]))
print(n.potential)
outputs.append(n.potential)
for x in range(200):
    n.evolve(np.array([0]))
    print(n.potential)
    outputs.append(n.potential)
plt.plot(range(1000), outputs)
print('Now showing results of mixed stimulation')
plt.show()
