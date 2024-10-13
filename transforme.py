import os
from PIL import Image
from tile import *

def encode(path):
    img = Image.open(path)
    data = img.getdata()
    result = []
    width , height = img.size
    for y in range(height):
        for x in range(width):
            indexs = (y * width + x ,(y +1) * width+x,y * width + x +1,y * width + x -1,(y -1) * width + x) #indexs[center,upper,right,left,lower]->
            current = []
            for i in indexs:
                if i < 0 or i >= len(data):
                    current.append(None)
                    continue
                pxcolor = data[i]
                if pxcolor[0] == 255 and pxcolor[1] == 255 and pxcolor[2] == 0:
                    current.append("Sand")
                    continue
                if pxcolor[0] == 153 and pxcolor[1] == 153 and pxcolor[2] == 153:
                    current.append(Sand)
                    continue
            
