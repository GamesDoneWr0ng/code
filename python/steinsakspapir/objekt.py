import numpy as np
import pygame as pg
pg.init()

SIZE = WIDTH, HEIGHT = 1280, 700
screen = pg.display.set_mode(SIZE)#, pg.FULLSCREEN)

clock = pg.time.Clock()

class Object:
    def __init__(self, position: np.ndarray, velocity: np.ndarray, type: str) -> None:
        self.position: np.ndarray = position
        self.velocity: np.ndarray = velocity
        self.type: str = type
        self.radius = 10
    
    # use boids as starting point for movement
    def centerOfMassSelf(self, others: list):
        sum = np.zeros(2)
        count = 0

        for other in others:
            if other == self:
                continue
            if other.type != self.type:
                continue
            sum += other.position
            count += 1

        if count == 0:
            return np.zeros(2)
        
        sum /= count
        return (sum - self.position) / 100
    
    def dontCollide(self, others: list):
        sum = np.zeros(2)

        for other in others:
            if other == self:
                continue
            if other.type != self.type:
                continue
            if np.sum((other.position - self.position)**2) < 100**2:
                sum -= other.position - self.position

        return sum
    
    def matchSpeed(self, others: list):
        sum = np.zeros(2)
        count = 0

        for other in others:
            if other == self:
                continue
            if other.type != self.type:
                continue
            sum += other.velocity
            count += 1

        if count == 0:
            return np.zeros(2)
        sum /= count
        return (sum-self.velocity)/8
    
    def goToTargetMass(self, others: list, target: str):
        sum = np.zeros(2)
        count = 0

        for other in others:
            if other.type != target:
                continue
            sum += other.position
            count += 1

        if count == 0:
            return np.zeros(2)
        
        sum /= count
        return (sum - self.position) / 100
    
    def hitTarget(self, others: list, target: str):
        sum = np.zeros(2)

        for other in others:
            if other.type != target:
                continue
            if np.sum((other.position - self.position)**2) < 100**2:
                sum += other.position - self.position

        return sum
    
    def move(self, others: list, target: str):
        self.velocity += self.centerOfMassSelf(others)/3
        self.velocity += self.dontCollide(others)/60
        self.velocity += self.matchSpeed(others)/60
        self.velocity += self.goToTargetMass(others, target)/3
        self.velocity += self.hitTarget(others, target)/10

        if np.sum(self.velocity**2) > 600**2:
            self.velocity /= np.linalg.norm(self.velocity) * 600

        self.position += self.velocity/60

    def render(self):
        match self.type:
            case "rock":
                pg.draw.circle(screen, (0, 0, 255), self.position, self.radius)
            case "paper":
                pg.draw.circle(screen, (255, 0, 0), self.position, self.radius)
            case "scissor":
                pg.draw.circle(screen, (255, 255, 0), self.position, self.radius)

    def collision(self, others: list):
        self.velocity[np.logical_or(self.position+self.radius > SIZE, self.position-self.radius < 0)] *= -1

        for other in others:
            if other.type == self.type:
                continue
            if np.sum((other.position - self.position)**2) < self.radius**2:
                if other.type == targets[self.type]:
                    other.type = self.type
                else:
                    self.type = other.type
        return False
    
    def debug(self, others, type):
        pg.draw.line(screen, (0, 255, 0), self.position, self.position+self.centerOfMassSelf(others)*100)
        pg.draw.line(screen, (255, 0, 0), self.position, self.position+self.goToTargetMass(others, type)*100)
        pg.draw.line(screen, (0, 0, 255), self.position, self.position+self.matchSpeed(others)*8)
        pg.draw.circle(screen, (0, 255, 0), self.position, 100, 1)
        for other in others:
            if np.sum((other.position - self.position)**2) < 100**2:
                if other.type == self.type:
                    pg.draw.line(screen, (0, 255, 0), self.position, other.position)
                if other.type == type:
                    pg.draw.line(screen, (255, 0, 0), self.position, other.position)

targets = {
    "rock": "scissor",
    "scissor": "paper",
    "paper": "rock"
}

objects = [Object(np.random.uniform(10,np.array(SIZE)-10,2), np.random.uniform(-2,2,2), np.random.choice(["rock", "paper", "scissor"]))
           for i in range(300)]

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for index, object in enumerate(objects):
        object.move(objects, targets[object.type])
        object.render()
        object.collision(objects[:index+1])
        #object.debug(objects, targets[object.type])

    #objects[0].debug(objects, targets[objects[0].type])

    clock.tick(60)
    pg.display.flip()