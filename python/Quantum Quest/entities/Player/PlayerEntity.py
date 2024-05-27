from entities.Entity import Entity
from entities import EntityType, MovementType
from entities.Player.Input import Input
from util.math.Calc import approach
from util.StateMachine import StateMachine
import pygame as pg
import numpy as np

class PlayerEntity(Entity):
    def __init__(self, room):
        super(PlayerEntity, self).__init__(EntityType.PLAYER, room)

        self.input = Input()

        # region constants
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
        self.jumpSpeed = -15
        self.dashCooldownTime = 0.2
        self.dashRefillCooldownTime = 0.1
        self.dashSpeed = 30
        self.endDashSpeed = 20
        self.endDashUpMult = 0.75
        self.dashTime = 0.15
        self.maxDashes = 1
        self.superJumpX = 32.5
        self.duckSuperJumpXMult = 1.25
        self.duckSuperJumpYMult = 0.5  

        self.stateNormal = 0
        self.statePhotonDash = 1

        # endregion

        # region vars
        self.currentMaxFall = 0
        self.jumpGraceTimer = self.jumpGraceTime
        self.dashCooldownTimer = self.dashCooldownTime
        self.dashRefillCooldownTimer = self.dashRefillCooldownTime
        self.startedDashing = False
        self.dashes = 1
        self.facing = 1
    
        # endregion
        
        self.stateMachine = StateMachine(0) # TODO: initialize to correct state from savefile
        self.stateMachine.addState(self.updateNormal, None, None, None)
        self.stateMachine.addState(self.updatePhotonDash, self.coroutinePhotonDash, self.startPhotonDash, self.endPhotonDash)

    def isPlayer(self) -> bool:
        return True
    
    def tick(self):
        self.input.update(self.getDeltaTime())
        #self.checkOnGround()

        if self.input.moveX != 0:
            self.facing = self.input.moveX.val

        # timers
        # jump
        if self.jumpGraceTimer > 0:
            self.jumpGraceTimer -= self.getDeltaTime()
        if self.onGround:
            self.jumpGraceTimer = self.jumpGraceTime

        # dashes
        if self.dashCooldownTimer > 0:
            self.dashCooldownTimer -= self.getDeltaTime()        
        if self.dashRefillCooldownTimer > 0:
            self.dashRefillCooldownTimer -= self.getDeltaTime()
        if self.onGround and self.dashRefillCooldownTimer <= 0:
            self.dashes = self.maxDashes

        super().tick()

    def tickMovement(self) -> None:
        self.stateMachine.update()

    # region state normal
    def updateNormal(self) -> int:
        if self.canDash():
            return self.statePhotonDash

        # Walk and friction
        if self.isOnGround():
            mult = 1
            self.setVelocityY(min(0, self.getVelocity()[1]))
        else: 
            mult = self.airMult

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
            mult = 0.5 if self.getVelocity()[1] < self.halfGravThreshold and self.input.jump.pressed else 1

            self.setVelocityY(approach(self.getVelocity()[1], self.currentMaxFall, self.gravity * mult * self.getDeltaTime()))

        # Jumping
        if self.input.jump:
            if self.jumpGraceTimer > 0:
                self.jump()

        self.move(MovementType.PLAYER, self.getVelocity() * self.getDeltaTime())

        return self.stateNormal
    
    # endregion

    # region state photon dash
    def callDashEvents(self):
        if not self.calledDashEvents:
            self.calledDashEvents = True
            # TODO: dash events
        pass

    def startPhotonDash(self):
        self.dashDir = np.array((self.input.moveX.val, self.input.moveY.val), dtype=np.float32)
        if np.all(self.dashDir == 0):
            self.dashDir = np.array([self.facing, 0], dtype=np.float32)

        self.beforeDashSpeed = self.getVelocity()
        self.setVelocity(np.zeros(2))
        self.dashes -= 1

        self.calledDashEvents = False
        self.dashStartedOnGround = self.onGround
        self.dashCooldownTimer = self.dashCooldownTime
        self.dashRefillCooldownTimer = self.dashRefillCooldownTime
        self.startedDashing = True

    def endPhotonDash(self):
        self.stateMachine.resetCoroutine()

    def updatePhotonDash(self):
        # TODO: super grab n jump n shit
        if self.dashDir[1] >= 0 and self.dashDir[0] != 0 and self.input.jump and self.jumpGraceTimer > 0:
            self.superJump(self.dashDir[1] > 0)
            return self.stateNormal

        self.move(MovementType.PLAYER, self.getVelocity() * self.getDeltaTime())
        return self.statePhotonDash

    def coroutinePhotonDash(self):
        newSpeed = self.dashDir * self.dashSpeed
        if np.sign(self.beforeDashSpeed[0]) == np.sign(newSpeed[0]) and np.abs(self.beforeDashSpeed[0]) > np.abs(newSpeed[0]):
            newSpeed[0] = self.beforeDashSpeed[0]
        self.setVelocity(newSpeed)

        self.callDashEvents()

        yield self.dashTime
        
        if self.dashDir[1] <= 0:
            self.setVelocity(self.dashDir * self.endDashSpeed)
        if self.getVelocity()[1] < 0:
            self.setVelocityY(self.getVelocity()[1] * self.endDashUpMult)

        self.stateMachine.state = self.stateNormal

    def canDash(self):
        return self.input.photonDash and self.dashCooldownTimer <= 0 and self.dashes > 0


    # endregion
    
    # region jumps
    def jump(self) -> None:
        self.jumpGraceTimer = 0
        self.input.jump.consumeBuffer()

        self.setVelocityX(self.getVelocity()[0] + self.input.moveX * self.jumpXBoost)
        self.setVelocityY(self.jumpSpeed)

        # TODO: sound particles

    def superJump(self, d) -> None:
        if self.dashRefillCooldownTimer <= 0:
            self.dashes = self.maxDashes
        self.jumpGraceTimer = 0
        self.input.jump.consumeBuffer()

        self.setVelocityX(self.superJumpX * self.facing)
        self.setVelocityY(self.jumpSpeed)

        if d: #TODO: if ducking
            self.setVelocityX(self.getVelocity()[0] * self.duckSuperJumpXMult)
            self.setVelocityY(self.getVelocity()[1] * self.duckSuperJumpYMult)

        # TODO: sfx, particals

    # endregion

    def render(self, screen, camera, scale: float):
        if not super().render(screen, camera, scale):
            return
        pg.draw.polygon(screen, (255,255,255) if self.dashes != 0 else (255,255,0), (self.getHitbox().getPoints()-camera.topLeft())*scale)