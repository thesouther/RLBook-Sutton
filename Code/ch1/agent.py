import numpy as np


class RandomAgent:
    def __init__(self, owner='x'):
        self.owner = owner

    def best_action(self, s, avail_acts, action_space):
        return np.random.choice(avail_acts)

    def choose_action(self, env, s):
        """
        random choice from available actions
        """
        avail_acts = env.get_available_actions()
        return self.best_action(avail_acts)

    def train(self):
        pass


class RLAgent:
    """
    Q-Learning agent
    """
    def __init__(self, owner='o', epsilon=0.1):
        self.owner = owner
        self.q_table = {}
        self.epsilon = epsilon

    def best_move(self, env):
        """
        choose best action from q-table, if the q not in q-table, set it 0.
        """
        avail_acts = env.get_available_actions()
        values = []
        for act in avail_acts:
            s_ = env.move(act)
            q_id = env.get_q_id(s_)
            # print(q_id)
            if q_id not in self.q_table:
                self.q_table[q_id] = 0
            values.append(self.q_table[q_id])
            env.un_move(act)
        idx = np.random.choice(np.flatnonzero(np.isclose(values, max(values))))
        a = avail_acts[idx]
        return a

    def choose_action(self, env, s):
        """
        choose action use epsilon-greedy policy.
        """
        avail_acts = env.get_available_actions()
        action_space = env.action_space
        prob = np.random.random()
        if prob < self.epsilon:
            a = self._random_action(avail_acts)
        else:
            a = self.best_move(env)
        return a

    def update_q_table(self, q_id):
        state = "".join([''.join(row) for row in s])
        value = self.cal_value(state)
        self.q_table[state] = value

    def train_one_step(self):
        pass

    def _random_action(self, avail_acts):
        return np.random.choice(avail_acts)


class HumanPlayer:
    def __init__(self, owner='x'):
        self.owner = owner
