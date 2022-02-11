import numpy as np


class neuron:


    def __init__(self, weights, potential, cation, anion, depolarizationThreshold, refractoryThreshold):
        self.weights = weights
        self.potential = potential
        self.cation = cation
        self.anion = anion
        self.depolarizationThreshold = depolarizationThreshold
        self.refractoryThreshold = refractoryThreshold
        self.synapseQuantity = len(weights)
        self.refractory = False

    def evolve(self, inputs):
        self.potential -= self.cation * self.potential
        if not self.refractory:
            self.potential += self.anion * self.potential
            self.potential += np.sum(inputs * self.weights) / self.synapseQuantity
            self.potential = self.potential * (self.potential > 0)
        if self.refractory == False and self.potential >= self.depolarizationThreshold:
            print('\nRefractory period has started\n')
            self.refractory = True
        if self.refractory == True and self.potential <= self.refractoryThreshold:
            print('\nRefractory period has ended\n')
            self.refractory = False
