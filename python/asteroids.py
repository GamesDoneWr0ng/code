import pygame as pg
import math
import random
pg.init()
clock = pg.time.Clock()
#creates screen variable and resolution
width, height = 600, 600
screen = pg.display.set_mode((width, height))

#Dictonary for easy access to colors
COLORS = {
    "black": (0,0,0),
    "white": (255,255,255)
}

#rotates a polygon a set amount of degrees
def rotatePolygon(polygon,theta):
    theta = math.radians(theta)
    rotatedPolygon = []
    for corner in polygon :
        temp = corner[0]*math.cos(theta)-corner[1]*math.sin(theta) , corner[0]*math.sin(theta)+corner[1]*math.cos(theta)
        rotatedPolygon.append([temp[0], temp[1]])
    return rotatedPolygon

def collision(poly1, poly2):
    #creates a list of lines that make up poly1
    poly1lines = []
    for i in poly1:
        if i != poly1[0]:
            poly1lines.append((lastpoint, i))
        lastpoint = i
    
    #creates a list of lines that make up poly2
    poly2lines = []
    for i in poly2:
        if i != poly2[0]:
            poly2lines.append((lastpoint, i))
        lastpoint = i
    
    for i in poly1lines:
        # Variables for the first line
        x1, y1, x2, y2 = i[0][0], i[0][1], i[1][0], i[1][1]
        
        for k in poly2lines:
            # Variables for the second line
            x3, y3, x4, y4 = k[0][0], k[0][1], k[1][0], k[1][1]
            
            # math shit
            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if den == 0:
                return
 
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            u = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / den
            if 0 < t < 1 and 0 < u < 1:
                return True

#the ship
class Ship:
    #variabels
    pos = [300, 300]
    rot = 0
    speed = [0, 0]
    points = [(0, -10), (10, 10), (0, 5), (-10, 10)]
    score = 0
    
    #draws the ship
    def draw(self):
        self.points = rotatePolygon([(0, -10), (10, 10), (0, 5), (-10, 10)], self.rot)
        for i in self.points:
            index = self.points.index(i)
            i = [i[0]+self.pos[0], i[1]+self.pos[1]]
            self.points[index] = i
        pg.draw.polygon(screen, COLORS["white"], self.points)
    
    #adds speed
    def addSpeed(self):
        self.speed[0] += main.deltaTime * 10 * math.cos(math.radians((self.rot - 90)))
        self.speed[1] += main.deltaTime * 10 * math.sin(math.radians((self.rot - 90)))
    
    #warp the ship to the other side of the screen when you hit a wall
    def edge(self):
        if self.pos[0] >= 610:
            self.pos[0] = 0
        elif self.pos[0] <= -10:
            self.pos[0] = 600
        elif self.pos[1] >= 610:
            self.pos[1] = 0
        elif self.pos[1] <= -10:
            self.pos[1] = 600
    
    #die
    def die(self):
        print("HA BAD!!!")
        main.running = False
    
    #ship collision
    def collision(self):
        #asteroid collision
        for i in asteroid.asteroids:
            apoints = []
            for k in i["points"]:
                apoints.append((k[0]+i["pos"][0], k[1]+i["pos"][1]))
            if collision(self.points, apoints):
                self.die()
        
        #bullet collision
        for i in bullet.bullets:
            bpoints = [(0+i["pos"][0], -3+i["pos"][1]), (3+i["pos"][0], 0+i["pos"][1]), (0+i["pos"][0], 3+i["pos"][1]), (-3+i["pos"][0], 0+i["pos"][1])]
            if collision(self.points, bpoints):
                self.die()
    
    #runs every frame
    def tick(self):
        self.speed[0] = self.speed[0] * 0.99
        self.speed[1] = self.speed[1] * 0.99
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        self.edge()
        self.collision()        

#the bullets
class Bullet:
    #where all the bullets data is stored
    bullets = []
    
    #adds another bullet
    def addBullet(self):
        shipPos = [ship.pos[0]+1-1, ship.pos[1]+1-1]
        shipRot = ship.rot +1-1
        shipSpeed = [ship.speed[0], ship.speed[1]]
        speed = [main.deltaTime * 300 * math.cos(math.radians((shipRot -90))), main.deltaTime * 300 * math.sin(math.radians((shipRot -90)))]
        self.bullets.append({"pos": [shipPos[0] + speed[0]*4, shipPos[1] + speed[1]*4], "speed": (speed[0]+shipSpeed[0], speed[1]+shipSpeed[1])})
    
    #draws the bullet
    def draw(self):
        for i in self.bullets:
            pg.draw.circle(screen, COLORS["white"], i["pos"], 3)
    
    #warp the bullet to the other side of the screen when you hit a wall
    def edge(self):
        for i in self.bullets:
            if i["pos"][0] >= 610:
                i["pos"][0] = 0
            elif i["pos"][0] <= -10:
                i["pos"][0] = 600
            elif i["pos"][1] >= 610:
                i["pos"][1] = 0
            elif i["pos"][1] <= -10:
                i["pos"][1] = 600
    
    #runs every tick
    def tick(self):
        for i in self.bullets:
            i["pos"][0] += i["speed"][0]
            i["pos"][1] += i["speed"][1]
        self.edge()

