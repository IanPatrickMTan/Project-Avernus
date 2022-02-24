import numpy as np


class Network:


    def __init__(self, weights, potentials, cation, anion, depolThresh, refractThresh, velDec):
        self.weights = weights
        self.potentials = potentials
        self.cation = cation
        self.anion = anion
        self.depolThresh = depolThresh
        self.refractThresh = refractThresh
        self.velDec = velDec
        self.absRefract = np.full(len(weights), False)
        self.cationIn = np.zeros(len(weights[0]))

    def evolve(self, inputs):
        self.cationIn = self.cationIn * self.velDec + self.cation * self.potentials
        self.potentials -= self.cationIn

        depoling = np.where(~self.absRefract)[0]
        notDepoling = np.where(self.absRefract)[0]
        anionIn = self.weights[depoling] @ inputs / len(self.weights[0]) + self.anion * self.potentials[depoling]
        excited = np.where(self.potentials[depoling] + anionIn > 0)
        self.potentials[depoling[excited]] += anionIn[excited]
        
        self.absRefract[np.where(self.potentials[depoling] >= self.depolThresh)] = True
        self.absRefract[np.where(self.potentials[notDepoling] <= self.refractThresh)] = False
