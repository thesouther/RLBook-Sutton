import os, sys
import time
import numpy as np


class RolloutWorker:
    def __init__(self, env, agent1, agent2):
        self.env = env
        if agent1.player == 'x' and agent2.player == 'o':
            self.player1 = agent1
            self.player2 = agent2
        elif agent1.player == 'o' and agent2.player == 'x':
            self.player1 = agent2
            self.player2 = agent1
        else:
            exit("游戏所属方错误：先手x，后手o！")

    def play_train(self, exchange_player=False):
        # 交换对手
        if exchange_player:
            exchP = self.player1
            self.player1 = self.player2
            self.player2 = exchP

        # 先随机下一步
        self.env.reset()
        a = self.env.sample_action()
        s_, r, terminal, win_tag = self.env.step(a)

        # #训练部分
        # train_epochs = 3
        # for epoch in range(train_epochs):
        #     step = 0
        #     while True:
        #         if terminal:
        #             break
        #         s = self.env.get_state()
        #         avail_acts = self.env.available_actions()
        #         action_space = self.env.action_space
        #         a = self.player1.choose_action(s, avail_acts, action_space)
        #         self.env.step(a)

        #         os.system('cls' if os.name == 'nt' else 'clear')
        #         print("epoch: {}, step: {}".format(epoch, step))
        #         self.env.render()
        #         time.sleep(1)
        #         step += 1
