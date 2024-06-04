import numpy as np
import pygame as pg
import os
from itertools import product
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()

fps = 150

#pattern = np.random.choice(["R","L"], 256)
#pattern[0] = "L" if pattern[0] == "N" else pattern[0]
pattern = "LRLRLRLR"
R = np.array([[0, -1], [1, 0]])
L = np.array([[0, 1], [-1, 0]])
U = -1
N = 1

#colors = [(i,i,i) for i in range(256)] # 256 colors
#colors = list(product([0,255//3,2*255//3,255], [0,255//3,2*255//3,255], [0,255//3,2*255//3,255])) # 64 colors
#colors = list(product([0,255,255], [0,127,255], [0,127,255])) # 27 colors
colors = list(product([0,255], [0,255], [0,255])) # 8 colors
#colors = [(0,0,0), (255,255,255)]

class Ant:
    def __init__(self, pattern, pos, dir) -> None:
        self.pos: np.ndarray = pos
        self.direction = dir

        self.directions = []
        for i in pattern:
            match i:
                case "R":
                    self.directions.append(R)
                case "L":
                    self.directions.append(L)
                case "N":
                    self.directions.append(N)
                case "U":
                    self.directions.append(U)
                case _:
                    print("Invalid pattern")
                    exit()

    def tick(self, cells):
        cell = cells[self.pos[0], self.pos[1]]
        # rotation matrix
        self.direction = np.dot(self.direction, self.directions[cell])
        #cell = (cell + 1) % len(pattern)

        #pg.draw.rect(screen, colors[cell], (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))
        #screen.set_at(self.pos + np.array((270,0)), colors[cell])
        self.lastPos = self.pos.copy()

        #cells[self.pos[0]][self.pos[1]] = cell
        self.pos += self.direction
        self.pos = self.pos % cells.shape
        #screen.set_at(self.pos + np.array((270,0)), colors[cell])
#        pg.draw.rect(screen, colors[cell], (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))

    def updateColor(self, cells, colors, screen, pattern):
        cell = (cells[self.lastPos[0], self.lastPos[1]] + 1) % len(pattern)
        cells[self.lastPos[0], self.lastPos[1]] = cell
        screen.set_at(self.lastPos + np.array((270,0)), colors[cell])


info = pg.display.Info() # You have to call this before pygame.display.set_mode()
size = width, height = info.current_w,info.current_h

font = pg.font.SysFont("Arial", 30)

screen = pg.display.set_mode(size, pg.FULLSCREEN)
screen.fill((0,0,0))
clock = pg.time.Clock()
pg.display.set_caption("Langtons maur")

cellSize = 1
#cells = np.zeros([width // cellSize, height // cellSize], dtype=np.int8)
cells = np.zeros([900, 900], dtype=np.int8)
skip = 0

ants = []
for i in range(81):
    ants.append(Ant(pattern, (np.array((0,-5)) + 100*np.array((i//9, i%9)) +50), np.array([0, 1])))
    ants.append(Ant(pattern, (np.array((5,0))  + 100*np.array((i//9, i%9)) +50), np.array([-1, 0])))
    ants.append(Ant(pattern, (np.array((0,5))  + 100*np.array((i//9, i%9)) +50), np.array([0, -1])))
    ants.append(Ant(pattern, (np.array((-5,0)) + 100*np.array((i//9, i%9)) +50), np.array([1, 0])))
mod = fps // 60

physicstick = 0
running = True
while running:
    #clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                fps *= 1.25
                mod = fps // 60
            elif event.key == pg.K_DOWN:
                fps *= 0.8
                mod = fps // 60

    for ant in ants:
        ant.tick(cells)
    for ant in ants:
        ant.updateColor(cells, colors, screen, pattern)

    skip = (skip + 1) % mod
    if skip == 0:
        pg.display.flip()
        clock.tick(60)

        text = font.render(f"FPS: {clock.get_fps()*mod:.2f}, {clock.get_fps():.2f}", True, (255, 0, 0))
        pg.draw.rect(screen, (0, 0, 0), (0, 0, text.get_width(), text.get_height()))
        screen.blit(text, (0, 0))