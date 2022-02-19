import numpy as np


class Network


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
        self.cationIn = self.cationIn * self.velDec + self.action * self.potentials
        self.potentials -= self.cationIn

        depoling = np.where(absRefract)
        anionIn = np.sum(inputs[depoling] * self.weights[depoling]) / len(self.weights[0]) + self.anion * self.potentials[depoling]
        self.potentials[np.where(absRefract and )]
