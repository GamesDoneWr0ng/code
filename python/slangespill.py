import pygame as pg
from functools import lru_cache
import numpy as np
pg.init()
np.set_printoptions(threshold=np.inf)

ladders = {
    1: 38,  # 142857 min
    4: 14,  # 227403
    9: 31,  # 270405
    21: 42, # 357410
    28: 84, # 569048
    36: 44, # 572204
    51: 67, # 402308
    71: 91, # 263411
    80: 100,# 438681
    16: 6,  # 464603
    48: 26, # 712530 max
    49: 11, # 588458
    56: 53, # 307408
    62: 19, # 237485
    64: 60, # 240179
    87: 24, # 481191
    93: 73, # 379077
    95: 75, # 372598
    98: 78  # 224170 
}

frequency = np.zeros(len(ladders))

@lru_cache(maxsize=None)
def step(pos, roll):
    pos += roll
    if pos in ladders:
        return ladders[pos], list(ladders.keys()).index(pos)
    return pos, -1

def bot(steps):
    for i in range(steps):
        pos = 0
        while pos < 100:
            roll = np.random.randint(1, 7)
            pos, f = step(pos, roll)
            if f != -1:
                frequency[f] += 1
        #print("done", i)
#bot(1000000)

#print(frequency)

boardImg = pg.image.load("resources/SlangespillBrett.png")
boardImg = pg.transform.scale(boardImg, (700, 700))
size = boardImg.get_size()
cellSize = size[0] // 10
screen = pg.display.set_mode(size)
pg.display.set_caption("SlangeSpill")
clock = pg.time.Clock()
fps = 60

pos = 0
running = True
while running:
    if pos > 100:
        running = False
        print("Winner")
    clock.tick(fps)
    screen.blit(boardImg, (0, 0))
    x = (pos % 10) * cellSize - cellSize // 2 if pos % 10 else cellSize // 2
    pg.draw.circle(screen, (255, 0, 0), (x if ((pos // 10) % 2 == 0) else size[0] - x, size[1] - ((pos-1) // 10 * cellSize + cellSize // 2)), cellSize // 2 - 15)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                roll = np.random.randint(1, 7)
                pos = step(pos, roll)[0]

    pg.display.flip()