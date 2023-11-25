import numpy as np
import pygame as pg
from time import time_ns

pg.init()


class Sudoku:
    def __init__(self, size, methods: dict, board = np.array(()), delay = 1000):
        self.methods = methods # methods the solver and generator can use
        self.size = size # size of screen
        self.screen = pg.display.set_mode((self.size, self.size)) # screen for drawing
        self.delay = delay # delay for draw after each move

        if len(board) >0:
            self.board = board # set board if given
        else:
            self.board = self.generate(methods) # generate a new board if not

        self.notes = np.zeros((9,9,9), dtype=np.int8) # make the notes
        self.notes[self.board == 0] = np.array([1,2,3,4,5,6,7,8,9]) # all numbers can go in all slots, when there is a number on a board the notes for that cell will be empty

        self.solve() # solve the board
        print(self.board) # print the board
        pg.time.delay(10000)

    def generate(self, methods):
        board = np.zeros((9,9), dtype=np.int8)
        for col in range(9):
            for row in range(9):
                board[col][row] = np.random.randint(1,10)
        return board

    def solve(self):
        while np.any(self.board == 0):
            for method, active in self.methods.items():
                if active:
                    start = time_ns()
                    self.board, self.notes, change = method(self.board, self.notes).solve()
                    print(f"{method.__name__:<19}: {(time_ns() - start) / 1e+9:<8}s  Change: {change}")

                    if change:
                        break

            self.draw()
            pg.time.delay(self.delay)

            if not change:
                break

    def draw(self):
        self.screen.fill((255, 255, 255))
        # Draw the grid
        for i in range(10):
            pg.draw.line(self.screen, (0, 0, 0), (0, i * self.size // 9), (self.size, i * self.size // 9), 3 if i%3 == 0 else 1)
            pg.draw.line(self.screen, (0, 0, 0), (i * self.size // 9, 0), (i * self.size // 9, self.size), 3 if i%3 == 0 else 1)

        # Draw the numbers
        font = pg.font.Font(None, self.size // 15)
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    text = font.render(str(self.board[i][j]), True, (0, 0, 0))
                    self.screen.blit(text, (j * self.size // 9 + self.size // 27, i * self.size // 9 + self.size // 27))
                else:
                    # Draw the notes
                    note_font = pg.font.Font(None, self.size // 27)
                    for k in range(9):
                        if self.notes[i][j][k] != 0:
                            note_text = note_font.render(str(k + 1), True, (0, 0, 0))
                            self.screen.blit(note_text, (j * self.size // 9 + (k % 3) * self.size // 27 + 5, i * self.size // 9 + (k // 3) * self.size // 27 + 5))

        # Update the display
        pg.display.update()
