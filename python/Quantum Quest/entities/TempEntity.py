from entities.Entity import Entity
from entities import EntityType, MovementType
import pygame as pg
import numpy as np

class TempEntity(Entity):
    def __init__(self, room):
        super(TempEntity, self).__init__(EntityType.TEMPENTITY, room)

    def render(self, screen, camera, scale: float):
        if not super().render(screen, camera, scale):
            return
        pg.draw.polygon(screen, (255,0,0), (self.getHitbox().getPoints()-camera.topLeft())*scale)