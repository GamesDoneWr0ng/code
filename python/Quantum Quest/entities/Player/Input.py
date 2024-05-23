from numpy import inf
import pygame as pg

# TODO: config file
controls = {
    "up": pg.K_e,
    "down": pg.K_d,
    "left": pg.K_s,
    "right": pg.K_f,
    "jump": pg.K_k,
    "photonDash": pg.K_l
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

    def __bool__(self) -> bool:
        return self.pressed
            
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
    def __bool__(self) -> bool: return self.val != 0

    def __mul__(self, __value) -> float: return self.val * __value

class BufferedInput(BasicInput):
    def __init__(self, key) -> None:
        super().__init__(key)
        self.lastPressed = inf

    def __bool__(self) -> bool:
        return self.lastPressed < 0.1

    def update(self, keys, deltaTime) -> None:
        # detect on keydown
        wasPressed = self.pressed
        super().update(keys)
        if self.pressed and not wasPressed:
            self.lastPressed = 0
        else:
            self.lastPressed += deltaTime

    def consumeBuffer(self) -> None:
        self.lastPressed = inf

class Input:
    def __init__(self) -> None:
        self.moveX      =       Input1D(controls["left"], controls["right"])
        self.moveY      =       Input1D(controls["up"], controls["down"])
        self.jump       = BufferedInput(controls["jump"])
        self.photonDash = BufferedInput(controls["photonDash"])
    
    def update(self, deltaTime: float) -> None:
        keys = pg.key.get_pressed()
        
        self.moveX.update(keys)
        self.moveY.update(keys)
        self.jump.update(keys, deltaTime)
        self.photonDash.update(keys, deltaTime)