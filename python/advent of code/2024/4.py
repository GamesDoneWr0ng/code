import numpy as np

data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
XMAS = np.array([i for i in "XMAS"])
arr = np.array([[letter for letter in row] for row in data.split("\n")])

count = 0
y,x = np.where(arr == "X")
for y,x in zip(y,x):
    if np.all(arr[y,x:x+4] == XMAS): # horizontal right
        count += 1