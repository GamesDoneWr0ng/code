import pygame as pg
import numpy as np
from itertools import product

class Player:
    def __init__(self, screen, pos: np.ndarray, speed: int, sprintMult: float, width: int) -> None:
        self.screen = screen
        self.pos: np.ndarray = pos
        self.speed: int = speed
        self.sprintMult: float = sprintMult
        self.width: int = width

        self.color = "#00FF00"

        self.pos[0] -= self.width // 2
        self.pos[1] -= self.width

    def update(self) -> None:
        keys = pg.key.get_pressed()
        
        mult = self.sprintMult if keys[pg.K_LSHIFT] else 1
            
        if keys[pg.K_LEFT]:
            self.pos[0] -= self.speed * mult
        if keys[pg.K_RIGHT]:
            self.pos[0] += self.speed * mult

        self.pos[0] = np.clip(self.pos[0], 0, self.screen.get_width() - self.width)

        if keys[pg.K_r]:
            self.color = "#FF0000"
        if keys[pg.K_g]:
            self.color = "#00FF00"

    def draw(self) -> None:
        pg.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.width, self.width))
