import numpy as np
from ..Camera import Camera
from util.math.Hitbox import Hitbox
from world.objects.Trigger import Trigger
import pygame as pg

class Transition(Trigger):
    def __init__(self, hitbox: Hitbox, room, connected: str, direction: np.ndarray, hasCollision: bool = True) -> None:
        super().__init__(hitbox, room, hasCollision)
        self.connected = connected
        self.direction = direction

    def onExit(self, entity):
        if np.dot(entity.getVelocity(), self.direction) > 0:
            self.room.world.move(self.room.getId(), self.connected, entity)
    
    def render(self, screen, camera: Camera, scale: float): # TODO: delete 
        if not super().render(screen, camera, scale):
            return
        pg.draw.polygon(screen, (0,0,255), (self.getHitbox().getPoints()-camera.topLeft())*scale)