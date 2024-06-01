import random
import pygame as pg
import math
pg.init()
clock = pg.time.Clock()

gridSize = 20
width, height = gridSize*30, gridSize*30
screen = pg.display.set_mode((width, height))


COLORS = {
    "black": (0,0,0),
    "red": (255,0,0),
    "green": (0,255,0),
    "white": (255,255,255)
}

class Snake:
    g = math.floor(gridSize/2)*30
    parts = [[g-150, g], [g-120, g], [g-90, g], [g-60, g], [g-30, g], [g, g]]
    rot = 1
    pos = parts[-1]*1
    length = 5
    
    def move(self):
        if self.rot == 0:
            self.pos[1] = self.pos[1] - 30
        elif self.rot == 1:
            self.pos[0] = self.pos[0] + 30
        elif self.rot == 2:
            self.pos[1] = self.pos[1] + 30
        elif self.rot == 3:
            self.pos[0] = self.pos[0] - 30
        self.parts.append(self.pos*1)
        if len(self.parts)>self.length:
            del self.parts[0]
            
    def edge(self):
        if self.pos[0] < 0:
            self.die()
        elif self.pos[1] < 0:
            self.die()
        elif self.pos[0] > gridSize*30:
            self.die()
        elif self.pos[1] > gridSize*30:
            self.die()
    
    def die(self):
        print("HA BAD!!!")
        main.running = False
    
    def collision(self):
        self.edge()
        for i in apple.apples:
            if self.pos == i:
                self.length += 1
                apple.addApple()
                if i in apple.apples:
                    apple.apples.pop(apple.apples.index(i))
        
        for i in self.parts:
            if self.parts.count(i) > 1:
                self.die()
                break
    
    def draw(self):
        for i in self.parts:
            pg.draw.rect(screen, COLORS["green"], pg.rect.Rect(i[0], i[1], 30, 30))

class Apple:
    apples = []
    
    def addApple(self):
        while True:
            pos = [random.randint(0, gridSize-1) * 30, random.randint(0, gridSize-1) * 30]
            if not pos in snake.parts and not pos in self.apples:
                self.apples.append(pos)
                break
    
    def draw(self):
        for i in self.apples:
            pg.draw.rect(screen, COLORS["red"], pg.rect.Rect(i[0], i[1], 30, 30))
            
#AI ikke viktig for framvisning
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = [current_node.position[0] + new_position[0], current_node.position[1] + new_position[1]]

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            flag = False
            for closed_child in closed_list:
                if child == closed_child:
                    flag = True
                    break
            if flag:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = child.position[0] - end_node.position[0] + child.position[1] - end_node.position[1]
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g >= open_node.g:
                    open_list.remove(open_node)
                    continue

            # Add the child to the open list
            open_list.append(child)

