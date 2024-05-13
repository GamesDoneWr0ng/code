import numpy as np
import pygame as pg
from random import choice

class Apple:
    def __init__(self, screen, pos: int, speed: int, size: int, color: str) -> None:
        self.pos: np.ndarray = np.array([pos, -size], dtype=int)
        self.speed: int = speed
        self.size : int = size
        self.screen = screen
        self.color = color

    def update(self):
        self.pos[1] += self.speed

    def draw(self):
        pg.draw.circle(self.screen, self.color, self.pos, self.size)