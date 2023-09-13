import pygame as pg
from battleship import Battleship
import numpy as np

clock = pg.time.Clock()

class Main:
    def __init__(self):
        self.running = True
        self.game = Battleship()
        self.mainLoop()

    def inputHandler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if self.game.started:
                # fire with mouse
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = np.array(pg.mouse.get_pos()) // self.game.cellSize
                        self.running = self.game.shoot(pos)
            else:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.game.editShip("place")
                    elif event.key == pg.K_UP:
                        self.game.editShip("up")
                    elif event.key == pg.K_DOWN:
                        self.game.editShip("down")
                    elif event.key == pg.K_LEFT:
                        self.game.editShip("left")
                    elif event.key == pg.K_RIGHT:
                        self.game.editShip("right")
                    elif event.key == pg.K_RSHIFT:
                        self.game.editShip("rotateClockwise")
                    elif event.key == pg.K_MINUS:
                        self.game.editShip("rotateCounterClockwise")

    def mainLoop(self):
        while self.running:
            clock.tick(60)
            self.inputHandler()
            self.game.draw()

main = Main()