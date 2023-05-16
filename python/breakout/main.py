from bricks import Bricks
import pygame as pg
pg.init()

COLORS = [
    (255, 0,   128),
    (255, 0,   255),
    (128, 0,   255),
    (0,   0,   255),
    (0,   128, 255),
    (0,   255, 255),
    (0,   255, 128),
    (0,   255, 0  ),
    #(128, 255, 0  ),
    (255, 255, 0  ),
    (255, 128, 0  ),
    (255, 0,   0  ),
]

windowSize = (900, 600)
window = pg.display.set_mode(windowSize)
pg.display.set_caption("Breakout")
clock = pg.time.Clock()
gridSize = (20, 10)
brickSize = (windowSize[0] // (gridSize[0]*3), windowSize[1] // (gridSize[1] * 6))

class Main:
    def __init__(self):
        self.bricks = Bricks(gridSize)
        self.running = True

    def draw(self):
        window.fill((0, 0, 0))
        color = -1
        for row in range(0, len(self.bricks.bricks), 2):
            for column in range(0, len(self.bricks.bricks[row]), 3):
                color = (color + 1) % len(COLORS)
                if self.bricks.bricks[row][column] == 0:
                    continue
                pg.draw.rect(window, COLORS[color],  (column * brickSize[0], row * brickSize[1], brickSize[0]*3, brickSize[1]*2))

        pg.draw.circle(window, (255, 255, 255), (self.bricks.ball[0]*brickSize[0], self.bricks.ball[1]*brickSize[1]), self.bricks.ballRadius * brickSize[1])
        pg.draw.rect(window, (255, 255, 255), (self.bricks.paddle[0]*brickSize[0]*6 - self.bricks.paddleSize*brickSize[0] *3, self.bricks.paddle[1]*brickSize[1]*6, self.bricks.paddleSize*brickSize[1] *3, 10))

        pg.display.update()
    
    def inputhandler(self, deltatime):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    main.bricks.move(-1, deltatime)
                if event.key == pg.K_RIGHT:
                    self.bricks.move(1, deltatime)

main = Main()

while main.running:
    clock.tick(60)
    deltatime = 1 / max(clock.get_fps(), 60)

    main.inputhandler(deltatime)
    main.bricks.update(deltatime)
    main.draw()