import numpy as np
import pygame as pg
pg.init()

class Sudoku:
    def __init__(self, size, methods: dict, board = np.array(())):
        if len(board) >0:
            self.board = board
        else:
            self.board = self.generate(methods)

        self.notes = np.zeros((9,9,9))
        self.notes[self.board == 0] = np.array([1,2,3,4,5,6,7,8,9])

        self.methods = methods
        self.size = size
        self.screen = pg.display.set_mode((self.size, self.size))

        self.solve()
        print(board)

    def generate(self, methods):
        board = np.zeros((9,9))
        for col in range(9):
            for row in range(9):
                board[col][row] = np.random.randint(1,10)
        return board

    def solve(self):
        while np.any(self.board == 0):
            for method, active in self.methods.items():
                if active:
                    self.board, self.notes, change = method(self.board, self.notes).solve()
                    if change:
                        break
            if not change:
                break

    def draw(self):
        pass