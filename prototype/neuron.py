import numpy as np


class Neuron:


    def __init__(self, weights, potential, cation, anion, depolarizationThreshold, refractoryThreshold):
        self.weights = weights
        self.potential = potential
        self.cation = cation
        self.anion = anion
        self.depolarizationThreshold = depolarizationThreshold
        self.refractoryThreshold = refractoryThreshold
        self.synapseQuantity = len(weights)
        self.refractory = False
        self.cationInflux = 0

    def evolve(self, inputs):
        self.potential -= self.cationInflux
        self.cationInflux = self.cationInflux * 0.6 + self.cation * self.potential
        print('cation influx:', self.cationInflux)
        if not self.refractory:
            anionInflux = np.sum(inputs * self.weights) / self.synapseQuantity + self.anion * self.potential
            self.potential += anionInflux * (self.potential + anionInflux > 0)
        if self.refractory == False and self.potential >= self.depolarizationThreshold:
            print('\nRefractory period has started\n')
            self.refractory = True
        if self.refractory == True and self.potential <= self.refractoryThreshold:
            print('\nRefractory period has ended\n')
            self.refractory = False

