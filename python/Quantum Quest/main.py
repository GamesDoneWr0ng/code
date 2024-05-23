if __name__ != "__main__":
    raise ImportError("This file is not meant to be imported")

from world.Camera import Camera
from world.World import World
import pygame as pg
import numpy as np
pg.init()

SIZE = WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()
scale = 16

world = World(screen)

camera = Camera(scale, world.getPlayer(), 
                np.array([[-WIDTH, -HEIGHT], [WIDTH, HEIGHT]], dtype=np.float64) / (scale* 4), 
                np.array([[-WIDTH, -HEIGHT], [WIDTH, HEIGHT]], dtype=np.float64) / (scale* 2))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_k:
                pass
            if event.key == pg.K_l:
                player = world.getPlayer()
                player.noClip = not player.noClip
    
    screen.fill((0,0,0))

    fps = clock.get_fps()
    deltaTime = 1 / 60#(fps if fps != 0 else 60)

    world.tick(deltaTime)
    camera.tick(deltaTime)
    world.render(camera, scale)

    pg.display.flip()
    clock.tick(60)