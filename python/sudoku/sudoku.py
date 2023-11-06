import numpy as np
import pygame as pg
pg.init()

class Sudoku:
    def __init__(self, size, methods: dict, difficulty = 0, board = None):
        if board:
            self.board = board
        else:
            self.board = self.generate(difficulty)
        self.notes = np.zeros((9,9,9))

        for col in self.board:
            for row in self.board[col]:
                if self.board[col][row] == 0:
                    self.notes[col][row] = np.array([1,2,3,4,5,6,7,8,9])

        self.methods = methods
        self.size = size
        self.screen = pg.display.set_mode((self.size, self.size))

    def generate(self):
        board = np.zeros((9,9))
        for col in board:
            for row in board[col]:
                board[col][row] = np.random.randint(1,10)
        return board
    
    def getCol(self, idx):
        return self.board[idx]
    
    def getRow(self, idx):
        return self.board[:,idx]
    
    def getBox(self, idx):
        return self.board[3*(idx//3):3*(idx//3)+3, 3*(idx%3):3*(idx%3)+3]

    def solve(self):
        for method, active in self.methods.items():
            if active:
                self.board, change = method(self.board)
                if change:
                    break

    def draw(self):
        pass