#the asteroids
class Asteroid:
    #where all the asteroids data is stored
    asteroids = []
    
    #adds another asteroid
    def addAsteroid(self):
        pos = round(random.randint(0, 3))
        if pos == 0:
            pos = [0, random.random() * 600]
        elif pos == 1:
            pos = [random.random() * 600, 0]
        elif pos == 2:
            pos = [600, random.random() * 600]
        elif pos == 3:
            pos = [random.random() * 600, 600]
        speed = [random.randint(-100, 100), random.randint(-100, 100)]
        points = []
        edges = random.randint(5, 8)
        for i in range(edges):
            points.append([random.randint(20,40), 0])
            points = rotatePolygon(points, 360/edges)
        self.asteroids.append({"pos": pos, "speed": speed, "rot": 0, "rotSpeed": random.random(), "points": points})
    
    #draws the asteroids
    def draw(self):
        for i in self.asteroids:
            for k in self.asteroids:
                k["points"] = rotatePolygon(k["points"], k["rotSpeed"])
            points = []
            for k in i["points"]:
                k = k*1
                k[0] += i["pos"][0]
                k[1] += i["pos"][1]
                points.append(k)
            pg.draw.polygon(screen, COLORS["white"], points)
    
    #warps the asteroid to the other side of the screen when they hit the edge
    def edge(self):
        for i in self.asteroids:
            pos = i["pos"]
            if pos[0] >= 610:
                i["pos"][0] = 0
            elif pos[0] <= -10:
                i["pos"][0] = 600
            elif pos[1] >= 610:
                i["pos"][1] = 0
            elif pos[1] <= -10:
                i["pos"][1] = 600
    
    #collision detection with bullets
    def collision(self):
        for i in self.asteroids:
            apoints = []
            for k in i["points"]:
                apoints.append((k[0]+i["pos"][0], k[1]+i["pos"][1]))
            for k in bullet.bullets:
                bpoints = [(0+k["pos"][0], -3+k["pos"][1]), (3+k["pos"][0], 0+k["pos"][1]), (0+k["pos"][0], 3+k["pos"][1]), (-3+k["pos"][0], 0+k["pos"][1])]
                if collision(apoints, bpoints):
                    if i in self.asteroids:
                        self.asteroids.remove(i)
                    if k in bullet.bullets:
                        bullet.bullets.remove(k)
                    ship.score += 1
    
    #runs every tick
    def tick(self):
        for i in self.asteroids:
            speed = i["speed"]
            i["pos"][0] += (speed[0] * main.deltaTime)
            i["pos"][1] += (speed[1] * main.deltaTime)
        self.edge()
        self.collision()

class Main:
    running = True
    deltaTime = 0.02
    asteroidTimer = 500
    
    def eventHandler(self):
        #checks for button inputs
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    bullet.addBullet()
                if event.key == pg.K_k:
                    asteroid.addAsteroid()
    
        #checks for button inputs but fast
        keys=pg.key.get_pressed()
        if keys[pg.K_a]:
            ship.rot = (ship.rot - (250 * main.deltaTime)) % 359
        if keys[pg.K_d]:
            ship.rot = (ship.rot + (250 * main.deltaTime)) % 359
        if keys[pg.K_w]:
            ship.addSpeed()
        if keys[pg.K_m]:
            bullet.addBullet()
    
    def tick(self):
        #clears the screen and creates deltatime
        screen.fill(COLORS["black"])
        clock.tick(60)
        self.deltaTime = 1 / (clock.get_fps() + 0.01)
        
        #spawns an asteroid every second
        if self.asteroidTimer < 0:
            asteroid.addAsteroid()
            self.asteroidTimer = 5 / ((ship.score+5)/5)
        self.asteroidTimer = self.asteroidTimer - self.deltaTime

        #events
        self.eventHandler()
        
        #displays your score
        font = pg.font.SysFont('didot.ttc', 50)
        img = font.render(str(ship.score), True, COLORS["white"])
        screen.blit(img, (0, 0))
        
        #calls varius functions
        ship.draw()
        ship.tick()
    
        bullet.draw()
        bullet.tick()
    
        asteroid.draw()
        asteroid.tick()
    
        #displays everything
        pg.display.flip()
        
#initializes the classes above
ship = Ship()
bullet = Bullet()
asteroid = Asteroid()
main = Main()

while main.running:
    main.tick()