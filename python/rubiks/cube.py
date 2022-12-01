from piece import Piece
from itertools import combinations

BELTS = {
    "u": ["r","f","l","b"],
    "d": ["r","b","l","f"],
    "r": ["u","b","d","f"],
    "l": ["u","f","d","b"],
    "f": ["u","r","d","l"],
    "b": ["u","l","d","r"],
    "y": ["r","f","l","b"],
    "x": ["u","b","d","f"],
    "z": ["u","r","d","l"]
}

class Cube:
    def __init__(self, pieces = []):
        if len(pieces) == 0:
            self.pieces = []
            colors = list(combinations(" bgro",2))
            colors.remove(("b", "g"))
            colors.remove(("r", "o"))
            colors.append((" ", " "))
            colors[0] = colors[0][::-1]
            colors[1] = colors[1][::-1]
            for i in ["w", " ", "y"]:
                for k in colors:
                    if [i, k[0], k[1]] == [" ", " ", " "]:
                        continue
                    self.pieces.append(Piece([i, k[0], k[1]]))
        else:
            self.pieces = pieces

    def rotate(self, side, direction):
        #for rotation first get all pieces on the side you want to rotate
        #then multiply the positions of those pieces with 1, 0 or -1 depending on the way you rotate it
        for i in self.pieces:
            if side in i.rotation:
                if side == "u" or side == "d":
                    if direction == 0:
                        i.pos = [i.pos[0], -i.pos[2], i.pos[1]]
                    if direction == 1:
                        i.pos = [i.pos[0], -i.pos[1], -i.pos[2]]
                    if direction == 2:
                        i.pos = [i.pos[0], i.pos[2], -i.pos[1]]
                if side == "r" or side == "l":
                    if direction == 0:
                        i.pos = [i.pos[2], i.pos[1], -i.pos[0]]
                    if direction == 1:
                        i.pos = [-i.pos[0], i.pos[1], -i.pos[2]]
                    if direction == 2:
                        i.pos = [-i.pos[2], i.pos[1], i.pos[0]]
                if side == "f" or side == "b":
                    if direction == 0:
                        i.pos = [-i.pos[1], i.pos[0], i.pos[2]]
                    if direction == 1:
                        i.pos = [-i.pos[0], -i.pos[1], i.pos[2]]
                    if direction == 2:
                        i.pos = [i.pos[1], -i.pos[0], i.pos[2]]
                if direction != 1:
                    if side == "d":
                        i.pos = [i.pos[0], -i.pos[1], -i.pos[2]]
                    if side == "l":
                        i.pos = [-i.pos[0], i.pos[1], -i.pos[2]]
                    if side == "b":
                        i.pos = [-i.pos[0], -i.pos[1], i.pos[2]]
                
                belt = BELTS[side]
                for index, k in enumerate(i.rotation):
                    if k != side:
                        i.rotation[index] = belt[(belt.index(k) + direction + 1) % 4]
            
            elif side == "x" or side == "y" or side == "z":
                if side == "y":
                    if direction == 0:
                        i.pos = [i.pos[0], -i.pos[2], i.pos[1]]
                    if direction == 1:
                        i.pos = [i.pos[0], -i.pos[1], -i.pos[2]]
                    if direction == 2:
                        i.pos = [i.pos[0], i.pos[2], -i.pos[1]]
                if side == "x":
                    if direction == 0:
                        i.pos = [i.pos[2], i.pos[1], -i.pos[0]]
                    if direction == 1:
                        i.pos = [-i.pos[0], i.pos[1], -i.pos[2]]
                    if direction == 2:
                        i.pos = [-i.pos[2], i.pos[1], i.pos[0]]
                if side == "z":
                    if direction == 0:
                        i.pos = [-i.pos[1], i.pos[0], i.pos[2]]
                    if direction == 1:
                        i.pos = [-i.pos[0], -i.pos[1], i.pos[2]]
                    if direction == 2:
                        i.pos = [i.pos[1], -i.pos[0], i.pos[2]]
                
                side2 = {"y": ["u", "d"], "x": ["r", "l"], "z": ["f", "b"]}
                belt = BELTS[side]
                for index, k in enumerate(i.rotation):
                    if k != side and not k in side2[side]:
                        i.rotation[index] = belt[(belt.index(k) + direction + 1) % 4]