import numpy as np


class RandomAgent:
    def __init__(self, env):
        self.env = env

    def choose_action(self, env):
        while True:
            a = np.random.randint(env.action_space)
            if env.is_legal_move(a):
                return a

    def train(self):
        pass


class RLAgent:
    def __init__(self, env):
        self.env = env

    def choose_action(self, env):
        pass

    def train(self):
        pass


class HumanPlayer:
    def __init__(self, env):
        self.env = env
