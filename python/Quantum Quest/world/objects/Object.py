from util.math.Hitbox import Hitbox
from world.Camera import Camera
import numpy as np

class Object:
    def __init__(self, hitbox: Hitbox, room) -> None:
        self.hitbox: Hitbox = hitbox
        self.position: np.ndarray = self.hitbox.getPosition()
        self.room = room
        self.id: int = room.nextId()

    def getHitbox(self) -> Hitbox:
        return self.hitbox
    
    def getPosition(self) -> np.ndarray:
        return self.position
    
    def setPosition(self, position: np.ndarray) -> None:
        self.position = position

    def isTicking(self) -> bool:
        return False
    
    def render(self, screen, camera: Camera, scale: float):
        return self.getHitbox().touches(camera.getHardBorder())