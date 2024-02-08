import numpy as np
import pygame as pg
import os
from itertools import product
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()

pattern = np.random.choice(["R","L"], 256)
pattern[0] = "L" if pattern[0] == "N" else pattern[0]
#pattern = "RUUUNRRULRRNRRLRLNUNURLNLRNLUNRURLRLRRUNUNNLULRRNUNRLRURNNNUUNNLURULNUURULRLRLNRNRLNRRRLNNRLNNULUNRRURRLUNLRRNNUULNLLRRNLRRULRLUNLURUNNNNNNRNRRRULLNNURUURUNRLNUUNLLNRNURRULULRRULLULLRUNNRNNNLNUNURRURULLRNRRUUNUNLLUURLNRNNRURRRLRULUUURRRNNNNULRLLURULLURRNNL"
R = np.array([[0, -1], [1, 0]])
L = np.array([[0, 1], [-1, 0]])
U = -1
N = 1

directions = []
for i in pattern:
    match i:
        case "R":
            directions.append(R)
        case "L":
            directions.append(L)
        case "N":
            directions.append(N)
        case "U":
            directions.append(U)
        case _:
            print("Invalid pattern")
            exit()

colors = [(i,i,i) for i in range(256)] # 256 colors
#colors = list(product([0,255//3,2*255//3,255], [0,255//3,2*255//3,255], [0,255//3,2*255//3,255])) # 64 colors
#colors = list(product([0,255,255], [0,127,255], [0,127,255])) # 27 colors
#colors = list(product([0,255], [0,255], [0,255])) # 8 colors 

fps = 1
info = pg.display.Info() # You have to call this before pygame.display.set_mode()
size = width, height = info.current_w,info.current_h

screen = pg.display.set_mode(size, pg.FULLSCREEN)
screen.fill((0,0,0))
clock = pg.time.Clock()
pg.display.set_caption("Langtons maur")

cellSize = 1

cells = np.zeros([width // cellSize, height // cellSize], dtype=np.int8)

pos = (np.array(cells.shape) // 2)
direction = np.array([0, 1])

skip = 0

physicstick = 0
running = True
while running:
    #clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                fps += 1
            elif event.key == pg.K_DOWN:
                fps -= 1
            elif event.key == pg.K_SPACE:
                fps = 60

    #physicstick = (physicstick + fps) % 60

    #if physicstick < fps:
    cell = cells[pos[0]][pos[1]]
    # rotation matrix
    direction = np.dot(direction, directions[cell])
    cell = (cell + 1) % len(pattern)

    #pg.draw.rect(screen, colors[cell], (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))
    screen.set_at(pos, colors[cell])

    cells[pos[0]][pos[1]] = cell
    pos += direction
    screen.set_at(pos, colors[cell])
#    pg.draw.rect(screen, colors[cell], (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))

    skip = (skip + 1) % 1500
    if skip == 0:
        pg.display.flip()