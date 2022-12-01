from copy import copy
import pygame as pg
import random
pg.init()
clock = pg.time.Clock()

SETTINGS = {
    #gamePlay
    "gridSize": (10, 20),               # (int, int)
    "randomBagType": "totalRandom",     # totalRandom, classic, 7-bag, 14-bag, pairs
    "allowedSpins": "none",             # none, T-Spin, allSpin, stupid
    "kickTable": "none",                # none
    "kickMax": 2,                       # int
    "seed": 0,                          # int
    "startingLevel": 1,                 # int
    
    #objectives
    "objective": "none",                # none, score, lines, time
    "count": 20,                        # int
    "time": 120,                        # int
    
    #custom
    "gravity": True,                    # True, False
    "structuralStability": True         # True, False
}

squareSize = 30
width, height = SETTINGS["gridSize"][0]*squareSize, SETTINGS["gridSize"][1]*squareSize
screen = pg.display.set_mode((width, height))

COLORS = {
    "black": (0,0,0),
    "gray": (153,153,153),
    "I": (62,157,212),
    "O": (226,160,44),
    "T": (180,57,141),
    "S": (94,178,0),
    "Z": (216,64,52),
    "J": (33,66,196),
    "L": (222,91,51)
}

class Block:
    def __init__(self, pos, color, center):
        self.pos = pos
        self.color = color
        self.center = center
    
    def __eq__(self, other):
        return self.pos == other.pos
    
    def rotate(self, type):
        offset = [self.center[0] - self.pos[0], self.center[1] - self.pos[1]]
        if type == 0:
            offset = [-offset[1], offset[0]]
        if type == 1:
            offset = [-offset[0], -offset[1]]
        if type == 2:
            offset = [offset[1], -offset[0]]
        self.pos = [self.center[0] - offset[0], self.center[1] - offset[1]]
    
    def copy(self):
        return Block(self.pos, self.color, self.center)

