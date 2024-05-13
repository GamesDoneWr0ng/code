from world.objects.Object import Object
from util.math.Hitbox import Hitbox
import numpy as np
import pygame as pg

class Platform(Object):
    def __init__(self, hitbox: Hitbox, room) -> None:
        super().__init__(hitbox, room)

    def render(self, screen, camera, scale: float):
        if not super().render(screen, camera, scale):
            return
        pg.draw.polygon(screen, (0,255,0), (self.getHitbox().getPoints()-camera.topLeft())*scale)