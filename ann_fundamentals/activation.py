import numpy as np


class Activation():
    def __init__(self, x):
        self.x = x

    def linear(self):
        return self.x

    def relu(self):
        return np.where(self.x > 0, self.x, 0)
