"""
This is a prototype model covering only a single neuron and has no synaptic plasticity capabilities. 
"""

import numpy as np


class Neuron:


    def __init__(self, weights, potential, cation, anion, depolarizationThreshold, refractoryThreshold, velocityDecay):
        self.weights = weights
        self.potential = potential
        self.cation = cation
        self.anion = anion
        self.depolarizationThreshold = depolarizationThreshold
        self.refractoryThreshold = refractoryThreshold
        self.synapseQuantity = len(weights)
        self.refractory = False
        self.cationInflux = 0
        self.velocityDecay = velocityDecay

    def evolve(self, inputs):
        # cationInflux is the amount of cations that flowed in this iteration, it carries a fraction of the previous iteration's influx with a bit added decided by the cation parameter and the potential of the neuron
        self.cationInflux = self.cationInflux * self.velocityDecay + self.cation * self.potential
        self.potential -= self.cationInflux
        # anionInflux is the amount of anions that flowed in this iteration and is decided by the sum of the input weight products along with a bit more that's dependent on the neuron's potential
        if not self.refractory:
            anionInflux = np.sum(inputs * self.weights) / self.synapseQuantity + self.anion * self.potential
            self.potential += anionInflux * (self.potential + anionInflux > 0)
        # this decides the absolute refractory period, as the neuron depolarizes it will reach a threshold which will trigger the absolute refractory period which will block all anion intake from that point until the absolute refractory period ends which is when it passes another threshold and enters the relative refractory period
        if self.refractory == False and self.potential >= self.depolarizationThreshold:
            self.refractory = True
        if self.refractory == True and self.potential <= self.refractoryThreshold:
            self.refractory = False

