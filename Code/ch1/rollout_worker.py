import os, sys
import time
import numpy as np


class RolloutWorker:
    def __init__(self, env, agent, inner_player):
        self.env = env
        self.agent = agent
        self.inner_player = inner_player
        # 默认内置对手先手，智能体后手
        self.inner_player.owner = 'x'
        self.agent.owner = 'o'

    def _inner_player_go(self, s):
        inner_a = self.inner_player.choose_action(s, avail_acts, action_space)
        s_, r, terminal, win_tag = self.env.step(inner_a)
        return s_, r, terminal, win_tag

    def play_train(self, agent_first=False):
        train_epochs = 3

        self.env.reset()
        action_space = self.env.action_space
        s, r, s_ = [], 0, self.env.get_state()
        terminal, win_tag = False, {'win': None}

        #训练部分
        for epoch in range(train_epochs):
            self.env.reset()
            step = 0
            if agent_first:
                # 智能体先手
                self.inner_player.owner = 'o'
                self.agent.owner = 'x'
            else:
                # 内置对手先手，先走一步
                self.inner_player.owner = 'x'
                self.agent.owner = 'o'
                s_, _, terminal, win_tag = self._inner_player_go(
                    self.env.get_state(), self.env.available_actions(),
                    action_space)

            while True:
                if terminal:
                    break
                    print(r, terminal, win_tag)

                # 智能体视角下下棋
                # 奖励使用下棋之后、内置智能体下棋之前的奖励。
                s = s_
                avail_acts = self.env.available_actions()
                a = self.agent.choose_action(s, avail_acts, action_space)
                s_, r, terminal, win_tag = self.env.step(a)
                if not terminal:
                    s_, r, terminal, win_tag = self._inner_player_go(
                        self.env.get_state(), self.env.available_actions(),
                        action_space)

                # player1 先手下棋
                p1_s = s

                p1_a = self.player1.choose_action(s, avail_acts, action_space)
                s_, r_, terminal, win_tag = self.env.step(a)
                #p1: (s, a, r, s_)

                # player2 后手下棋
                avail_acts = self.env.available_actions()
                p2_s = s_
                p2_a = self.player1.choose_action(p2_s, avail_acts,
                                                  action_space)
                s, r, terminal, win_tag = self.env.step(p2_a)
                p2_s_ = 0
                p2_r = 0
                #p2: (s, a, r, s_)

                self.env.render()

                # os.system('cls' if os.name == 'nt' else 'clear')
                # print("epoch: {}, step: {}".format(epoch, step))
                # self.env.render()
                # time.sleep(1)
                step += 1
