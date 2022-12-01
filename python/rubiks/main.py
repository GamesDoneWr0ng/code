from cube import Cube
from draw import Draw
from solver import Solver

import copy
from random import choice, randint
from time import sleep
import pygame as pg
pg.init()

cube = Cube()
draw = Draw()
solver = Solver()

todo = []
timer = 10

running = True
while running:
    dir = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
            break
        
        keys = pg.key.get_pressed()

        if event.type == pg.KEYDOWN:
            if keys[pg.K_LSHIFT]:
                dir = 2
            if keys[pg.K_2]:
                dir = 1

            if keys[pg.K_r]:
                cube.rotate("r", dir)
            if keys[pg.K_l]:
                cube.rotate("l", dir)
            if keys[pg.K_u]:
                cube.rotate("u", dir)
            if keys[pg.K_d]:
                cube.rotate("d", dir)
            if keys[pg.K_f]:
                cube.rotate("f", dir)
            if keys[pg.K_b]:
                cube.rotate("b", dir)
            
            if keys[pg.K_x]:
                cube.rotate("x", dir)
            if keys[pg.K_y]:
                cube.rotate("y", dir)
            if keys[pg.K_z]:
                cube.rotate("z", dir)

            if keys[pg.K_7] and len(todo) == 0:
                todo = solver.phase_1(copy.deepcopy(cube.pieces))
            elif keys[pg.K_8] and len(todo) == 0:
                todo = solver.phase_2(copy.deepcopy(cube.pieces))
        
        if keys[pg.K_s]:
            move = choice(["r", "l", "u", "d", "f", "b"])
            dir = randint(0,2)
            cube.rotate(move, dir)

        if keys[pg.K_q]:
            draw.rotate("q")
        if keys[pg.K_a]:
            draw.rotate("a")
        
        movment = pg.mouse.get_rel()
        if pg.mouse.get_pressed()[0]:
            draw.rotate(movment)
            
    if not pg.mouse.get_pressed()[0]:
        draw.reset()
    
    if len(todo) != 0:
        if timer == 0:
            move = todo.pop(0)
            cube.rotate(move[0], move[1])
            timer = 10
        else:
            timer -= 1

    draw.draw(cube.pieces)