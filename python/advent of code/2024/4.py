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
    for slice in [arr[y,x:x+4], # horizontal right
                  arr[y:y+4,x], # vertical down
                  arr[y,x:x-4 if x-4>=0 else None:-1], # horizontal left
                  arr[y:y-4 if y-4>=0 else None:-1,x], # vertical up

                  np.diagonal(arr[y:y+4, x:x+4]), # diagonal down right
                  np.diagonal(arr[y:y-4 if y-4>=0 else None:-1, x:x+4]), # diagonal up right
                  np.diagonal(arr[y:y+4, x:x-4 if x-4>=0 else None:-1]), # diagonal down left
                  np.diagonal(arr[y:y-4 if y-4>=0 else None:-1, x:x-4 if x-4>=0 else None:-1]) # diagonal up left
                  ]:
        if slice.size != 4:
            continue
        if np.all(slice == XMAS):
            count += 1
print(count)

count = 0
y,x = np.where(arr=="A")
for y,x in zip(y,x):
    slice = arr[y-1 if y-1>=0 else None:y+2, x-1 if x-1>=0 else None:x+2]
    if slice.size != 9:
        continue
    if slice[0,0] in {"M", "S"} and \
       slice[0,2] in {"M", "S"} and \
       slice[2,0] in {"M", "S"} and \
       slice[2,2] in {"M", "S"} and \
       slice[0,0] != slice[2,2] and \
       slice[0,2] != slice[2,0]:
        count += 1
        
print(count)