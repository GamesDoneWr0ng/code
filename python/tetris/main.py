import pygame as pg
import numpy as np
pg.init()

HEIGHT, WIDTH = 20, 10
SIZE = np.array((HEIGHT, WIDTH), dtype=np.int8)
CELLSIZE = 30

COLORS = (
    (0,0,0),
    (6, 239, 240),
    (240, 240, 0),
    (240, 0, 0),
    (6, 240, 0),
    (0, 0, 240),
    (240, 160, 0),
    (160, 0, 240)
)

PIECES = [
    np.array(((1,1,1,1),
              (0,0,0,0),
              (0,0,0,0),
              (0,0,0,0))),

    np.array(((2,2),
              (2,2))),

    np.array(((3,3,0),
              (0,3,3),
              (0,0,0))),

    np.array(((0,4,4),
              (4,4,0),
              (0,0,0))),

    np.array(((5,5,5),
              (5,0,0),
              (0,0,0))),

    np.array(((6,6,6),
              (0,0,6),
              (0,0,0))),

    np.array(((0,7,0),
              (7,7,7),
              (0,0,0)))
]

screen = pg.display.set_mode((WIDTH * CELLSIZE, HEIGHT * CELLSIZE))
clock = pg.time.Clock()

class Tetris:
    def __init__(self, screen: pg.Surface, size: np.ndarray, startSpeed: int = 40):
        self.screen: pg.Surface = screen
        self.screen.fill(COLORS[0])
        self.size: np.ndarray = size
        self.speed = startSpeed
        self.dropTimer = self.speed
        self.board: np.ndarray = np.zeros(size)
        self.batch = []
        self.piece: np.ndarray = self.newPiece()

    def newPiece(self) -> np.ndarray:
        self.piecePos: np.ndarray = np.array((0, 4))
        if len(self.batch) == 0:
            self.batch = list(range(7))
            np.random.shuffle(self.batch)
        return PIECES[self.batch.pop()]
    
    def draw(self, drawpiece: bool = True):
        for row in range(max(self.piecePos[0]-1, 0), min(self.piecePos[0] + self.piece.shape[0], HEIGHT)):
            for col in range(max(self.piecePos[1]-1, 0), min(self.piecePos[1] + self.piece.shape[1] +1, WIDTH)):
                pieceInternalPos = np.array((row, col)) - self.piecePos
                pg.draw.rect(self.screen, 
                             COLORS[int((drawpiece 
                                         and np.all(np.logical_and(pieceInternalPos < self.piece.shape, pieceInternalPos >= 0)) 
                                         and (self.piece[pieceInternalPos[0], pieceInternalPos[1]]) or self.board[row, col]))], 
                             pg.Rect(col*CELLSIZE, row*CELLSIZE, CELLSIZE, CELLSIZE))
    
    def drawAll(self):
        for row in range(HEIGHT):
            for col in range(WIDTH):
                pieceInternalPos = np.array((row, col)) - self.piecePos
                pg.draw.rect(self.screen, 
                             COLORS[int((np.all(np.logical_and(pieceInternalPos < self.piece.shape, pieceInternalPos >= 0)) 
                                         and (self.piece[pieceInternalPos[0], pieceInternalPos[1]]) or self.board[row, col]))], 
                             pg.Rect(col*CELLSIZE, row*CELLSIZE, CELLSIZE, CELLSIZE))

    def collition(self, piece: np.ndarray, pos: np.ndarray) -> bool:
        shape = np.array(np.where(piece))
        low  = np.min(shape, axis=1)
        high = np.max(shape, axis=1)
        return np.any(np.logical_and(piece[tuple(slice(l  ,h+1) for l, h in zip(low, high))], 
                                self.board[tuple(slice(p+l,p+h+1) for p, l, h in zip(pos, low, high))]))

    def rotate(self, k):
        newPiece = np.rot90(self.piece, k=k)
        if not (np.any(self.piecePos+np.max(np.array(np.where(newPiece)), axis=1) >= self.size) 
                or np.any(self.piecePos+np.min(np.array(np.where(newPiece)), axis=1)<0) 
                or self.collition(newPiece, self.piecePos)):
            self.draw(False)
            self.piece = newPiece
            self.draw()

    def update(self):
        change = False
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                return False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if not (self.piecePos[1]+np.min(np.where(self.piece)[1]) <= 0 or self.collition(self.piece, self.piecePos + np.array((0,-1)))):
                        self.piecePos[1] -= 1
                if event.key == pg.K_RIGHT:
                    if not (self.piecePos[1]+np.max(np.where(self.piece)[1])+1 >= WIDTH or self.collition(self.piece, self.piecePos + np.array((0,1)))):
                        self.piecePos[1] += 1
                if event.key == pg.K_UP:
                    self.rotate(-1)
                if event.key == pg.K_z:
                    self.rotate(1)
                if event.key == pg.K_a:
                    self.rotate(2)
                if event.key == pg.K_SPACE:
                    self.draw(False)
                    distance = 1
                    while not (self.piecePos[0]+np.max(np.where(self.piece)[0])+distance >= HEIGHT or self.collition(self.piece, self.piecePos + np.array((distance, 0)))):
                        distance += 1
                    self.piecePos[0] += distance-1
                    self.dropTimer = 0

        if self.dropTimer == 0:
            self.dropTimer = self.speed
            if not (self.piecePos[0]+np.max(np.where(self.piece)[0]+1) >= HEIGHT or self.collition(self.piece, self.piecePos + np.array((1,0)))):
                self.piecePos[0] += 1
            else:
                shape = np.array(np.where(self.piece))
                low  = np.min(shape, axis=1)
                high = np.max(shape, axis=1)
                cut = tuple(slice(p+l,p+h+1) for p,l,h in zip(self.piecePos, low, high))
                self.board[cut] = self.piece[tuple(slice(l,h+1) for l,h in zip(low, high))] + self.board[cut]
                self.draw()
                lineclears = np.where(np.all(self.board > 0, axis=1))[0]
                for i in lineclears:
                    self.board[1:i+1] = self.board[:i]
                    self.board[0] = 0
                self.piece = self.newPiece()
                if lineclears.size != 0:
                    self.drawAll()
        else:
            self.dropTimer -= 1

        self.draw()
        pg.display.flip()
        return True

tetris = Tetris(screen, SIZE)

while True:
    alive = tetris.update()
    clock.tick(60)
    if not alive:
        break