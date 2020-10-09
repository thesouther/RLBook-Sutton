import numpy as np

PLAYERS = ['x', 'o']


class TicTacToe:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = self.new_board()

    def reset(self):
        self.board = self.new_board()

    def step(self):
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

    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        board = '\n'.join([' '.join(row) for row in self.board])
        print(board)