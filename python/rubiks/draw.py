import pygame as pg
import numpy as np
from itertools import product
from math import sin,cos
pg.init()

WINDOW_SIZE =  800
ROTATE_SPEED = 0.02
SCALE = 100
window = pg.display.set_mode( (WINDOW_SIZE, WINDOW_SIZE) )
clock = pg.time.Clock()

#red and orange swaped to fix visual bug, probably no other effect
COLORS = {
    "r": (255,0,0),
    "g": (0,255,0),
    "b": (0,0,255),
    "y": (255,255, 0),
    "o": (255,165, 0),
    "w": (255,255,255)
}

class Draw():
    def __init__(self) -> None:
        self.angle_x = np.pi / 4
        self.angle_y = -np.pi / 8
        self.angle_z = -np.pi / 2
        self.sides = ['u','l','b']

    def rotate(self, movment):
        if movment == "q":
            self.angle_z += ROTATE_SPEED
        elif movment == "a":
            self.angle_z -= ROTATE_SPEED
        else:
            self.angle_x -= movment[0] * ROTATE_SPEED
            self.angle_y -= movment[1] * ROTATE_SPEED
    
    def reset(self):
        self.angle_x -= (self.angle_x - np.pi / 4) / 10
        self.angle_y -= (self.angle_y + np.pi / 8) / 10

    def getPoints(self, pieces):
        for i in pieces:
            i.points = []
            for k in list(product([0.5,-0.5], repeat=3)):
                i.points.append(np.matrix([[i.pos[0] + k[0]], [i.pos[1] + k[1]], [i.pos[2] + k[2]]]))

    def draw(self, pieces):
        clock.tick(20)
        window.fill((0,0,0))

        self.getPoints(pieces)

        rotation_x = np.matrix([[1, 0, 0],
                                [0, cos(self.angle_x), -sin(self.angle_x)],
                                [0, sin(self.angle_x), cos(self.angle_x)]])

        rotation_y = np.matrix([[cos(self.angle_y), 0, sin(self.angle_y)],
                                [0, 1, 0],
                                [-sin(self.angle_y), 0, cos(self.angle_y)]])

        rotation_z = np.matrix([[cos(self.angle_z), -sin(self.angle_z), 0],
                                [sin(self.angle_z), cos(self.angle_z), 0],
                                [0, 0, 1]])
        
        high = 0
        for i in pieces:
            i.points2d = []
            for k in i.points:
                rotate_x = np.matmul(rotation_x, k)
                rotate_y = np.matmul(rotation_y, rotate_x)
                rotate_z = np.matmul(rotation_z, rotate_y)
                
                if len(i.rotation) == 3:
                    if rotate_z.item((2,0)) < high:
                        high = rotate_z.item((2,0))
                        sides = i.rotation

                x = (rotate_z.item((0,0)) * SCALE) + WINDOW_SIZE/2
                y = (rotate_z.item((1,0)) * SCALE) + WINDOW_SIZE/2

                i.points2d.append([x,y])

        for i in pieces:
            directions = {
                "u": [i.points2d[0], i.points2d[1], i.points2d[3], i.points2d[2]],
                "d": [i.points2d[4], i.points2d[5], i.points2d[7], i.points2d[6]],
                "r": [i.points2d[0], i.points2d[1], i.points2d[5], i.points2d[4]],
                "l": [i.points2d[2], i.points2d[3], i.points2d[7], i.points2d[6]],
                "f": [i.points2d[0], i.points2d[2], i.points2d[6], i.points2d[4]],
                "b": [i.points2d[1], i.points2d[3], i.points2d[7], i.points2d[5]]
            }
            
            index = 0
            for k in i.colors:
                if k == ' ':
                    continue

                if i.rotation[index] == sides[0] or i.rotation[index] == sides[1] or i.rotation[index] == sides[2]:
                    index += 1
                    continue

                pg.draw.polygon(window, COLORS[k], directions[i.rotation[index]])
                index += 1

        #self.angle_x = self.angle_y = self.angle_z = self.angle_x + 0.02
        pg.display.flip()