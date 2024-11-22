# converts a image to something desmos understands
import numpy as np
from scipy.signal import convolve2d
from PIL import Image
import matplotlib.pyplot as plt
import potrace

img_path = "/Users/askborgen/Desktop/code/website/desmosArt/images/pikachu.png"

def img_to_gradient(path):
    img = Image.open(path)
    data = np.array(img.getdata()).reshape(img.size[1], img.size[0], 3)
    data = np.sum(data, axis=2)/3
    kernel = np.array([[-3 -3j, 0-10j, + 3-3j],
                       [-10+0j, 0+ 0j, +10+0j],
                       [-3 +3j, 0+10j, + 3+3j]])
    gradient = convolve2d(data, kernel, boundary="symm", mode="same")
    return gradient

def png_to_svg(path):
    data = np.abs(img_to_gradient)
    bmp = potrace.Bitmap(data)
    print(bmp)

img_to_gradient(img_path)