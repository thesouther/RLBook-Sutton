import numpy as np
import os, sys
import time

PLAYERS = ['x', 'o']


class TicTacToe:
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = self._new_board()
        self.player1 = 'x'
        self.player2 = 'o'
        self.curr_player = self.player1
        self.actions = np.array([[i // board_size, i % board_size]
                                 for i in range(board_size * board_size)])
        self.action_space = [i for i in range(len(self.actions))]

    def reset(self):
        self.board = self._new_board()

    def step(self, a):
        s_, r, terminal, = [], 0, False
        win_tag = {"player1": None, "player2": None}
        # 下棋
        x, y = self.actions[a]
        self.board[x][y] = self.curr_player
        # 判断是否赢棋或者结束
        if self.is_end:
            pass
        else:
            pass
        return s_, r, terminal, win_tag

    def is_end(self):
        for row in self.board:
            if '.' in row:
                return False
        return True

    def get_reward(self):
        pass

    def _new_board(self):
        return [['.' for _ in range(self.board_size)]
                for _ in range(self.board_size)]

    def is_legal_move(self, a):
        x = self.actions[a][0]
        y = self.actions[a][1]
        return 0 <= x < self.board_size and 0 <= y < self.board_size and self.board[
            x][y] == '.'

    def available_actions(self):
        avail_act = []
        for a in self.action_space:
            if self.is_legal_move(a):
                avail_act.append(a)
        return avail_act

    def sample_action(self):
        avail_acts = self.available_actions()
        return np.random.choice(avail_acts)

    def get_state(self):
        return self.board

    def render(self):
        board = '\n'.join([' '.join(row) for row in self.board])
        print("{}".format(board))
