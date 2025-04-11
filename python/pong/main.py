# Main class for pong
# Handels comunication between classes and inputs

import pygame as pg
import gymnasium as gym
from stable_baselines3 import PPO
from torch import Tensor
from pong import PongEnv
pg.init()

size = width, height = 800, 600
screen = pg.display.set_mode(size)
pg.display.set_caption("Pong")

gym.register( # register the environment
    id='Pong-v0',
    entry_point='pong:PongEnv')

class Main:
    def __init__(self) -> None:
        self.model = PPO.load("python/pong/policies/stablebase")
        self.pong = PongEnv(size, render_mode="human")

    def inputHandler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            return -4
        elif keys[pg.K_s] or keys[pg.K_DOWN]:
            return 4
        return 0
    
    def getAi(self, obs):
        action, _states = self.model.predict(obs)
        return int(action)

main = Main()

obs = Tensor(main.pong.reset()[0])
main.running = True
t = 0
while main.running:
    inputs = main.inputHandler()
    if t == 0:
        opponent = main.getAi(obs)
    t = (t+1) % 5
    #opponent = int(main.pong.ballPos[1] > main.pong.aiPaddle)

    obs = Tensor(main.pong.step(opponent, inputs)[0])
    main.pong.render()