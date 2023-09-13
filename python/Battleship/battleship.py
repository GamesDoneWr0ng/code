import numpy as np
import pygame as pg
pg.init()

class Battleship:
    def __init__(self, size = 600):
        self.size      = (size, size)
        self.screen    = pg.display.set_mode(self.size)
        self.cellSize  = size // 10
        self.ships     = np.zeros((2, 10,10))
        self.shots     = np.zeros((2, 10,10))
        self.placeShip = np.zeros((10,10))
        self.started   = False
        self.player    = 0
        self.startup   = self.startGame()
        self.swapTimer = 0

    def startGame(self):
        for player in range(2):
            self.player = player
            for i in range(2,6):
                self.placeShip[0][0:i] = 1
                while np.sum(self.placeShip) != 0:
                    yield 
            self.swapTimer = 90

        self.started = True

    def editShip(self, input):
        if input == "up":
            if np.sum(self.placeShip[:,0]) == 0:
                self.placeShip = np.roll(self.placeShip, -1, axis=1)
        elif input == "down":
            if np.sum(self.placeShip[:,9]) == 0:
                self.placeShip = np.roll(self.placeShip, 1, axis=1)
        elif input == "left":
            if np.sum(self.placeShip[0]) == 0:
                self.placeShip = np.roll(self.placeShip, -1, axis=0)
        elif input == "right":
            if np.sum(self.placeShip[9]) == 0:
                self.placeShip = np.roll(self.placeShip, 1, axis=0)
        elif input == "rotateClockwise":
            self.placeShip = np.rot90(self.placeShip, -1)
        elif input == "rotateCounterClockwise":
            self.placeShip = np.rot90(self.placeShip, 1)
        elif input == "place":
            if np.sum(self.placeShip[self.ships[self.player] == 1]) == 0:
                self.ships[self.player] += self.placeShip
                self.placeShip = np.zeros((10,10))
        for i in self.startup:
            return i
        
    def shoot(self, pos):
        if self.swapTimer > 0 or self.shots[self.player][pos[0]][pos[1]] == 1:
            return True
        self.shots[self.player][pos[0]][pos[1]] = 1
        self.swapTimer = 90

        if np.all(self.shots[self.player][self.ships[int(not self.player)] == 1] == 1):
            return False

        self.player = int(not self.player)
        return True

    def draw(self):
        self.screen.fill((255,255,255))
        self.swapTimer -= 1
        player = self.player if self.swapTimer < 0 else int(not self.player)
        for i in range(1,10):
            pg.draw.line(self.screen, (0,0,0), (i*self.cellSize, 0), (i*self.cellSize, self.size[0]))
            pg.draw.line(self.screen, (0,0,0), (0, i*self.cellSize), (self.size[0], i*self.cellSize))
        if self.started == False:
            for j in range(10):
                for k in range(10):
                    if self.ships[player][j][k]:
                        pg.draw.rect(self.screen, (100,100,100), (j*self.cellSize+1, k*self.cellSize+1, self.cellSize-1, self.cellSize-1))
                    if self.placeShip[j][k] and self.swapTimer < 0:
                        pg.draw.rect(self.screen, (0,255,0), (j*self.cellSize+1, k*self.cellSize+1, self.cellSize-1, self.cellSize-1))
        else:
            #player = int(not player)
            for j in range(10):
                for k in range(10):
                    if self.shots[player][j][k]:
                        pg.draw.line(self.screen, (255,0,0) if self.ships[player][j][k] else (0,0,0), (j*self.cellSize+3, k*self.cellSize+3), ((j+1)*self.cellSize-3, (k+1)*self.cellSize-3))
                        pg.draw.line(self.screen, (255,0,0) if self.ships[player][j][k] else (0,0,0), ((j+1)*self.cellSize-3, k*self.cellSize+3), (j*self.cellSize+3, (k+1)*self.cellSize-3))

        pg.display.flip()