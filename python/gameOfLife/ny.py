import numpy as np
from scipy.signal import convolve2d
import pygame as pg
pg.init()

fps = 1

cellSize = 1
gridSize = (700,700)
grid = np.zeros(gridSize, dtype=int)

screenSize = (gridSize[0] * cellSize, gridSize[1] * cellSize) 
screen = pg.display.set_mode(screenSize)
clock = pg.time.Clock()
font = pg.font.Font(None, 24)

def update(grid):
    # Define a kernel for convolution that sums up the neighbors
    kernel = np.ones((3, 3), dtype=int)
    kernel[1, 1] = 0
    
    # Use convolution to get the sum of neighbors for each cell
    neighbor_sums = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
    
    # Apply the rules of the game
    birth   = (grid == 0) &  (neighbor_sums == 3)
    survive = (grid == 1) & ((neighbor_sums == 2) | (neighbor_sums == 3))
    
    # Combine birth and survival conditions to form the new grid
    new_grid = np.logical_or(birth, survive).astype(int)
    change = np.logical_xor(grid, new_grid)
    
    return new_grid, change

def draw(grid, change, screen = screen, cellSize = cellSize):
    # Create a surface to hold the grid image

    # Draw each alive cell onto the grid surface
    x,y = np.nonzero(change)
    for i in zip(x,y):
        #pg.draw.rect(gridSurface, (255, 255, 255), (i[0] * cellSize, i[1] * cellSize, cellSize, cellSize))
        screen.set_at(i, (255, 255, 255) if grid[i[0], i[1]] else (0, 0, 0))

    """    # Draw each alive cell onto the grid surfa
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                #pg.draw.rect(gridSurface, (255, 255, 255), (i * cellSize, j * cellSize, cellSize, cellSize))
                gridSurface.set_at((i,j), (255, 255, 255))
    """
    pg.display.flip()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:    
                grid, change = update(grid)
                draw(grid, change)
            if event.key == pg.K_g:
                grid = np.random.randint(0, 2, gridSize)
                draw(grid, np.ones(gridSize))
            if event.key == pg.K_UP:
                draw(grid, np.ones(gridSize))
                fps += 1
                text = font.render(f"FPS: {fps}", True, (255, 255, 255))
                screen.blit(text, (0, 0))
                pg.display.flip()
            if event.key == pg.K_DOWN:
                draw(grid, np.ones(gridSize))
                fps -= 1
                text = font.render(f"FPS: {fps}", True, (255, 255, 255))
                screen.blit(text, (0, 0))
                pg.display.flip()

        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            pos = [pos[0]//cellSize, pos[1]//cellSize]
            grid[pos[0], pos[1]] = not grid[pos[0], pos[1]]
            change = np.zeros(gridSize)
            change[pos[0], pos[1]] = 1
            draw(grid, change)

        keys = pg.key.get_pressed()
        if keys[pg.K_b]:
            change = np.zeros(gridSize)
            for i in range(fps):
                grid, c = update(grid)
                change = np.logical_or(change, c)
            draw(grid, change)
    clock.tick(60)