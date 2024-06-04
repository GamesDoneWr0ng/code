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
    
    return new_grid

def draw(grid, screenSize = screenSize, cellSize = cellSize):
    # Create a surface to hold the grid image
    gridSurface = pg.Surface(screenSize)
    gridSurface.fill((0, 0, 0))

    # Draw each alive cell onto the grid surface
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 1:
                #pg.draw.rect(gridSurface, (255, 255, 255), (i * cellSize, j * cellSize, cellSize, cellSize))
                gridSurface.set_at((i,j), (255, 255, 255))

    # Blit the grid surface onto the screen
    screen.blit(gridSurface, (0, 0))
    pg.display.flip()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:    
                grid = update(grid)
                draw(grid)
            if event.key == pg.K_g:
                grid = np.random.randint(0, 2, gridSize)
                draw(grid)
            if event.key == pg.K_UP:
                fps += 1
                text = font.render(f"FPS: {fps}", True, (255, 255, 255))
                screen.blit(text, (0, 0))
                pg.display.flip()
            if event.key == pg.K_DOWN:
                fps -= 1
                text = font.render(f"FPS: {fps}", True, (255, 255, 255))
                screen.blit(text, (0, 0))
                pg.display.flip()

        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            pos = [pos[0]//cellSize, pos[1]//cellSize]
            grid[pos[0], pos[1]] = not grid[pos[0], pos[1]]
            draw(grid)

        keys = pg.key.get_pressed()
        if keys[pg.K_b]:
            for _ in range(fps):
                grid = update(grid)
            draw(grid)