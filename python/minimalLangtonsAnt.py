import pygame as pg

gridSize = (100,100)
cellSize = 5

screen = pg.display.set_mode((gridSize[0] * cellSize, gridSize[1] * cellSize))
screen.fill((0, 0, 0))

clock = pg.time.Clock()

grid = [[0 for x in range(gridSize[0])] for y in range(gridSize[1])]

antPos = gridSize[0] // 2, gridSize[1] // 2
antDir = 0

running = True
while running:
    # quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # rotate based on color
    if grid[antPos[1]][antPos[0]] == 0:
        grid[antPos[1]][antPos[0]] = 1
        antDir = (antDir + 1) % 4
    else:
        grid[antPos[1]][antPos[0]] = 0
        antDir = (antDir - 1) % 4

    # change the color
    pg.draw.rect(screen, (255, 255, 255) if grid[antPos[1]][antPos[0]] == 1 else (0,0,0), (antPos[0] * cellSize, antPos[1] * cellSize, cellSize, cellSize))

    # move the ant
    if antDir == 0:
        antPos = (antPos[0] + 1) % gridSize[0], antPos[1]
    elif antDir == 1:
        antPos = antPos[0], (antPos[1] + 1) % gridSize[1]
    elif antDir == 2:
        antPos = (antPos[0] - 1) % gridSize[0], antPos[1]
    elif antDir == 3:
        antPos = antPos[0], (antPos[1] - 1) % gridSize[1]

    pg.draw.rect(screen, (255, 0, 0), (antPos[0] * cellSize, antPos[1] * cellSize, cellSize, cellSize))
    
    pg.display.flip()
    #clock.tick(10)