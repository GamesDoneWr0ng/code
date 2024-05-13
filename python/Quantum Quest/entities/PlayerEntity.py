from entities.Entity import Entity
from entities import EntityType, MovementType
from entities.Input import Input
from util.math.Calc import approach
from util.math.Hitbox import Polygon
import pygame as pg
import numpy as np

class PlayerEntity(Entity):
    def __init__(self, room):
        super(PlayerEntity, self).__init__(EntityType.PLAYER, room)

        self.input = Input()

        # constants
        self.maxRun = 90/8
        self.runAccel = 125
        self.runReduce = 50
        self.airMult = 0.65
        self.maxFall = 20
        self.fastMaxFall = 30
        self.maxFallAccel = 300/8
        self.halfGravThreshold = 5
        self.jumpGraceTime = 0.1
        self.jumpXBoost = 5
        self.jumpSpeed = -105/8

        # vars
        self.inputDirection = np.array([0, 0])
        self.currentMaxFall = 0
        self.jumpGraceTimer = 0.1
    
    def isPlayer(self) -> bool:
        return True
    
    def tick(self):
        self.input.update(self.getDeltaTime())
#        self.checkOnGround()

        # timers
        if self.jumpGraceTimer > 0:
            self.jumpGraceTimer -= self.getDeltaTime()
        if self.onGround:
            self.jumpGraceTimer = self.jumpGraceTime

        super().tick()
        #self.move(MovementType.PLAYER, self.getVelocity())

    def tickMovement(self) -> None:

        # Walk and friction
        mult = 1 if self.isOnGround() else self.airMult

        if abs(self.getVelocity()[0] > self.maxRun and self.input.moveX == np.sign(self.getVelocity()[0])):
            # Reduse speed down to maxSpeed
            self.setVelocityX(approach(self.getVelocity()[0], self.input.moveX * self.maxRun, self.runReduce * mult * self.getDeltaTime()))
        else:
            # Accelerate to maxSpeed
            self.setVelocityX(approach(self.getVelocity()[0], self.input.moveX * self.maxRun, self.runAccel * mult * self.getDeltaTime()))

        # Vertical
        # Calculate max fall speed
        mf = self.fastMaxFall if self.input.moveY > 0 else self.maxFall
        self.currentMaxFall = approach(self.currentMaxFall, mf, self.maxFallAccel * self.getDeltaTime())

        # Apply gravity
        if not self.isOnGround():
            mult = 1 if abs(self.getVelocity()[1] < self.halfGravThreshold and self.input.jump == 1) else 0.5

            self.setVelocityY(approach(self.getVelocity()[1], self.currentMaxFall, self.gravity * mult * self.getDeltaTime()))

        # Jumping
        if self.input.jump.pressed:
            if self.jumpGraceTimer > 0:
                self.jump()

        self.move(MovementType.PLAYER, self.getVelocity() * self.getDeltaTime())
    
    def jump(self) -> None:
        self.jumpGraceTimer = 0

        self.setVelocityX(self.getVelocity()[0] + self.jumpXBoost)
        self.setVelocityY(self.jumpSpeed)

        # TODO: sound particles

    def render(self, screen, camera, scale: float):
        if not super().render(screen, camera, scale):
            return
        pg.draw.polygon(screen, (255,255,255), (self.getHitbox().getPoints()-camera.topLeft())*scale)