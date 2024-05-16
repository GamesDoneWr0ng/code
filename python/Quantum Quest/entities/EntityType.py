from util.math.Hitbox import Hitbox, Polygon, Circle
import numpy as np
from copy import deepcopy

class EntityType:
    def __init__(self, id: str):
        self.id: str = id
        self.hitbox = None
        self.gravity = 0.0
        self.maxSlope = 0.5

    def __eq__(self, other: object) -> bool:
        return self.id == other.id

    def copy(self):
        return deepcopy(self)

    def setHitbox(self, hitbox: Hitbox):
        self.hitbox: Hitbox = hitbox
        return self

    def getHitbox(self):
        return self.hitbox

    def hasHitbox(self):
        return not self.hitbox == None
    
    def setGravity(self, gravity: float):
        self.gravity = gravity
        return self
    
    def getGravity(self):
        return self.gravity
    
    def setMaxSlope(self, slope: float):
        self.maxSlope = slope

    def getMaxSlope(self):
        return self.maxSlope

PLAYER: EntityType = EntityType("player").setHitbox(Polygon(np.array([[0, 0], [1, 0], [1, 2], [0, 2]], dtype=np.float64))).setGravity(900/8)
TEMPENTITY: EntityType = EntityType("temp_entity").setHitbox(Polygon(np.array([[0, 0], [1, 0], [1, 2], [0, 2]], dtype=np.float64)))