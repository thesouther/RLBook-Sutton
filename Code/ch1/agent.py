import numpy as np


class RandomAgent:
    def __init__(self, player='x'):
        self.player = player

    def choose_action(self, s, avail_acts, action_space):
        return np.random.choice(avail_acts)

    def train(self):
        pass


class RLAgent:
    def __init__(self, player='o'):
        self.player = player

    def choose_action(self, env):
        pass

    def train(self):
        pass


class HumanPlayer:
    def __init__(self, player='x'):
        self.player = player
