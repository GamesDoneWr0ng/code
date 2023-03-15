from PPO import PPO
from Network import Network
import numpy as np
import pygame as pg
pg.init()

gridSize = 20
width, height = gridSize*30, gridSize*30
screen = pg.display.set_mode((width, height))

COLORS = {
    "black": (0,0,0),
    "red": (255,0,0),
    "green": (0,255,0),
    "white": (255,255,255)
}

REWARDSIZES = {
    "apple": 1,
    "die": -1,
    "moveCloser": 0.1,
    "moveAway": -0.1,
    "makeHole": -0.3
}

class Snake:
    def __init__(self):
        g = np.floor(gridSize/2)
        self.parts = [[g - i, g] for i in reversed(range(5))]
        self.length = 5
        self.apple = [g + 5, g]

        # ai
        self.lastdistance = np.abs(np.subtract(self.parts[-1], self.apple))
        self.generation = 1
        self.states = []
        self.storeState()
        self.rewards = []
        network = Network(39, [30,20,10], 4)
        self.ai = PPO(network, gridSize ** 2 * REWARDSIZES["apple"])

    def move(self, rotation):
        newPos = np.add(self.parts[-1], rotation)

        # hit a wall
        if np.all((newPos >= 0)&(newPos < gridSize)):
            self.die()
            return
        # didn't get apple
        if newPos != self.apple:
            self.parts.pop(0)
        # got apple
        else:
            self.newApple()
        # hit snake
        if np.any(np.all(np.equal(newPos, self.parts), axis=1)):
            self.die()
            return
        self.parts.append(newPos)

        distance = np.abs(np.subtract(self.parts[-1], self.apple))
        if distance > self.lastdistance:
            self.rewards.append(REWARDSIZES["moveAway"])
        else:
            self.rewards.append(REWARDSIZES["moveCloser"])

        self.storeState()
        self.draw()

    def die(self):
        self.rewards.append(REWARDSIZES["die"])
        print(f"Generation: {self.generation}, Reward: {np.sum(self.rewards)}")
        self.ai.train(self.states, self.rewards)
        # reset
        g = np.floor(gridSize/2)
        self.parts = [[g - i, g] for i in reversed(range(5))]
        self.length = 5
        self.apple = [g + 5, g]

    def newApple(self):
        self.rewards.append(REWARDSIZES["apple"])
        if self.length == gridSize ** 2:
            print("Perfect game reached at:")
            print(f"Generation: {self.generation}, Reward: {np.sum(self.rewards)}")
            print("YAY")

        # spawn apple
        while True:
            pos = [np.random.randint(0,gridSize), np.random.randint(0,gridSize)]
            if np.any(np.all(np.equal(pos, self.parts), axis=1)):
                continue
            self.apple = pos
            return
        
    def collide(self, pos, state, length):
        changed = False
        if np.all(np.equal(pos, self.apple)):
            state.append(length / gridSize)                     # lenght
            state.append(1)                                     # apple
            changed = True
        elif np.any(np.all(np.equal(pos, self.parts), axis=1)):
            state.append(length / gridSize)                     # lenght
            state.append(0)                                     # snake
            changed = True
        elif not np.all((pos >= 0)&(pos < gridSize)):
            state.append(length / gridSize)                     # lenght
            state.append(-1)                                    # wall
            changed = True
        return state, changed

    def storeState(self):
        """inputs from snake
        16 lines out of snake head (distance to colistion / max distance)
        16 inputs for what the lines hit (-1 wall, 0 snake, 1 apple)
        2 for head position
        2 for relative position to apple
        2 for relative position to tail
        1 for snake lenght
        """
        state = []
        # vision
        for i in [[0,1], [1,2], [1,1], [2,1], [1,0], [2,-1], [1,-1], [1,-2], [0,-1], [-1, -2], [-1,-1], [-2, -1], [-1, 0], [-2, 1], [-1,1], [-1, 2]]:
            pos = self.parts[-1]
            for length in range(1, gridSize+1):
                if np.sum(np.abs(i)) == 3:
                    tempPos = np.add(pos, np.floor_divide(i,2))
                    state, changed = self.collide(tempPos, state, 2*length-1)
                    if changed:
                        break

                    pos = np.add(pos, i)
                    state, changed = self.collide(pos, state, 2*length)
                else:
                    pos = np.add(pos, i)
                    state, changed = self.collide(pos, state, length)     
                
                if changed:
                    break

        # positions
        state.append(self.parts[-1][0] / gridSize)                      # head x
        state.append(self.parts[-1][1] / gridSize)                      # head y

        state.append((self.apple[0] - self.parts[-1][0]) / gridSize)    # relative apple x
        state.append((self.apple[1] - self.parts[-1][1]) / gridSize)    # relative apple y

        state.append((self.parts[0][0] - self.parts[-1][0]) / gridSize) # relative tail x
        state.append((self.apple[1] - self.parts[-1][1]) / gridSize)    # relative tail y

        # lenght
        state.append(self.length / gridSize ** 2)                       # lenght

        self.states.append(state)

    def draw(self):
        screen.fill(COLORS["black"])
        for i in self.parts:
            pg.draw.rect(screen, COLORS["green"], pg.rect.Rect(i[0]*30, i[1]*30, 30, 30))
        pg.draw.rect(screen, COLORS["red"], pg.rect.Rect(self.apple[0]*30, self.apple[1]*30, 30, 30))
        for i in range(30, gridSize*30, 30):
            pg.draw.line(screen, COLORS["white"], (i, 0), (i, gridSize*30))
            pg.draw.line(screen, COLORS["white"], (0, i), (gridSize*30, i))
        pg.display.flip()

snake = Snake()

while True:
    snake.ai.actor.forward(snake.states[-1])