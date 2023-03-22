import openpyxl
import os
import sys

os.chdir("python/Apple/Frames")
frames = os.listdir('.')
wb = openpyxl.load_workbook("/Users/askborgen/Desktop/Ukeplan.xlsm")
sheet = wb.active.title
if sheet != "Apple":
    sys.exit()


