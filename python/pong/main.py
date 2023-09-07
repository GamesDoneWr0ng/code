# Main class for pong
# Handels comunication between classes

import pygame as pg
import gymnasium as gym
from torch import Tensor, tensor, device, no_grad
from numpy import argmax
from torch.distributions.categorical import Categorical
from stable_baselines3.common.atari_wrappers import MaxAndSkipEnv
from pong import PongEnv
from ai import Agent
pg.init()

size = width, height = 800, 600
screen = pg.display.set_mode(size)
pg.display.set_caption("Pong")

class Main:
    def __init__(self) -> None:
        def make_env():
            def thunk():
                env = gym.make("Pong-v0")
                env = MaxAndSkipEnv(env, skip=4)
                return env
            return thunk
        
        env = gym.vector.SyncVectorEnv([make_env()])
        self.ai = Agent(env)
        self.ai.load("python/pong/policies/main.pt")

        self.pong = PongEnv(size, render_mode="human-vs-bot")

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
        with no_grad(): # ai
            logits = self.ai.actor(obs)
            probs = Categorical(logits=logits)
            #probs = torch.nn.functional.softmax(logits, dim=-1)
            #action = probs.cpu().sample()
            action = tensor(argmax(probs.probs.cpu().numpy(), keepdims=True).T, device=device("mps"))
            return action.cpu().numpy()[0]


main = Main()

obs = Tensor(main.pong.reset()[0])
main.running = True
while main.running:
    inputs = main.inputHandler()
    #opponent = main.getAi(obs)
    opponent = int(main.pong.ballPos[1] > main.pong.aiPaddle)

    obs = Tensor(main.pong.step(opponent, inputs)[0])
    main.pong.render()