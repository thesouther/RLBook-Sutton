import numpy as np
import os, sys
import time

PLAYERS = ['x', 'o']


class TicTacToe:
    def __init__(self, board_size=3):
        """
        初始换棋盘参数。
        """
        self.board_size = board_size
        self.player1 = PLAYERS[0]
        self.player2 = PLAYERS[1]
        self._new_board()
        self.actions = np.array([[i // self.board_size, i % self.board_size]
                                 for i in range(self.board_size *
                                                self.board_size)])
        self.action_space = [i for i in range(len(self.actions))]

    def _new_board(self):
        self.curr_player = self.player1
        self.terminal = False
        self.board = [['.' for _ in range(self.board_size)]
                      for _ in range(self.board_size)]

    def step(self, a):
        """
        进行一步走棋， 之后交换下棋方
        """
        if self.terminal:
            exit("please reset your environment!")
        s_, r, = [], 0
        win_tag = {"win": None}
        # 下棋
        x, y = self.actions[a]
        self.board[x][y] = self.curr_player
        # 判断是否赢棋或者结束
        if self.is_end():
            self.terminal = True
            if self.has_won(self.curr_player):
                win_tag["win"] = self.curr_player
            elif self.has_won(self.get_opposite(self.curr_player)):
                win_tag["win"] = self.get_opposite(self.curr_player)
            else:
                win_tag["win"] = None
        r = self.get_reward()
        s_ = self.board
        # 交换下棋方
        self.curr_player = self.get_opposite(self.curr_player)
        return s_, r, self.terminal, win_tag

    def get_reward(self):
        if self.has_won(self.curr_player):
            return 1
        elif self.has_won(self.get_opposite(self.curr_player)):
            return 0
        else:
            return 0.5

    def get_opposite(self, player):
        opposite = PLAYERS[0] if player == PLAYERS[1] else PLAYERS[1]
        return opposite

    def has_won(self, player):
        """
        检查行、列、两个对角是否相同
        """
        board_size = self.board_size
        b = self.board
        bt = np.array(self.board).T.tolist()
        bd = [[self.board[x + i * dx][y + i * dy] for i in range(board_size)]
              for (x, y, dx, dy) in [(0, 0, 1, 1), (board_size - 1, 0, -1, 1)]]
        for row in b + bt + bd:
            if len(set(row)) == 1 and row[0] == player:
                return True
        return False

    def is_end(self):
        return self.is_over() or self.has_won(self.player1) or self.has_won(
            self.player2)

    def is_over(self):
        for row in self.board:
            if '.' in row:
                return False
        return True

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
        if self.terminal:
            exit("please reset your environment!")
        avail_acts = self.available_actions()
        return np.random.choice(avail_acts)

    def get_state(self):
        return self.board

    def render(self):
        board = '\n'.join([' '.join(row) for row in self.board])
        print("{}".format(board))

    def reset(self):
        self._new_board()


if __name__ == "__main__":
    env = TicTacToe(board_size=3)
    env.reset()
    a = env.sample_action()
    s_, r, terminal, win_tag = env.step(a)
    for i in range(10):
        a = env.sample_action()
        s_, r, terminal, win_tag = env.step(a)
        env.render()
        print(r, terminal, win_tag)