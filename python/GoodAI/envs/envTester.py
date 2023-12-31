import pygame as pg
import gymnasium as gym

clock = pg.time.Clock()
env = gym.make("CartPole-v1", render_mode="human")
env.reset()
env.metadata["render_fps"] = 9999999

def inputs():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            env.close()
        #elif event.type == pg.KEYDOWN:
        #    if event.key == pg.K_RIGHT or event.key == pg.K_d:
        #        return 2
        #    elif event.key == pg.K_LEFT or event.key == pg.K_a:
        #        return 0
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            return 1
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            return 0
    

last_action = 0
while True:
    #clock.tick(60)
    action = inputs()
    if action is not None:
        last_action = action
    env.step(last_action)