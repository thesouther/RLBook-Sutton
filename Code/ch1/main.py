import os, sys
import time
from agent import RandomAgent, RLAgent, HumanPlayer
from MyEnvs.tic_tac_toe import TicTacToe
from rollout_worker import RolloutWorker


def main():
    env = TicTacToe(board_size=3)
    # x先手，o后手
    random_agent = RandomAgent(player='x')
    rl_agent = RLAgent(player='o')
    rollout_worker = RolloutWorker(env=env,
                                   agent1=random_agent,
                                   agent2=rl_agent)
    # 通过与随机智能体博弈训练RL智能体
    rollout_worker.play_train(exchange_player=False)


if __name__ == "__main__":
    main()