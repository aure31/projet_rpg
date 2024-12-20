import os
import csv
from PIL import Image
from tile import *

def list_to_csv(l,width):
    # utilise des ',' comme séparateurs
    with open('map.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Initialiser une ligne vide
        row = []
        
        for element in l:
            if element != None:
                row.append(element)
            # Si la largeur est atteinte, écrire la ligne et réinitialiser
            if len(row) == width:
                writer.writerow(row)
                row = []  # Réinitialiser la ligne
        
        # Écrire la dernière ligne si elle n'est pas vide
        if row:
            writer.writerow(row)


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

dict_condition = { '["Grass","Grass","Grass","Grass","Grass","Grass","Grass","Grass","Grass"]' : Grass,
                  '["Brick","Brick","Brick","Grass","Grass","Grass","Grass","Grass","Grass"]' : Grass_Brick_north,
                   '["Grass","Grass","Grass","Grass","Grass","Grass","Brick","Brick","Brick"]' : Grass_Brick_south,
                   '["Grass","Grass","Brick","Grass","Grass","Brick","Grass","Grass","Brick"]' : Grass_Brick_west,
                   '["Brick","Grass","Grass","Brick","Grass","Grass","Brick","Grass","Grass"]' : Grass_Brick_est,
                   '["Brick","Brick","Brick","Grass","Grass","Brick","Grass","Grass","Brick"]' : Grass_Brick_int_corner_west,
                   '["Brick","Brick","Brick","Brick","Grass","Grass","Brick","Grass","Grass"]' : Grass_Brick_int_corner_est,
                   '["Grass","Grass","Brick","Grass","Grass","Brick","Brick","Brick","Brick"]' : Grass_Brick_int_corner_west.set_rotation(rotation._180),
                   '["Brick","Grass","Grass","Brick","Grass","Grass","Brick","Brick","Brick"]' : Grass_Brick_int_corner_est.set_rotation(rotation._180),
                   '["Grass","Grass","Brick","Grass","Grass","Grass","Grass","Grass","Grass"]' : Grass_Brick_ext_corner_west,
                   '["Brick","Grass","Grass","Grass","Grass","Grass","Grass","Grass","Grass"]' : Grass_Brick_ext_corner_est,
                   '["Grass","Grass","Grass","Grass","Grass","Grass","Brick","Grass","Grass"]' : Grass_Brick_ext_corner_west.set_rotation(rotation._180),
                   '["Grass","Grass","Grass","Grass","Grass","Grass","Grass","Grass","Brick"]' : Grass_Brick_ext_corner_est.set_rotation(rotation._180),
                   '["Grass","Grass","Grass","Grass","Grass","Grass","Stone","Stone","Stone"]' : Grass_Stone.set_rotation(rotation._90),
                   '["Grass","Grass","Stone","Grass","Grass","Stone","Grass","Grass","Stone"]' : Grass_Stone.set_rotation(rotation._180),
                   '["Stone","Grass","Grass","Stone","Grass","Grass","Stone","Grass","Grass"]' : Grass_Stone,
                   '["Stone","Stone","Stone","Grass","Grass","Grass","Grass","Grass","Grass"]' : Grass_Stone.set_rotation(rotation._270),
                   '["Grass","Grass","Grass","Grass","Grass","Grass","Grass","Grass","Stone"]' : Grass_Stone_Ext_Corner,
                   '["Grass","Grass","Grass","Grass","Grass","Grass","Stone","Grass","Grass"]' : Grass_Stone_Ext_Corner.set_rotation(rotation._90),
                   '["Stone","Grass","Grass","Grass","Grass","Grass","Grass","Grass","Grass"]' : Grass_Stone_Ext_Corner.set_rotation(rotation._180),
                   '["Grass","Stone","Grass","Grass","Grass","Stone","Grass","Grass","Grass"]' : Grass_Stone_Ext_Corner.set_rotation(rotation._270),
                   '["Grass","Grass","Stone","Grass","Grass","Stone","Stone","Stone","Stone"]' : Grass_Stone_Int_Corner,
                   '["Stone","Grass","Grass","Stone","Grass","Grass","Stone","Stone","Stone"]' : Grass_Stone_Int_Corner.set_rotation(rotation._90),
                   '["Stone","Stone","Stone","Grass","Grass","Stone","Grass","Grass","Stone"]' : Grass_Stone_Int_Corner.set_rotation(rotation._180),
                   '["Stone","Stone","Stone","Stone","Grass","Grass","Stone","Grass","Grass"]' : Grass_Stone_Int_Corner.set_rotation(rotation._270),
                   '["Grass","Grass","Grass","Grass","Grass","Grass","Sand","Sand","Sand"]' : Grass_Sand.set_rotation(rotation._90),
                   '["Grass","Grass","Sand","Grass","Grass","Sand","Grass","Grass","Sand"]' : Grass_Sand,
                   '["Sand","Grass","Grass","Sand","Grass","Grass","Sand","Grass","Grass"]' : Grass_Sand.set_rotation(rotation._180),
                   '["Sand","Sand","Sand","Grass","Grass","Grass","Grass","Grass","Grass"]' : Grass_Sand.set_rotation(rotation._270),
                   '["Grass","Grass","Grass","Grass","Grass","Grass","Grass","Grass","Sand"]' : Grass_Sand_Ext_Corner,
                   '["Grass","Grass","Grass","Grass","Grass","Grass","Sand","Grass","Grass"]' : Grass_Sand_Ext_Corner.set_rotation(rotation._90),
                   '["Sand","Grass","Grass","Grass","Grass","Grass","Grass","Grass","Grass"]' : Grass_Sand_Ext_Corner.set_rotation(rotation._180),
                   '["Grass","Grass","Sand","Grass","Grass","Grass","Grass","Grass","Grass"]' : Grass_Sand_Ext_Corner.set_rotation(rotation._270),
                   '["Grass","Grass","Sand","Grass","Grass","Sand","Sand","Sand","Sand"]' : Grass_Sand_Int_Corner,
                   '["Sand","Grass","Grass","Sand","Grass","Grass","Sand","Sand","Sand"]' : Grass_Sand_Int_Corner.set_rotation(rotation._90),
                   '["Sand","Sand","Sand","Grass","Grass","Sand","Grass","Grass","Sand"]' : Grass_Sand_Int_Corner.set_rotation(rotation._180),
                   '["Sand","Sand","Sand","Sand","Grass","Grass","Sand","Grass","Grass"]' : Grass_Sand_Int_Corner.set_rotation(rotation._270),
                   }
        
def tile_condition(current):
    for e in dict_condition.keys():
        if current == eval(e):
            return dict_condition[e]
    return None

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
        # result.append([])
        for x in range(width):
            indexs:list[list] =[]
            # => [[tl,t,tr],[l,c,r],[dl,d,dr]]
            if tileMap[y*width + x] != "Grass" :
                center = tileMap[y*width + x]
                if center == "Sand":
                    result.append(Sand)
                elif center == "Stone":
                    result.append(Stone)
                elif center == "Brick":
                    result.append(Brick)  
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

                    tile = tileMap[i]
                    current.append(tile)

            result.append(tile_condition(current))
            # print(f"{current}")
            # print(tileMap[i])
    list_to_csv(result,width)
    return result
            


# encode("Assets\map.png")
# print("all good ")