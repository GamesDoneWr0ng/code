import numpy as np

# bricks for a brakeout game
class Bricks:
    def __init__(self, size):
        self.size = size
        self.bricks = np.array([[1 for x in range(size[0]*3)] for y in range(size[1]*2)] + [[0 for x in range(size[0]*3)] for y in range(size[1]*2)])
        self.ball = np.array([int(size[0] *0.5), int(size[1] *0.5)])
        self.velocity = [1, 1]
        self.paddle = [int(size[0] *0.5), int(size[1] *0.9)]
        self.paddleSize = 15
        self.ballRadius = 0.5

    def update(self, deltaTime):
        self.ball[0] += self.velocity[0] * deltaTime
        if self.checkCollision():
            self.velocity[0] *= -1
            self.destroyBrick()

        self.ball[1] += self.velocity[1] * deltaTime
        if self.checkCollision():
            self.velocity[1] *= -1
            self.destroyBrick()

        if self.ball[0] < 0 or self.ball[0] > self.size[0] - 1:
            self.velocity[0] *= -1
        if self.ball[1] < 0 or self.ball[1] > self.size[1] - 1:
            self.velocity[1] *= -1

        if self.ball[1] == self.paddle[1] and \
            self.ball[0] >= self.paddle[0] - self.paddleSize and \
            self.ball[0] <= self.paddle[0] + self.paddleSize and \
            self.velocity[1] > 0:

            self.velocity[1] *= -1
            self.velocity[0] = self.velocity[0] * (self.paddle[0] - self.ball[0]) / self.paddleSize

    def checkCollision(self):
        for i in range(self.bricks.shape[0]):
            for j in range(self.bricks.shape[1]):
                if self.bricks[i,j] == 1:  # check if there is a brick at this position
                    brick_pos = (i,j)
                    distance = ((brick_pos[0] - self.ball[0])**2 + (brick_pos[1] - self.ball[1])**2)**0.5
                    if distance <= self.ballRadius:
                        return True

    def destroyBrick(self):
        topLeftOffset = self.ball[0] % 3, self.ball[1] % 2
        topLeft = self.ball - topLeftOffset
        self.bricks[topLeft[0]][topLeft[1] : topLeft[1] + 3] = 0
        self.bricks[topLeft[0] + 1][topLeft[1] : topLeft[1] + 3] = 0

    def move(self, dir, deltatime):
        self.paddle[0] += dir * deltatime