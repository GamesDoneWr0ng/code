GRIDSIZE = 24
CELLSIZE = 30

from board import Board
from math import floor
import pygame as pg
pg.init()

class Main:
    def __init__(self, gridSize, cellSize):
        self.board = Board(gridSize, cellSize)

main = Main(GRIDSIZE, CELLSIZE)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                main.board.nextGeneration()
            if event.key == pg.K_g:
                main.board.generate()
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            pos = [floor(pos[0]/CELLSIZE), floor(pos[1]/CELLSIZE)]
            main.board.click(pos)
    keys=pg.key.get_pressed()
    if keys[pg.K_b]:
        main.board.nextGeneration()
    main.board.draw()