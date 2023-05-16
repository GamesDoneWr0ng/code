import os
import xlwings as xw
from PIL import Image
import time
import numpy as np
import pandas as pd

SIZE = (480, 360)
FPS = 12

with open('/Users/askborgen/Desktop/code/python/Apple/base.html', 'r') as f:
    base = f.read()

lastFrame = time.time()
os.chdir("python/Apple/Frames")
frames = sorted(i if len(i) == 8 else "0" + i for i in os.listdir('.'))[1:]
wb = xw.Book("/Users/askborgen/Desktop/code/python/Apple/Book2.xlsm")
update = wb.macro("Update")
reSize = wb.macro("ReSize")
sheet = wb.sheets.active

reSize()

def image_to_bw_np(image, threshold=128):
    img_gray = image.convert('L')
    img_gray_np = np.array(img_gray)
    img_bw_np = np.where(img_gray_np < threshold, 0, 255)
    #img_bw = Image.fromarray(img_bw_np.astype(np.uint8), 'L')
    return img_bw_np

#@jit(parallel=True, forceobj=True)
def display(img, lastImg):
    for y in range(SIZE[1]):
        for x in range(SIZE[0]):
            if img[x][y] == lastImg[x][y]:
                continue
            img[x][y]

# animate
lastImg = np.zeros(SIZE[::-1]) - 1
for frame in frames[::3]:
    img = Image.open(frame if frame[0] != "0" else frame[1:])
    img = image_to_bw_np(img)

    display(img, lastImg)
    lastImg = img

    update()
    print(frame, 1 / (lastFrame - time.time()), "fps")
    lastFrame = time.time()