from PIL import Image
import xlwings as xw
import numpy as np
import os
import time
from xlwings.utils import col_name

SIZE = (480, 360)
FPS = 12

lastFrame = time.time()
os.chdir("python/Apple/Frames")
frames = sorted(i if len(i) == 8 else "0" + i for i in os.listdir('.'))[1:]

book = xw.Book("/Users/askborgen/Desktop/code/python/Apple/Book2.xlsx")
sheet = book.sheets.active

def image_to_bw_np(image, threshold=150):
    img_gray = image.convert('L')
    img_gray_np = np.array(img_gray)
    img_bw_np = np.where(img_gray_np < threshold, 0, 1)
    #img_bw = Image.fromarray(img_bw_np.astype(np.uint8), 'L')
    return img_bw_np

def display(img, lastImg):
    for y in range(SIZE[1]):
        for x in range(SIZE[0]):
            if img[y][x] == lastImg[y][x]:
                continue
            sheet.range(col_name(x + 1) + str(y + 1)).color = (0, 0, 0) if img[y][x] == 0 else (255, 255, 255)
    
    sheet.api.Calculate()

lastImg = np.zeros(SIZE[::-1]) - 1
for frame in frames[::3]:
    img = Image.open(frame if frame[0] != "0" else frame[1:])
    img = image_to_bw_np(img)

    display(img, lastImg)
    lastImg = img

    #update()
    print(frame, 1 / (lastFrame - time.time()), "fps")
    lastFrame = time.time()