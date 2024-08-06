import pygame as pg
import time
pg.init()

SIZE = WIDTH, HEIGHT = 1600, 800
screen = pg.display.set_mode(SIZE)

lastClick = time.time()

sum = 0
lastPos = [0, 0]
lastFrame = False

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    if pg.mouse.get_pressed()[0] and not lastFrame:
        t = time.time() - lastClick
        
        if t == 0:
            break
        
        sum += t
        
        newPos = [lastPos[0] + t * 80, 8/t]
        pg.draw.line(screen, (255, 255, 255), lastPos, newPos)
        lastPos = newPos
        
        if sum > 20:
            screen.fill((0, 0, 0))
            lastPos = [0,0]
            sum = 0
        
        print(t, 1/t)
        lastClick = time.time()
    
    lastFrame = pg.mouse.get_pressed()[0]

    pg.display.flip()