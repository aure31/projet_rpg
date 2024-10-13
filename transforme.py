import os
from PIL import Image
from tile import *

def closest_color(pixel):
    # Définir les couleurs cibles
    colors = {
        "yellow": (255, 255, 0),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255)
    }
    
    # Calculer la distance euclidienne pour trouver la couleur la plus proche
    closest_name = None
    closest_distance = float('inf')

    for color_name, color_value in colors.items():
        distance = sum((p - c) ** 2 for p, c in zip(pixel, color_value)) ** 0.5
        if distance < closest_distance:
            closest_distance = distance
            closest_name = color_name

    return colors[closest_name]

def transform_colors(pixel_list):
    # Transformer les couleurs de la liste de tuples
    transformed_list = [closest_color(pixel) for pixel in pixel_list]
    return transformed_list


def encode(path):
    img = Image.open(path)
    data = transform_colors(img.getdata())
    result = []
    tileMap = []
    width , height = img.size
    for y in range(height):
        for x in range(width):
            # => [[tl,t,tr],[l,c,r],[dl,d,dr]]
            pxcolor = data[y * width + x]
            # print(f"[{pxcolor[0]},{pxcolor[1]},{pxcolor[2]}]")
            if pxcolor[0] == 0 and pxcolor[1] == 255 and pxcolor[2] == 0:
                tileMap.append("Grass")
            elif pxcolor[0] == 0 and pxcolor[1] == 0 and pxcolor[2] == 255:
                tileMap.append("Stone")
            elif pxcolor[0] == 255 and pxcolor[1] == 255 and pxcolor[2] == 0:
                tileMap.append("Sand")
            elif pxcolor[0] == 255 and pxcolor[1] == 0 and pxcolor[2] == 0:
                tileMap.append("Bricks")
            else:
                tileMap.append("not bound")

    for y in range(height):
        for x in range(width):
            indexs:list[list] =[]
            # => [[tl,t,tr],[l,c,r],[dl,d,dr]]
            for y_indice in range(-1,2):
                indexs.append([])
                for x_indice in range(-1,2):
                    if y+y_indice<0 or x+x_indice<0 or y+y_indice>=height or x+x_indice>=width:
                        indexs[y_indice+1].append(-1)
                        continue
                    indexs[y_indice+1].append((y+y_indice) * width + x+x_indice)

            current = []
            for j in indexs:
                for i in j :
                    if i < 0 or i >= len(data):
                        current.append(None)
                        continue

                    tile = data[i]
            
            print(f"{current}")
            




encode("Assets\map.png")