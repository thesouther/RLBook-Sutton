import os, sys
import time
from agent import RandomAgent, RLAgent, HumanPlayer
from MyEnvs.tic_tac_toe import TicTacToe


def human_vs_agent():
    human_player = HumanPlayer(env=env)


if __name__ == "__main__":
    env = TicTacToe(board_size=3)

    random_agent = RandomAgent(env=env)
    rl_agent = RLAgent(env=env)

    self_play_train(env, random_agent, rl_agent)