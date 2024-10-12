import os
from PIL import Image
from tile import *

def encode(path, scale):
    img = Image.open(path)
    data = img.getdata()
    result = []
    width , height = img.size
    for y in range(height):
        for x in range(width):
            indexs = (y * width + x ,(y +1) * width+x,y * width + x +1,y * width + x -1,(y -1) * width + x)
            current = []
            for i in indexs:
                if i < 0 or i >= len(data):
                    current.append(None)
                    continue
                tempData = data[i]
                if tempData[0] == 255 and tempData[1] == 253 and tempData[2] == 0:
                    current.append(None)
                    continue
                
            
