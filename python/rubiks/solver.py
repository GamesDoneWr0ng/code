from cube import Cube

cross = {
    "u1": [],
    "u2": [["l", 1], ["d", 0], ["f", 1]],
    "u3": [["b", 1], ["d", 1], ["f", 1]],
    "u4": [["r", 1], ["d", 2], ["f", 1]],

    "u1r": [["f", 0], ["u", 2], ["r", 0], ["u", 0]],
    "u2r": [["l", 0], ["f", 0]],
    "u3r": [["b", 0], ["u", 0], ["l", 0], ["u", 2]],
    "u4r": [["r", 2], ["f", 2]],

    "m1": [["f", 0]],
    "m2": [["u", 0], ["l", 0], ["u", 2]],
    "m3": [["u", 1], ["b", 0], ["u", 1]],
    "m4": [["u", 2], ["r", 0], ["u", 0]],
    "m4r": [["f", 2]],
    "m1r": [["u", 0], ["l", 2], ["u", 2]],
    "m2r": [["u", 1], ["b", 2], ["u", 1]],
    "m3r": [["u", 2], ["r", 2], ["u", 0]],

    "b1": [["f", 1]],
    "b2": [["d", 0], ["f", 1]],
    "b3": [["d", 1], ["f", 1]],
    "b4": [["d", 2], ["f", 1]],

    "b1r": [["f", 0], ["u", 0], ["l", 2], ["u", 2]],
    "b2r": [["l", 2], ["f", 0], ["l", 0]],
    "b3r": [["d", 0], ["l", 2], ["f", 0], ["l", 0]],
    "b4r": [["r", 0], ["f", 2], ["r", 2]]
}

fix = {
    "": [],
    "c1": [["l", 2], ["u", 2], ["l", 0]],
    "c2": [["b", 2], ["u", 1], ["b", 0]],
    "c3": [["b", 0], ["u", 0], ["b", 2]],
    "e1": [["l", 2], ["u", 2], ["l", 0], ["u", 0]],
    "e2": [["b", 2], ["u", 0], ["b", 0], ["u", 2]],
    "e3": [["b", 0], ["u", 0], ["b", 2], ["u", 2]],
}

