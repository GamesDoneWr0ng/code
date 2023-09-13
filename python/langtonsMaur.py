import numpy as np
import pygame as pg
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()

fps = 1
info = pg.display.Info() # You have to call this before pygame.display.set_mode()
size = width, height = info.current_w,info.current_h

screen = pg.display.set_mode(size, pg.FULLSCREEN)
screen.fill((0,0,0))
clock = pg.time.Clock()
pg.display.set_caption("Langtons maur")

cellSize = 20

cells = np.ones([width // cellSize, height // cellSize], dtype=np.int8)

pos = (np.array(cells.shape) // 2)
direction = np.array([0, 1])

physicstick = 0
running = True
while running:
    clock.tick(60)
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

    physicstick = (physicstick + fps) % 60

    if physicstick < fps:
        cell = cells[pos[0]][pos[1]]
        # rotation matrix
        direction = direction @ (np.array([[0, -1], [1, 0]]) if cell == 1 else np.array([[0, 1], [-1, 0]]))
        cell *= -1

        pg.draw.rect(screen, (0, 0, 0) if cell == 1 else (255, 255, 255), (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))

        cells[pos[0]][pos[1]] = cell
        pos += direction
        pg.draw.rect(screen, (255, 0, 0), (pos[0] * cellSize, pos[1] * cellSize, cellSize, cellSize))

    pg.display.flip()