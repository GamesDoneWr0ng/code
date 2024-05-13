import numpy as np
from apple import Apple
from player import Player
import pygame as pg
pg.init()

SIZE = WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()
font = pg.font.SysFont("Arial", 30)
f = open("/Users/askborgen/Desktop/code/python/terminprøve24vår/eplesankning/apples.csv").read().split("\n")

points = 0

def collision(apples, player):
    newApples = []
    points = 0

    for apple in apples:
        if apple.pos[1] - apple.size > HEIGHT:
            continue

        if player.pos[0] + player.width <  apple.pos[0] -  apple.size  or \
            apple.pos[0] + apple.size   < player.pos[0] - player.width or \
            apple.pos[1] + apple.size   < player.pos[1] - player.width:

            # No collition
            newApples.append(apple)
            continue

        if player.pos[0] < apple.pos[0] and apple.pos[0] < player.pos[0] + player.width:
            points += 1 if apple.color == player.color else -1
            continue

        if player.pos[0] > apple.pos[0]:
            # Get y value of circle at x = player.pos[0]
            y = -np.sin(np.arccos((player.pos[0] - apple.pos[0]) / apple.size)) * apple.size
        else:
            # x = player.pos[0] + player.width
            y = -np.sin(np.arccos((player.pos[0] + player.width - apple.pos[0]) / apple.size)) * apple.size
        
        if y > player.pos[1] - player.width:
            points += 1 if apple.color == player.color else -1
            continue
        if y > player.pos[1] - player.width:
            points += 1 if apple.color == player.color else -1
            continue


        newApples.append(apple)

    return newApples, points

player = Player(screen, np.array([WIDTH // 2, HEIGHT]), 6, 3, 50)
apples = []

while clock.get_fps() == 0:
    clock.tick(60)

n = 1
t = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("#000000")

    # add apples
    if n < len(f):
        line = f[n].split(";")
        if len(line) != 5:
            running = False
            break
        
        if float(line[0]) < t:
            apples.append(Apple(screen, int(line[1]), int(line[2]), int(line[3]), line[4]))
            n += 1
            continue
    elif len(apples) == 0:
        running = False
        print(f"No more apples. Points collected: {points}")
        break

    # update and draw
    player.update()
    player.draw()

    for apple in apples:
        apple.update()
        apple.draw()

    # colliton
    apples, p = collision(apples, player)
    points += p

    # draw points
    text = font.render(f"Points: {points}", True, "#FFFFFF")
    screen.blit(text, (10, 10))

    # update screen n stuff
    pg.display.flip()
    clock.tick(60)
    t += 1/clock.get_fps() if clock.get_fps() != 0 else 60