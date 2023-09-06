# Main class for pong
# Handels comunication between classes

import pygame as pg
import time
from pong import PongEnv
#from ai import Ai
pg.init()

size = width, height = 800, 600
screen = pg.display.set_mode(size)
pg.display.set_caption("Pong")
clock = pg.time.Clock()
fps = 60

class Main:
    def __init__(self) -> None:
        self.pong = PongEnv(size, render_mode="human-vs-bot")
        #self.ai = Ai()

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

main = Main()

main.running = True
while main.running:
    clock.tick(fps)

    inputs = main.inputHandler()
    #ai = main.ai.update(main.pong.getState())
    main.pong.step(0, inputs)#, ai)
    main.pong.render()