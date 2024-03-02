import numpy as np

class Neuron:

  def __init__(self, **kwargs):
    self.resting_potential = kwargs.get('potential', -65)
    self.potential = kwargs.get('potential', self.resting_potential)
    self.recovery = kwargs.get('recovery', 0)
    self.recovery_time_scale = kwargs.get('recovery_time_scale', 0.02)
    self.recovery_sensitivity = kwargs.get('recovery_sensitivity', 0.2)
    self.weights = kwargs.get('weights', 1)

  def step(inputs, dt = 1):
    self.potential += 
    self.recovery += 

