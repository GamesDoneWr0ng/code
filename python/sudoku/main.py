"""
Takes args and comunicates between classes
"""
from methods.direct_sight import DirectSight
from methods.hidden_singles import HiddenSingles
from methods.last_posible_number import LastPosibleNumber
from methods.naked_candidates import NakedCandidates
from methods.hidden_candidates import HiddenCandidates
from methods.intersection_removal import IntersectionRemoval

from sudoku import Sudoku
import numpy as np

#https://www.sudokuwiki.org/sudoku.htm
activeMethods = {
    DirectSight: True,
    HiddenSingles: True,
    LastPosibleNumber: True,
    NakedCandidates: False,
    HiddenCandidates: False,
    IntersectionRemoval: True
}

board = np.array(
    [[0,1,7, 9,0,3, 6,0,0],
     [0,0,0, 0,8,0, 0,0,0],
     [9,0,0, 0,0,0, 5,0,7],

     [0,7,2, 0,1,0, 4,3,0],
     [0,0,0, 4,0,2, 0,7,0],
     [0,6,4, 3,7,0, 2,5,0],

     [7,0,1, 0,0,0, 0,6,5],
     [0,0,0, 0,3,0, 0,0,0],
     [0,0,5, 6,0,1, 7,2,0]])

class Main:
    """
    Main class
    """
    def __init__(self):
        self.sudoku = Sudoku(700, activeMethods, board, 1000)

main = Main()