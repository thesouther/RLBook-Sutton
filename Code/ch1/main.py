import os, sys
import time
from agent import RandomAgent, RLAgent, HumanPlayer
from MyEnvs.tic_tac_toe import TicTacToe


def self_play_train(env, player1, player2):
    env.reset()
    train_epochs = 3
    for epoch in range(train_epochs):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("epoch:", epoch)
        env.render()
        time.sleep(1)


def human_vs_agent():
    human_player = HumanPlayer(env=env)


if __name__ == "__main__":
    env = TicTacToe(board_size=3)

    random_agent = RandomAgent(env=env)
    rl_agent = RLAgent(env=env)

    self_play_train(env, random_agent, rl_agent)