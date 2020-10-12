import os, sys
import time
from agent import RandomAgent, RLAgent, HumanPlayer
from MyEnvs.tic_tac_toe import TicTacToe
from rollout_worker import RolloutWorker


def main():
    env = TicTacToe(board_size=3)
    # x先手，o后手
    random_agent = RandomAgent()
    rl_agent = RLAgent()
    rollout_worker = RolloutWorker(env=env,
                                   agent=rl_agent,
                                   inner_player=random_agent)
    # 通过与随机智能体博弈训练RL智能体
    rollout_worker.play_train(exchange_player=False)


if __name__ == "__main__":
    main()