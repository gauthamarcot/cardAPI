import os
import re
import io
import cv2
import json as js
import numpy as np
from PIL import Image as img
import pytesseract as pyte

def textextract(file):
    image = cv2.imread(file)
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    adap = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    imgfile = "{}.png".format(os.getpid())
    cv2.imwrite(imgfile, adap)
    text = pyte.image_to_string(img.open(imgfile), lang='eng')
    text_output = open('../output.txt', 'w', encoding='utf-8')
    text_output.write(text)
    print(text)