from entities import EntityType, MovementType, RemovalReason
from util.math.Hitbox import Hitbox
from world.Camera import Camera
import numpy as np

class Entity:
    def __init__(self, type: EntityType.EntityType, room) -> None:
        self.type: EntityType.EntityType = type.copy()
        self.hitbox = self.type.getHitbox() if self.type.hasHitbox() else None
        self.room = room
        self.id: int = room.nextId()
        self.velocity: np.ndarray = np.zeros(2)
        self.position: np.ndarray = self.hitbox.getPosition() if self.hasHitbox() else None
        self.onGround: bool = False
        self.gravity: float = self.type.getGravity()
        self.noClip: bool = False

    def __eq__(self, other) -> bool:
        return self.getId() == other.getId()

    def getHitbox(self) -> Hitbox:
        return self.hitbox
    
    def hasHitbox(self):
        return not self.hitbox == None

    def remove(self, reason: RemovalReason.RemovalReason) -> None:
        self.onRemoved()

    def onRemoved(self) -> None:
        pass

    def kill(self) -> None:
        self.remove(RemovalReason.KILLED)
        self.emitGameEvent("entity.kill") # TODO event

    def emitGameEvent(self, event) -> None:
        self.room.emitGameEvent(self, event, self.position)

    def recieveGameEvent(self, event) -> None:
        pass
    
    def isPlayer(self) -> bool:
        return False
    
    def getId(self) -> int:
        return self.id
    
    def setId(self, id: int) -> None:
        self.id = id

    def getType(self) -> EntityType.EntityType:
        return self.type

    def getPosition(self) -> np.ndarray:
        return self.position
    
    def setPosition(self, position: np.ndarray):
        self.position = position
        if self.hasHitbox():
            self.getHitbox().setPosition(position)

    def getVelocity(self) -> np.ndarray:
        return self.velocity
    
    def setVelocity(self, velocity: np.ndarray) -> None:
        self.velocity = velocity

    def setVelocityX(self, velocity: float) -> None:
        self.velocity[0] = velocity

    def setVelocityY(self, velocity: float) -> None:
        self.velocity[1] = velocity

    def setState(self, state): # TODO animation state
        pass

    def tick(self) -> None:
        self.tickMovement()

    def tickMovement(self) -> None:
#        self.checkOnGround()

#        if not self.isOnGround():
#            self.setVelocity(self.getVelocity() + np.array([0, self.gravity * self.getDeltaTime()]))

        self.move(MovementType.SELF, self.getVelocity() * self.getDeltaTime())

    def move(self, movementType: MovementType.MovementType, movement: np.ndarray) -> None:
        if self.noClip or not self.hasHitbox(): # TODO: movement
            self.setPosition(self.getPosition() + movement)
            return
        
        movement = self.adjustMovementForWorldCollisions(movement)
        
        if np.sum(movement**2) < 1E-7:
            return
        
        self.setPosition(self.getPosition() + movement)
    
    def adjustMovementForWorldCollisions(self, movement: np.ndarray) -> np.ndarray:
        if np.sum(movement**2) > 1E-4:
            hitbox = self.getHitbox().stretch(movement)
        else:
            hitbox = self.getHitbox()

        for object in self.room.objects:
            collision, correction, axis = hitbox.checkCollision(object.getHitbox())
            if collision:
                movement += correction
                # axes are normalized so we can check the first element
                if np.abs(axis)[1] > self.type.getMaxSlope():
                    self.setOnGround(True)

                #self.setVelocity(self.getVelocity()*axis[::-1])

        return movement
        
    def render(self, screen, camera: Camera, scale: float):
        return self.getType().getHitbox().touches(camera.getHardBorder())
    
    def setOnGround(self, onGround: bool):
        self.onGround = onGround

    def isOnGround(self) -> bool:
        return self.onGround
    
    def setNoClip(self, noClip: bool):
        self.noClip = noClip
    
    def checkOnGround(self):
        if self.gravity == 0:
            self.setOnGround(True)
            return
        if self.getVelocity()[1] < 0:
            self.setOnGround(False)
            return
        hitbox = self.getHitbox().stretch(np.array([0, self.gravity * self.getDeltaTime()]))
        for object in self.room.objects:
            collision, _, _ = hitbox.checkCollision(object.getHitbox())
            if collision:
                self.setOnGround(True)
                return
        self.setOnGround(False)

    def getDeltaTime(self) -> float:
        return self.room.getDeltaTime()