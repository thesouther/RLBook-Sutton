import os, sys
import time
from agent import RandomAgent, RLAgent, HumanPlayer
from MyEnvs.tic_tac_toe import TicTacToe
from rollout_worker import RolloutWorker


def main():
    env = TicTacToe(board_size=3)
    random_agent = RandomAgent()
    rl_agent = RLAgent(epsilon=0.1)
    rollout_worker = RolloutWorker(env=env,
                                   agent=rl_agent,
                                   inner_player=random_agent)
    # train RL agent with random agent
    rollout_worker.play_train(agent_first=False)


if __name__ == "__main__":
    main()