class Hamiltonian:
    cycle = [[2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [2,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [2,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [2,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [2,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [2,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [2,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [2,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [2,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
             [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [2,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0]]
    
    cycleIndex = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    appleIndex = 0
    snakeIndexes = []
    skiped = []
    
    
    def __init__(self):
        index = -1
        for i in range(20):
            index += 1
            self.cycleIndex[i].append(index)
        for i in range(10):
            for k in range(19):
                index += 1
                self.cycleIndex[19-2*i].append(index)
            for k in range(19):
                index += 1
                self.cycleIndex[18-2*i].insert(1, index)
    
    def skip(self):
        if snake.length > 300:
            return True
        self.appleIndex = self.cycleIndex[int(apple.apples[0][1]/30)][int(apple.apples[0][0]/30)]
        self.snakeIndexes = []
        for i in [[0, -30], [0, 30], [-30, 0], [30, 0]]:
            child = [i[0]+snake.pos[0], i[1]+snake.pos[1]]
            if child in snake.parts:
                continue
            if child[0]/30 > (len(self.cycle) - 1) or child[0]/30 < 0 or child[1]/30 > (len(self.cycle[len(self.cycle)-1]) -1) or child[1]/30 < 0:
                continue
            self.snakeIndexes.append(self.cycleIndex[int(child[1]/30)][int(child[0]/30)])
        for i in self.snakeIndexes:
            s = self.cycleIndex[int(snake.pos[1]/30)][int(snake.pos[0]/30)]
            if i < s:
                continue
            if s < self.appleIndex < i:
                continue
            if i == s + 1:
                continue
            snake.move()
            return False
        return True

def runAi():
    if main.aiMode == 1:
        main.setupAStar()
        if main.path == None:
            main.aiMode = False
        if main.aiMode:
            if snake.pos[0] > main.path[1][1]*30:
                snake.rot = 3
                snake.move()
            elif snake.pos[0] < main.path[1][1]*30:
                snake.rot = 1
                snake.move()
            elif snake.pos[1] > main.path[1][0]*30:
                snake.rot = 0
                snake.move()
            elif snake.pos[1] < main.path[1][0]*30:
                snake.rot = 2
                snake.move()
    
    elif main.aiMode == 2:
        if gridSize == 20:
            if hamiltonian.skip():
                snake.rot = hamiltonian.cycle[int(snake.pos[1]/30)][int(snake.pos[0]/30)]
                snake.move()
        else:
            main.aiMode = 0

class Main:
    running = True
    moveTimer = 1000
    
    #AI
    aiMode = 0
    board = []
    start = [0, 0]
    end = [0, 0]
    path = []
    
    def setupAStar(self):
        self.board = []
        for i in range(0, gridSize*30, 30):
            line = []
            for k in range(0, gridSize*30, 30):
                if [k, i] in snake.parts:
                    line.append(1)
                else:
                    line.append(0)
            line = line*1
            self.board.append(line)
        self.board[int(snake.pos[1]/30)][int(snake.pos[0]/30)] = 0
        self.start = [int(snake.pos[1]/30), int(snake.pos[0]/30)]
        self.end = [int(apple.apples[0][1]/30), int(apple.apples[0][0]/30)]
        self.path = astar(self.board, self.start, self.end)
    
    def __init__(self):
        apple.addApple()
    
    def eventHandler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_n:
                    self.aiMode = (self.aiMode + 1) % 3
        
        if self.aiMode == 0:
            keys=pg.key.get_pressed()
            if keys[pg.K_m]:
                apple.addApple()
            if keys[pg.K_w]:
                if snake.rot != 2:
                    snake.rot = 0
            elif keys[pg.K_d]:
                if snake.rot != 3:
                    snake.rot = 1
            elif keys[pg.K_s]:
                if snake.rot != 0:
                    snake.rot = 2
            elif keys[pg.K_a]:
                if snake.rot != 1:
                    snake.rot = 3
            elif keys[pg.K_SPACE]:
                apple.addApple()

    def tick(self):
        screen.fill(COLORS["black"])
        clock.tick(60)
        self.deltaTime = 1 / (clock.get_fps() + 0.01)
        
        if self.aiMode == 0:
            if self.moveTimer < 0:
                snake.move()
                self.moveTimer = 0.25
            self.moveTimer = self.moveTimer - self.deltaTime
        
        if self.aiMode != 0:
            runAi()
        
        self.eventHandler()
    
        snake.collision()
        apple.draw()
        snake.draw()
        
        for i in range(30, gridSize*30, 30):
            pg.draw.line(screen, COLORS["white"], (i, 0), (i, gridSize*30))
            pg.draw.line(screen, COLORS["white"], (0, i), (gridSize*30, i))
        
        font = pg.font.SysFont('didot.ttc', 50)
        img = font.render(str(snake.length), True, COLORS["white"])
        screen.blit(img, (0, 0))
    
        pg.display.flip()
        
snake = Snake()
apple = Apple()
main = Main()
hamiltonian = Hamiltonian()

while main.running:
    main.tick()