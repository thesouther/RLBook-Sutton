import numpy as np


class RandomAgent:
    def __init__(self, owner='x'):
        self.owner = owner

    def choose_action(self, s, avail_acts, action_space):
        return np.random.choice(avail_acts)

    def train(self):
        pass


class RLAgent:
    def __init__(self, owner='o'):
        self.owner = owner

    def choose_action(self, env):
        pass

    def train(self):
        pass


class HumanPlayer:
    def __init__(self, owner='x'):
        self.owner = owner
