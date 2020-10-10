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
        self.curr_player = 'x'
        self.actions = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1],
                                 [1, 2], [2, 0], [2, 1], [2, 2]])
        self.action_space = len(self.actions)

    def reset(self):
        self.board = self._new_board()

    def step(self, a):
        s, a, r, s_ = [], [], [], []
        if self.is_end:
            pass
        else:
            pass
        return s, a, r, s_

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

    def render(self):
        board = '\n'.join([' '.join(row) for row in self.board])
        print("{}".format(board))
