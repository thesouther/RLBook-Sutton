import os, sys
import time
import numpy as np


class RolloutWorker:
    def __init__(self, env, agent, inner_player):
        self.env = env
        self.agent = agent
        self.inner_player = inner_player
        self.inner_player.owner = 'x'
        self.agent.owner = 'o'

    def _inner_player_go(self, env, s):
        """
        inner player go one step, and get agent's reward.
        """
        inner_a = self.inner_player.choose_action(env, s)
        s_, r, terminal, win_tag = self.env.step(inner_a)
        if terminal:
            if win_tag['win'] == self.inner_player.owner:
                r = -1
            else:
                r = 0
        return s_, r, terminal, win_tag

    def play_train(self, agent_first=False):
        """
        train agent
        s: the board before take action
        a: action
        r: ** use the reward after inner player go **
        s_: the board after agent and inner player plays.
        """
        train_epochs = 1
        alpha = 0.56
        gamma = 0.9
        print("start training...")
        for epoch in range(train_epochs):
            self.env.reset()
            step = 0
            if agent_first:
                # agent first, do nothing
                self.inner_player.owner = 'o'
                self.agent.owner = 'x'
                s, r, s_ = [], 0, self.env.get_state()
                terminal, win_tag = False, {'win': None}
                self.env.render()
            else:
                # inner player first, go one step
                self.inner_player.owner = 'x'
                self.agent.owner = 'o'
                s = self.env.get_state()
                s_, r, terminal, win_tag = self._inner_player_go(self.env, s)
                self.env.render()
            while True:
                if terminal:
                    self.env.reset()
                    break
                # agent play
                # get reward after inner player go
                s = s_
                a = self.agent.choose_action(self.env, s)
                sa, r, terminal, win_tag = self.env.step(a)
                # print("sa, r, terminal, win_tag", sa, r, terminal, win_tag)
                sa_id = self.env.get_q_id(sa)
                if not terminal:
                    # inner player go
                    s_, r, terminal, win_tag = self._inner_player_go(
                        self.env, sa)
                    # print("s_, r, terminal, win_tag", s_, r, terminal, win_tag)
                if terminal:
                    max_q_s_a = 0

                # Q = self.agent.q_table

                # avail_acts = self.env.get_available_actions()
                # values = []
                # for act in avail_acts:
                #     s_ = env.move(act)
                #     q_id = env.get_q_id(s_)
                #     # print(q_id)
                #     if q_id not in self.q_table:
                #         self.q_table[q_id] = 0
                #     values.append(self.q_table[q_id])
                #     env.un_move(act)
                # idx = np.random.choice(np.flatnonzero(np.isclose(values, max(values))))
                # a = avail_acts[idx]

                # max_q_s_a =
                # Q[sa_id] = Q[sa_id] + alpha(r + gamma * max_q_s_a - Q[sa_id])
                #(s, a, s_, r)

                # self.agent.train_one_step()

                self.env.render()

                # os.system('cls' if os.name == 'nt' else 'clear')
                # print("epoch: {}, step: {}".format(epoch, step))
                # self.env.render()
                # time.sleep(1)
                step += 1
