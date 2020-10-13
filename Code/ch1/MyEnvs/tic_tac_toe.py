import numpy as np
import os, sys
import time
from agent import RandomAgent

PLAYERS = ['x', 'o']


class TicTacToe:
    def __init__(self, board_size=3, agent_first=False, inner_player=None):
        """
        'x' first, 'o' second
        """
        self.board_size = board_size
        self.player1 = PLAYERS[0]
        self.player2 = PLAYERS[1]
        self.actions = np.array([[i // self.board_size, i % self.board_size]
                                 for i in range(self.board_size *
                                                self.board_size)])
        self.action_space = [i for i in range(len(self.actions))]
        self.agent_first = agent_first
        self.inner_player = inner_player

        if self.inner_player is None:
            self._init_inner_player()

        self._new_board()

    def _init_inner_player(self):
        if self.agent_first:
            random_agent = RandomAgent(owner='o')
        else:
            random_agent = RandomAgent(owner='x')
        self.inner_player = random_agent

    def _new_board(self):
        self.curr_player = self.player1
        self.terminal = False
        self.board = [['.' for _ in range(self.board_size)]
                      for _ in range(self.board_size)]
        if not self.agent_first:
            self.inner_player_go(self.get_state())

    def inner_player_go(self, s):
        avail_acts = self.get_available_actions()
        action_space = self.action_space
        a = self.inner_player.best_action(s, avail_acts, action_space)
        s_ = self.move(a)
        return s_

    def move(self, a):
        """
        go play and exchange current player.
        """
        if not self.terminal and a in self.get_available_actions():
            x, y = self.actions[a]
            self.board[x][y] = self.curr_player
            # exchange current player
            self.curr_player = self.get_opposite(self.curr_player)
            return self.board

    def check_win_tag(self, check_agent=True):
        win_tag = {"win": None}
        if check_agent:
            if self.has_won(self.curr_player):
                win_tag["win"] = "agent"
            elif self.has_won(self.get_opposite(self.curr_player)):
                win_tag["win"] = "inner_player"
            else:
                win_tag["win"] = "draw"
            r = self.get_reward(self.curr_player)
        else:
            if self.has_won(self.curr_player):
                win_tag["win"] = "inner_player"
            elif self.has_won(self.get_opposite(self.curr_player)):
                win_tag["win"] = "agent"
            else:
                win_tag["win"] = "draw"
            r = self.get_reward(self.get_opposite(self.curr_player))
        self.terminal = True
        return win_tag, r

    def step(self, a):
        """
        go one step and exchange current player.
        """
        if self.terminal and a not in self.get_available_actions():
            exit("please reset your environment!")
        s_, r, = [], 0
        win_tag = {"win": None}
        sa = self.move(a)
        # one player has won or the game has ended.
        if self.is_end():
            win_tag, r = self.check_win_tag(check_agent=True)
            return sa, r, self.terminal, win_tag
        # not end inner player goone step.
        s_ = self.inner_player_go(sa)
        if self.is_end():
            win_tag, r = self.check_win_tag(check_agent=False)
            return s_, r, self.terminal, win_tag
        r = self.get_reward(self.curr_player)
        return s_, r, self.terminal, win_tag

    def un_move(self, a):
        x, y = self.actions[a]
        self.board[x][y] = '.'
        self.curr_player = self.get_opposite(self.curr_player)
        self.terminal = False

    def get_reward(self, player):
        """
        get current player's reward
        """
        if self.has_won(player):
            return 1
        elif self.has_won(self.get_opposite(player)):
            return -1
        else:
            return 0

    def get_opposite(self, player):
        """
        get opposite player
        """
        opposite = PLAYERS[0] if player == PLAYERS[1] else PLAYERS[1]
        return opposite

    def has_won(self, player):
        """
        check rows, columns and diagonal lines
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

    def get_available_actions(self):
        avail_act = []
        for a in self.action_space:
            if self.is_legal_move(a):
                avail_act.append(a)
        return avail_act

    def sample_action(self):
        if self.terminal:
            exit("please reset your environment!")
        avail_acts = self.get_available_actions()
        return np.random.choice(avail_acts)

    def get_state(self):
        return self.board

    def get_q_id(self, s):
        return "".join([''.join(row) for row in s])

    def render(self):
        board = '\n'.join([' '.join(row) for row in self.board])
        print("{}".format(board))
        print()

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