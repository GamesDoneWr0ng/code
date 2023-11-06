"""
Takes args and comunicates between classes
"""
import methods
from sudoku import Sudoku

#https://www.sudokuwiki.org/sudoku.htm
activeMethods = {
    methods.hidden_singles: True
}

class Main:
    """
    Main class
    """
    def __init__(self):
        self.sudoku = Sudoku(800, activeMethods)