if __name__ != "__main__":
    raise ImportError("This file is not meant to be imported")

from world.World import World
from world.Camera import Camera
from entities.PlayerEntity import PlayerEntity
from entities.TempEntity import TempEntity
from world.objects.Playform import Platform
from world.objects.Transition import Transition
from util.math.Hitbox import Polygon
import numpy as np
import pygame as pg
pg.init()

SIZE = WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()
scale = 16

world = World(screen)

world.rooms["start"].addEntity(PlayerEntity(world.rooms["start"]))
world.rooms["start"].addEntity(TempEntity(world.rooms["start"]))
world.rooms["start"].entities[1].setPosition(np.array([1,1], dtype=np.float64))
world.rooms["start"].addObject(Platform(Polygon(np.array([[-5, 3], [-5, 4], [11, 4], [11, 3]])), world.rooms["start"]))
world.rooms["start"].addObject(Platform(Polygon(np.array([[-5, -1], [-5, -2], [5, -2], [5, -1]])+1), world.rooms["start"]))

world.rooms["left"].addObject(Platform(Polygon(np.array([[8, 3], [8, 4], [21, 4], [21, 3]])), world.rooms["left"]))

world.rooms["start"].addObject(Transition(Polygon(np.array([[9, 1], [9, 3], [10, 3], [10, 1]])), world.rooms["start"], "left", np.array([1,0])))
world.rooms["left"].addObject(Transition(Polygon(np.array([[9, 1], [9, 3], [10, 3], [10, 1]])), world.rooms["left"], "start", np.array([-1,0])))


camera = Camera(scale, world.getPlayer(), 
                np.array([[-WIDTH, -HEIGHT], [WIDTH, HEIGHT]], dtype=np.float64) / (scale* 4), 
                np.array([[-WIDTH, -HEIGHT], [WIDTH, HEIGHT]], dtype=np.float64) / (scale*2))

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