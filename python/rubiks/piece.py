class Piece:
    def __eq__(self, other: object) -> bool:
        return self.pos == other.pos and self.rotation == other.rotation and self.colors == other.colors

    def __init__(self, colors: list):
        self.points = []
        self.points2d = []
        self.colors = colors

        self.pos = [0,0,0]
        if colors[0] == "w":
            self.pos[0] = 1
        elif colors[0] == "y":
            self.pos[0] = -1
        else:
            self.pos[0] = 0
        if colors[1] == "b":
            self.pos[1] = 1
        elif colors[1] == "g":
            self.pos[1] = -1
        else:
            self.pos[1] = 0
        if colors[2] == "r":
            self.pos[2] = 1
        elif colors[2] == "o":
            self.pos[2] = -1
        else:
            self.pos[2] = 0
        
        self.rotation = []
        for i in colors:
            if i == "w":
                self.rotation.append("u")
            if i == "y":
                self.rotation.append("d")
            if i == "b":
                self.rotation.append("r")
            if i == "g":
                self.rotation.append("l")
            if i == "r":
                self.rotation.append("f")
            if i == "o":
                self.rotation.append("b")
        
        #pos = [up/white, rigth/blue, front/red
        #rotation = [direction of first color, direction of second color, direction of third color]
