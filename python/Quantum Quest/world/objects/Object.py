from util.math.Hitbox import Hitbox
from world.Camera import Camera
import numpy as np

class Object:
    def __init__(self, hitbox: Hitbox, room, hasCollision: bool = True) -> None:
        self.hitbox: Hitbox = hitbox
        self.position: np.ndarray = self.hitbox.getPosition()
        self.room = room
        self.id: int = room.nextId()
        self._hasCollision: bool = hasCollision

    def hasCollision(self) -> bool:
        return self._hasCollision
    
    def setCollision(self, hasCollision: bool) -> None:
        self._hasCollision = hasCollision

    def getHitbox(self) -> Hitbox:
        return self.hitbox
    
    def getPosition(self) -> np.ndarray:
        return self.position
    
    def setPosition(self, position: np.ndarray) -> None:
        self.position = position

    def isTicking(self) -> bool:
        return False

    def isTrigger(self) -> bool:
        return False
    
    def render(self, screen, camera: Camera, scale: float):
        return self.getHitbox().touches(camera.getHardBorder())