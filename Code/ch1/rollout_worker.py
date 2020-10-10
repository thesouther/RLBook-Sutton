class RolloutWorker:
    def __init__(self, env):
        self.env = env

    def self_play_train(self, env, player1, player2):
        env.reset()
        train_epochs = 3
        for epoch in range(train_epochs):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("epoch:", epoch)
            env.render()
            time.sleep(1)
