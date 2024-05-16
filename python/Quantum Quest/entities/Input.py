from ast import In
from numpy import inf
import pygame as pg

# TODO: config file
controls = {
    "up": pg.K_w,
    "down": pg.K_s,
    "left": pg.K_a,
    "right": pg.K_d,
    "jump": pg.K_SPACE
}

class BasicInput:
    def __init__(self, key) -> None:
        self.key = key
        self.pressed = False

    def update(self, keys) -> None:
        if keys[self.key]:
            self.pressed = True
        else:
            self.pressed = False
            
class Input1D:
    def __init__(self, keyDown, keyUp) -> None:
        self.keyDown = keyDown
        self.keyUp = keyUp
        self.val: float = 0

    def update(self, keys) -> None:
        self.val = 0
        if keys[self.keyDown]:
            self.val -= 1
        if keys[self.keyUp]:
            self.val += 1

    # comparasons == != < <= > >=
    def __eq__(self, __value) -> bool: return self.val == __value
    def __ne__(self, __value) -> bool: return self.val != __value
    def __lt__(self, __value) -> bool: return self.val <  __value
    def __le__(self, __value) -> bool: return self.val <= __value
    def __gt__(self, __value) -> bool: return self.val >  __value
    def __ge__(self, __value) -> bool: return self.val >= __value

    def __mul__(self, __value) -> float: return self.val * __value

class BufferedInput(BasicInput):
    def __init__(self, key) -> None:
        super().__init__(key)
        self.lastPressed = inf

    def update(self, keys, deltaTime) -> None:
        wasPressed = self.pressed
        super().update(keys)
        if self.pressed and not wasPressed:
            self.lastPressed = 0
        else:
            self.lastPressed += deltaTime


class Input:
    def __init__(self) -> None:
        self.moveX = Input1D(controls["left"], controls["right"])
        self.moveY = Input1D(controls["up"], controls["down"])
        self.jump  = BufferedInput(controls["jump"])
    
    def update(self, deltaTime: float) -> None:
        keys = pg.key.get_pressed()
        
        self.moveX.update(keys)
        self.moveY.update(keys)
        self.jump.update(keys, deltaTime)