from cell import Cell
import random
import pygame as pg
pg.init()

class Board:
    def __init__(self, gridSize, cellSize):
        self.gridSize = gridSize
        self.cellSize = cellSize
        size = self.gridSize*self.cellSize
        self.screen = pg.display.set_mode((size, size))

        self.cells = []
        self.generation = 0

        for i in range(self.gridSize):
            rad = []
            for k in range(self.gridSize):
                rad.append(Cell([k, i]))
            self.cells.append(rad)
        
        #self.generate()
        self.draw()
    
    def generate(self):
        for i in self.cells:
            for k in i:
                if random.randint(0,2) == 0:
                    k.active = True
    
    def draw(self):
        self.screen.fill((0,0,0))
        for i in self.cells:
            for k in i:
                if k.active:
                    pg.draw.rect(self.screen, (255,255,255), pg.rect.Rect(k.pos[0]*self.cellSize, k.pos[1]*self.cellSize, self.cellSize, self.cellSize))
        pg.display.flip()

    def getFriends(self, cell):
        pos = cell.pos
        cells = []
        for i in [[-1,-1], [0,-1], [1,-1], [-1,0], [1,0], [-1,1], [0,1], [1,1]]:
            if pos[0] + i[0] < 0 or pos[0] + i[0] > self.gridSize-1 or pos[1] + i[1] < 0 or pos[1] + i[1] > self.gridSize-1:
                continue
            cells.append([pos[0] + i[0], pos[1] + i[1]])
        activeCount = 0
        for i in cells:
            if self.cells[i[1]][i[0]].active:
                activeCount += 1
        return activeCount
    
    def nextGeneration(self):
        switch = []
        for i in self.cells:
            for k in i:
                activeCount = self.getFriends(k)
                if k.active and (activeCount < 2 or activeCount > 3):
                    switch.append(k)
                elif not k.active and activeCount == 3:
                    switch.append(k)
        for i in switch:
            i.active = not i.active
        self.generation += 1
    
    def click(self, pos):
        cell = self.cells[pos[1]][pos[0]]
        cell.active = not cell.active