class Tetris:
    level = SETTINGS["startingLevel"]
    hold = None
    currentPiece = None
    bag = []
    nextPieces = []
    activePieces = []
    placedPieces = []
    shadow = []
    
    def __init__(self):
        for i in range(5):
            if self.bag == []:
                self.getBag()
            self.nextPieces.append(self.bag[0])
            self.bag.pop(0)
        self.spawnPiece()
        
    def getShadow(self):
        self.shadow.clear()
        for i in self.activePieces:
            self.shadow.append(i.copy())
        for i in self.shadow:
            i.color = i.color + (128,)
        for i in range(SETTINGS["gridSize"][1]):
            for k in self.shadow:
                if not self.collisionDetect(k, 1):
                    return 
        
            for k in self.shadow:
                k.pos[1] += 1
    
    def spawnPiece(self):
        self.activePieces.clear()
        if self.nextPieces[0] == 'I':
            for i in [[3, 0], [4, 0], [5, 0], [6, 0]]:
                self.activePieces.append(Block(i, COLORS["I"], [4.5, -0.5]))
        elif self.nextPieces[0] == 'T':
            for i in [[4, -1], [3, 0], [4, 0], [5, 0]]:
                self.activePieces.append(Block(i, COLORS["T"], [4, 0]))
        elif self.nextPieces[0] == 'O':
            for i in [[4, -1], [5, -1], [4, 0], [5, 0]]:
                self.activePieces.append(Block(i, COLORS["O"], [4.5, -0.5]))
        elif self.nextPieces[0] == 'J':
            for i in [[3, -1], [3, 0], [4, 0], [5, 0]]:
                self.activePieces.append(Block(i, COLORS["J"], [4, 0]))
        elif self.nextPieces[0] == 'L':
            for i in [[5, -1], [3, 0], [4, 0], [5, 0]]:
                self.activePieces.append(Block(i, COLORS["L"], [4, 0]))
        elif self.nextPieces[0] == 'S':
            for i in [[4, -1], [5, -1], [3, 0], [4, 0]]:
                self.activePieces.append(Block(i, COLORS["S"], [4, -1]))
        elif self.nextPieces[0] == 'Z':
            for i in [[3, -1], [4, -1], [4, 0], [5, 0]]:
                self.activePieces.append(Block(i, COLORS["Z"], [4, -1]))
        
        self.currentPiece = self.nextPieces[0]
        self.nextPieces.pop(0)
        
        if self.bag == []:
            self.getBag()
        self.nextPieces.append(self.bag[0])
        self.bag.pop(0)
        
        for i in self.activePieces:
            for k in self.placedPieces:
                if i == k:
                    self.die()
    
    def getBag(self):
        pieces = ['I', 'T', 'O', 'L', 'J', 'S', 'Z']
        self.bag.append(random.choice(pieces))
        
    def hardDrop(self):
        for i in range(SETTINGS["gridSize"][1]):
            if self.move(1):
                break
        self.placePice()
    
    def holdF(self):
        if self.hold == None:
            self.hold = copy(self.currentPiece)
        else:
            temp = copy(self.hold)
            self.hold = copy(self.currentPiece)
            self.currentPiece = copy(temp)
            self.spawnPiece()
    
    def placePice(self):
        for i in self.activePieces:
            self.placedPieces.append(i)
        self.activePieces.clear()
        self.spawnPiece()

    def move(self, dir):
        for i in self.activePieces:
            if not self.collisionDetect(i, dir):
                return True
        
        for i in self.activePieces:
            if dir == 0:
                i.pos[0] -= 1
                i.center[0] -= 1
            elif dir == 1:
                i.pos[1] += 1
                i.center[1] += 1
            elif dir == 2:
                i.pos[0] += 1
                i.center[0] += 1
            else:
                i.pos[1] -= 1
                i.center[1] -= 1
    
    def rotate(self, type):
        before = copy(self.activePieces)
        for i in self.activePieces:
            i.rotate(type)
        
        if self.collisionDetect(i, -1):
            self.activePieces = copy(before)
            return
    
    def collisionDetect(self, block, dir):
        before = copy(block.pos)
        if dir == 0:
            block.pos[0] -= 1
        elif dir == 1:
            block.pos[1] += 1
        elif dir == 2:
            block.pos[0] += 1
        elif dir == 3:
            block.pos[1] -= 1
        
        if block.pos[0] > SETTINGS["gridSize"][0]-1 or block.pos[0] < 0 or block.pos[1] > SETTINGS["gridSize"][1]-1 or block.pos[1] < -1:
            block.pos = copy(before)
            return False
        
        for i in self.placedPieces:
            if i == block:
                block.pos = copy(before)
                return False
        
        block.pos = copy(before)
        return True
    
    def die(self):
        main.running = False
        print('HA BAD!!!')
        
    def draw(self):
        for i in self.placedPieces + self.activePieces:
            pg.draw.rect(screen, i.color, (i.pos[0]*squareSize, i.pos[1]*squareSize, squareSize, squareSize))
            pg.draw.rect(screen, i.color, (i.pos[0]*squareSize, i.pos[1]*squareSize, squareSize, squareSize))
        for i in self.shadow:
            surface = pg.Surface((squareSize, squareSize))
            pg.draw.rect(surface, i.color, surface.get_rect())
            screen.blit(surface, (i.pos[0]*squareSize, i.pos[1]*squareSize))

class Main:
    running = True
    lastInput = 0
    timer = 1
    
    def eventHandler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    tetris.rotate(0)
                    self.lastInput = 1
                if event.key == pg.K_a:
                    tetris.rotate(1)
                    self.lastInput = 1
                if event.key == pg.K_z:
                    tetris.rotate(2)
                    self.lastInput = 1
                if event.key == pg.K_LEFT:
                    tetris.move(0)
                    self.lastInput = 1
                if event.key == pg.K_DOWN:
                    tetris.move(1)
                    self.lastInput = 1
                if event.key == pg.K_RIGHT:
                    tetris.move(2)
                    self.lastInput = 1
                if event.key == pg.K_RSHIFT and not SETTINGS["gravity"]:
                    tetris.move(3)
                    self.lastInput = 1
                if event.key == pg.K_SPACE:
                    tetris.hardDrop()
                    self.lastInput = 1
                if event.key == pg.K_c:
                    tetris.holdF()
                    self.lastInput = 1
    
    def bugUpdate(self):
        screen.fill(COLORS["black"])
        tetris.draw()
        pg.display.flip()
    
    def tick(self):
        screen.fill(COLORS["black"])
        
        fps = clock.get_fps()
        if fps == 0:
            fps = 60
        deltatime = 1/fps
        
        self.timer -= deltatime
        self.lastInput -= deltatime
        if self.timer <= 0:
            self.timer = 0.5
            if tetris.move(1) and self.lastInput <= 0:
                tetris.placePice()
        
        self.eventHandler()
        
        #tetris.getShadow()
        tetris.draw()
        
        pg.display.flip()

main = Main()
tetris = Tetris()

while main.running:
    main.tick()