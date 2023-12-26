import pygame as pg
from snake import SnakeEnv

env = SnakeEnv(render_mode="human")
env.render()

def inputs():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            env.close()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP or event.key == pg.K_w:
                return 0
            elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                return 1
            elif event.key == pg.K_DOWN or event.key == pg.K_s:
                return 2
            elif event.key == pg.K_LEFT or event.key == pg.K_a:
                return 3
    
    return None

while True:
    input = inputs()
    if input is not None:
        env.step(input)