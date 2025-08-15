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
    (240, 160, 0)
)

PIECES = [
    np.array(((1,1,1,1))),

    np.array(((2,2),
              (2,2))),

    np.array(((3,3,0),
              (0,3,3))),

    np.array(((0,4,4),
              (4,4,0))),

    np.array(((5,5,5),
              (5,0,0))),

    np.array(((6,6,6),
              (0,0,6))),

    np.array(((7,7,7),
              (0,7,0)))
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
            self.batch = np.random.shuffle(list(range(6)))
        return PIECES[self.batch.pop()]
    
    def draw(self, drawpiece: bool):
        for row in range(max(self.piecePos[0]-1, 0), self.piecePos[1] + self.piece.shape[0]):
            for col in range(max(self.piecePos[0]-1, 0), min(self.piecePos[1] + self.piece.shape[1] +1, WIDTH)):
                pg.draw.rect(self.screen, COLORS[(drawpiece and self.piece[self.size-self.piecePos]) or self.board[row, col]], pg.Rect(col*CELLSIZE, row*CELLSIZE, CELLSIZE, CELLSIZE))

    def collition(self, piece: np.ndarray, pos: np.ndarray) -> bool:
        shape = piece.shape
        return np.any(np.logical_and(piece, self.board[tuple(slice(p,p+s) for p, s in zip(pos, shape))]))

    def update(self):
        change = False
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                return False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if not (self.piecePos[1] <= 0 or self.collition(self.piece, self.piecePos + np.array((0,-1)))):
                        self.piecePos[1] -= 1
                        change = True
                if event.key == pg.K_RIGHT:
                    if not (self.piecePos[1]+self.piece.shape[1] >= WIDTH or self.collition(self.piece, self.piecePos + np.array((0,1)))):
                        self.piecePos[1] += 1
                        change = True
                if event.key == pg.K_UP:
                    newPiece = np.rot90(self.piece, k=-1)
                    if not (np.any(self.piecePos+newPiece.shape > self.size) or self.collition(newPiece, self.piecePos)):
                        self.piece = newPiece
                        change = True
                if event.key == pg.K_z:
                    newPiece = np.rot90(self.piece, k=1)
                    if not (np.any(self.piecePos+newPiece.shape > self.size) or self.collition(newPiece, self.piecePos)):
                        self.piece = newPiece
                        change = True
                if event.key == pg.K_SPACE:
                    self.draw(False)
                    distance = 1
                    while not (self.piecePos[0]+self.piece.shape[0]+distance >= HEIGHT or self.collition(self.piece, self.piecePos + np.array((distance, 0)))):
                        distance += 1
                    self.piecePos[0] += distance
                    self.dropTimer = 0

        if self.dropTimer == 0:
            self.dropTimer = self.speed
            if not (self.piecePos[0]+self.piece.shape[0]+1 >= HEIGHT or self.collition(self.piece, self.piecePos + np.array(1,0))):
                self.piecePos[0] += 1
            else:
                self.board[self.piecePos[0]+self.piece.shape[0]:self.piecePos[1]+self.piece.shape[1]] = np.max(self.piece, self.board[self.piecePos[0]+self.piece.shape[0]:self.piecePos[1]+self.piece.shape[1]])
                self.draw()
                self.newPiece()
        else:
            self.dropTimer -= 1

        self.draw()
        return True

tetris = Tetris(screen, SIZE)