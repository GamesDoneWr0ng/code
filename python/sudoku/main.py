"""
Takes args and comunicates between classes
"""
from methods.direct_sight import DirectSight
from methods.hidden_singles import HiddenSingles
from methods.last_posible_number import LastPosibleNumber
from methods.naked_candidates import NakedCandiadates
from sudoku import Sudoku
import numpy as np

#https://www.sudokuwiki.org/sudoku.htm
activeMethods = {
    DirectSight: True,
    HiddenSingles: True,
    LastPosibleNumber: True
}

board = np.array(
    [[0,0,0, 1,0,5, 0,9,0],
     [1,4,0, 0,0,0, 6,7,0],
     [0,8,0, 0,0,2, 4,0,0],
     
     [0,6,3, 0,7,0, 0,1,0],
     [9,0,0, 0,0,0, 0,0,3],
     [0,1,0, 0,9,0, 5,2,0],

     [0,0,7, 2,0,0, 0,8,0],
     [0,2,6, 0,0,0, 0,3,5],
     [0,0,0, 4,0,9, 0,6,0]])

class Main:
    """
    Main class
    """
    def __init__(self):
        self.sudoku = Sudoku(800, activeMethods, board)
        

main = Main()