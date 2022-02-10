if __name__ == '__main__':
    from neuron import neuron
    import numpy as np
    import matplotlib.pyplot as plt
    from random import uniform
    n = neuron(np.array([1]), 0, 0.1, 0.1, 2, 0.1)
    n.potential
    outputs = []
    for x in range(1000):
        n.evolve(np.array([0.3]))
        print(n.potential)
        outputs.append(n.potential)
    plt.plot(range(1000), outputs)
    plt.show()
    n = neuron(np.array([1]), 0, 0.1, 0.1, 2, 0.1)
    n.potential
    outputs = []
    for x in range(1000):
        n.evolve(np.array([((x % 100) > 70) * 0.3]))
        print(n.potential)
        outputs.append(n.potential)
    plt.plot(range(1000), outputs)
    plt.show()
    n = neuron(np.array([1]), 0, 0.1, 0.1, 2, 0.1)
    n.potential
    outputs = []
    for x in range(1000):
        n.evolve(np.array([uniform(0, 1)]))
        print(n.potential)
        outputs.append(n.potential)
    plt.plot(range(1000), outputs)
    plt.show()
    n = neuron(np.array([-1]), 0, 0.1, 0.1, 2, 0.1)
    n.potential
    outputs = []
    for x in range(1000):
        n.evolve(np.array([uniform(0, 1)]))
        print(n.potential)
        outputs.append(n.potential)
    plt.plot(range(1000), outputs)
    plt.show()