f2l = {
    "d1_m": [],
    "d1_mr": [["r", 0], ["u", 2], ["r", 2], ["u", 2], ["f", 2], ["u", 1], ["f", 0], ["u", 1], ["f", 2], ["u", 0], ["f", 0]],
    "d1_u1": [["u", 0], ["r", 0], ["u", 2], ["r", 2], ["u", 2], ["f", 2], ["u", 0], ["f", 0]],
    "d1_u2": [["r", 0], ["u", 2], ["r", 2], ["u", 2], ["f", 2], ["u", 0], ["f", 0]],
    "d1_u3": [["u", 2], ["f", 2], ["u", 0], ["f", 0], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "d1_u4": [["u", 1], ["f", 2], ["u", 0], ["f", 0], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "d1_u1r": [["u", 1], ["f", 2], ["u", 0], ["f", 0], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "d1_u2r": [["u", 0], ["f", 2], ["u", 0], ["f", 0], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "d1_u3r": [["f", 2], ["u", 0], ["f", 0], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "d1_u4r": [["u", 2], ["f", 2], ["u", 0], ["f", 0], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],

    "d2_m": [["r", 0], ["u", 2], ["r", 2], ["u", 2], ["r", 0], ["u", 0], ["r", 2], ["u", 1], ["r", 0], ["u", 2], ["r", 2]],
    "d2_mr": [["r", 0], ["u", 2], ["r", 2], ["u", 0], ["f", 2], ["u", 2], ["f", 0], ["u", 2], ["f", 2], ["u", 2], ["r", 0]],
    "d2_u1": [["u", 2], ["r", 0], ["u", 2], ["r", 2], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "d2_u2": [["u", 1], ["r", 0], ["u", 2], ["r", 2], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "d2_u3": [["u", 0], ["r", 0], ["u", 2], ["r", 2], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "d2_u4": [["r", 0], ["u", 2], ["r", 2], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "d2_u1r": [["f", 2], ["u", 2], ["f", 0], ["u", 0], ["f", 2], ["u", 2], ["f", 0]],
    "d2_u2r": [["u", 2], ["f", 2], ["u", 2], ["f", 0], ["u", 0], ["f", 2], ["u", 2], ["f", 0]],
    "d2_u3r": [["u", 1], ["f", 2], ["u", 2], ["f", 0], ["u", 0], ["f", 2], ["u", 2], ["f", 0]],
    "d2_u4r": [["u", 0], ["f", 2], ["u", 2], ["f", 0], ["u", 0], ["f", 2], ["u", 2], ["f", 0]],

    "d3_m": [["r", 0], ["u", 2], ["r", 2], ["u", 0], ["r", 0], ["u", 1], ["r", 2], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "d3_mr": [["r", 0], ["u", 2], ["r", 2], ["u", 1], ["f", 2], ["u", 2], ["f", 0], ["u", 2], ["f", 2], ["u", 0], ["f", 0]],
    "d3_u1": [["f", 2], ["u", 0], ["f", 0], ["u", 2], ["f", 2], ["u", 0], ["f", 0]],
    "d3_u2": [["u", 2], ["f", 2], ["u", 0], ["f", 0], ["u", 2], ["f", 2], ["u", 0], ["f", 0]],
    "d3_u3": [["u", 1], ["f", 2], ["u", 0], ["f", 0], ["u", 2], ["f", 2], ["u", 0], ["f", 0]],
    "d3_u4": [["u", 0], ["f", 2], ["u", 0], ["f", 0], ["u", 2], ["f", 2], ["u", 0], ["f", 0]],
    "d3_u1r": [["u", 2], ["r", 0], ["u", 0], ["r", 2], ["u", 2], ["r", 0], ["u", 0], ["r", 2]],
    "d3_u2r": [["u", 1], ["r", 0], ["u", 0], ["r", 2], ["u", 2], ["r", 0], ["u", 0], ["r", 2]],
    "d3_u3r": [["u", 0], ["r", 0], ["u", 0], ["r", 2], ["u", 2], ["r", 0], ["u", 0], ["r", 2]],
    "d3_u4r": [["r", 0], ["u", 0], ["r", 2], ["u", 2], ["r", 0], ["u", 0], ["r", 2]],

    "u1_m": [["r", 0], ["u", 0], ["r", 2], ["u", 2], ["r", 0], ["u", 0], ["r", 2], ["u", 2], ["r", 0], ["u", 0], ["r", 2]],
    "u1_mr": [["r", 0], ["u", 2], ["r", 2], ["f", 2], ["u", 1], ["f", 0]],
    "u1_u1": [["f", 2], ["u", 1], ["f", 0], ["u", 0], ["f", 2], ["u", 2], ["f", 0]],
    "u1_u2": [["u", 2], ["f", 2], ["u", 1], ["f", 0], ["u", 2], ["f", 2], ["u", 0], ["f", 0]],
    "u1_u3": [["u", 1], ["f", 2], ["u", 2], ["f", 0], ["u", 2], ["f", 2], ["u", 0], ["f", 0]],
    "u1_u4": [["u", 1], ["f", 1], ["u", 1], ["f", 0], ["u", 0], ["f", 2], ["u", 0], ["f", 1]],
    "u1_u1r": [["u", 1], ["r", 1], ["u", 1], ["r", 2], ["u", 2], ["r", 0], ["u", 2], ["r", 1]],
    "u1_u2r": [["u", 1], ["r", 0], ["u", 0], ["r", 2], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "u1_u3r": [["u", 0], ["r", 0], ["u", 1], ["r", 2], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "u1_u4r": [["r", 0], ["u", 1], ["r", 2], ["u", 2], ["r", 0], ["u", 0], ["r", 2]],

    "u2_m": [["u", 2], ["r", 0], ["u", 2], ["r", 2], ["u", 1], ["r", 0], ["u", 2], ["r", 2]],
    "u2_mr": [["u", 1], ["r", 0], ["u", 2], ["r", 2], ["u", 2], ["f", 2], ["u", 2], ["f", 0]],
    "u2_u1": [["u", 0], ["f", 2], ["u", 0], ["f", 0], ["u", 2], ["f", 2], ["u", 2], ["f", 0]],
    "u2_u2": [["f", 2], ["u", 2], ["f", 0]],
    "u2_u3": [["u", 0], ["f", 2], ["u", 2], ["f", 0], ["u", 2], ["f", 2], ["u", 2], ["f", 0]],
    "u2_u4": [["u", 2], ["r", 0], ["u", 1], ["r", 2], ["u", 0], ["f", 2], ["u", 2], ["f", 0]],
    "u2_u1r": [["r", 0], ["u", 0], ["r", 2], ["u", 1], ["r", 0], ["u", 2], ["r", 2], ["u", 0], ["r", 0], ["u", 2], ["r", 2]],
    "u2_u2r": [["u", 2], ["r", 0], ["u", 1], ["r", 2], ["u", 1], ["r", 0], ["u", 2], ["r", 2]],
    "u2_u3r": [["u", 2], ["r", 0], ["u", 0], ["r", 2], ["u", 1], ["r", 0], ["u", 2], ["r", 2]],
    "u2_u4r": [["u", 0], ["r", 0], ["u", 2], ["r", 2]],

    "u3_m": [["u", 2], ["r", 0], ["u", 1], ["r", 2], ["u", 0], ["r", 0], ["u", 0], ["r", 2]],
    "u3_mr": [["u", 1], ["f", 2], ["u", 0], ["f", 0], ["u", 0], ["r", 0], ["u", 0], ["r", 2]],
    "u3_u1": [["u", 2], ["f", 2], ["u", 0], ["f", 0]],
    "u3_u2": [["u", 0], ["f", 2], ["u", 2], ["f", 0], ["u", 1], ["f", 2], ["u", 0], ["f", 0]],
    "u3_u3": [["u", 0], ["f", 2], ["u", 1], ["f", 0], ["u", 1], ["f", 2], ["u", 0], ["f", 0]],
    "u3_u4": [["r", 0], ["u", 2], ["r", 2], ["u", 1], ["f", 2], ["u", 2], ["f", 0]],
    "u3_u1r": [["r", 2], ["u", 1], ["r", 1], ["u", 0], ["r", 1], ["u", 0], ["r", 0]],
    "u3_u2r": [["u", 2], ["r", 0], ["u", 0], ["r", 2], ["u", 0], ["r", 0], ["u", 0], ["r", 2]],
    "u3_u3r": [["r", 0], ["u", 0], ["r", 2]],
    "u3_u4r": [["u", 2], ["r", 0], ["u", 2], ["r", 2], ["u", 0], ["r", 0], ["u", 0], ["r", 2]]
}

class Solver:
    def phase_1(self, pieces: list) -> list:
        calcCube = Cube(pieces)
        moves = []
        relevant = [0,1,2,3]
        topPos = calcCube.pieces[8].pos

        #rotates the cube correctly
        do = []
        if topPos[2] == 1:
            do = ["x", 0]
        if topPos[0] == -1:
            do = ["x", 1]
        if topPos[2] == -1:
            do = ["x", 2]
        if topPos[1] == 1:
            do = ["z", 2]
        if topPos[1] == -1:
            do = ["z", 0]
        if len(do) != 0:
            moves.append(do)
            calcCube.rotate(do[0], do[1])

        count = -1
        while calcCube.pieces[9].pos[1] != 1:
            calcCube.rotate("y", 0)
            count += 1
        moves.append(["y", count])

        for i in [2,0,3,1]:
            piece = calcCube.pieces[i]
            move = ""
            if piece.pos[0] == 1:
                    move = move + "u"
            elif piece.pos[0] == 0:
                move = move + "m"
            else:
                move = move + "b"

            if piece.pos[0] != 0:
                if piece.pos[2] == 1:
                    move = move + "1"
                elif piece.pos[1] == -1:
                    move = move + "2"
                elif piece.pos[2] == -1:
                    move = move + "3"
                else:
                    move = move + "4"
                if piece.rotation[0] != "u" and piece.rotation[0] != "d":
                        move = move + "r"
            else:
                if piece.pos[1:3] == [-1, 1]:
                    move = move + "1"
                    if piece.rotation[0] == "f":
                        move = move + "r"
                elif piece.pos[1:3] == [-1, -1]:
                    move = move + "2"
                    if piece.rotation[0] == "l":
                        move = move + "r"
                elif piece.pos[1:3] == [1, -1]:
                    move = move + "3"
                    if piece.rotation[0] == "b":
                        move = move + "r"
                else:
                    move = move + "4"
                    if piece.rotation[0] == "r":
                        move = move + "r"
            
            for k in cross[move]:
                moves.append(k)
                calcCube.rotate(k[0], k[1])
            moves.append(["y", 0])
            calcCube.rotate("y", 0)

        return moves

    def phase_2(self, pieces: list) -> list:
        calcCube = Cube(pieces)
        moves = []

        moves.append(["z", 1])
        moves.append(["y", 2])
        calcCube.rotate("z", 1)
        calcCube.rotate("y", 2)

        for i in [[4,13,9],[5,14,10],[6,15,11],[7,16,12]]:
            corner = calcCube.pieces[i[0]]
            edge = calcCube.pieces[i[1]]
            move = ""

            fixMove = ""
            if corner.pos == [-1, -1, 1]:
                fixMove = "c1"
            elif corner.pos == [-1, -1, -1]:
                fixMove = "c2"
            elif corner.pos == [-1, 1, -1]:
                fixMove = "c3"
            elif corner.pos[0] == 1:
                count = -1
                while corner.pos != [1, 1, 1]:
                    calcCube.rotate("u", 0)
                    count += 1
                moves.append(["u", count])

            for k in fix[fixMove]:
                moves.append(k)
                calcCube.rotate(k[0], k[1])

            fixMove = ""
            if edge.pos == [0, -1, 1]:
                fixMove = "e1"
            elif edge.pos == [0, -1, -1]:
                fixMove = "e2"
            elif edge.pos == [0, 1, -1]:
                fixMove = "e3"
            
            for k in fix[fixMove]:
                moves.append(k)
                calcCube.rotate(k[0], k[1])

            if corner.pos[0] == -1:
                move = move + "d"
            else:
                move = move + "u"
            if corner.rotation[0] == "u" or corner.rotation[0] == "d":
                move = move + "1_"
            elif corner.rotation[0] == "f":
                move = move + "2_"
            else:
                move = move + "3_"
            
            if calcCube.pieces[i[2]].colors[1] == " ":
                middlecolor = calcCube.pieces[i[2]].colors[2]
            else:
                middlecolor = calcCube.pieces[i[2]].colors[1]
                
            if edge.pos[0] == 0:
                move = move + "m"
                if edge.rotation[0] == "f" and edge.colors[1] == middlecolor or edge.rotation[0] == "r" and edge.colors[2] == middlecolor:
                    move = move + "r"
            else:
                move = move + "u"
                if edge.pos[2] == 1:
                    move = move + "1"
                elif edge.pos[1] == -1:
                    move = move + "2"
                elif edge.pos[2] == -1:
                    move = move + "3"
                else:
                    move = move + "4"
                if edge.rotation[0] == "u" and edge.colors[2] == middlecolor or edge.rotation[1] == "u" and edge.colors[1] == middlecolor:
                    move = move + "r"
            
            for k in f2l[move]:
                moves.append(k)
                calcCube.rotate(k[0], k[1])
            moves.append(["y", 0])
            calcCube.rotate("y", 0)
        
        return moves

    def phase_3(self):
        return

    def phase_4(self):
        return