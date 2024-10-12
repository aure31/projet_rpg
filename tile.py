import pygame as p
import os




tilePath = os.path.join("Assets","textures","tiles")

class rotation:
    random = -1
    constant = 0
    _90 = 1
    _180 = 2
    _270 = 3

class tile:
    def __init__(self, img:p.Surface,rotation:int = 0):
        if rotation == -1:
            self.img = img
            self.randomRot = True
            return
        self.img = p.transform.rotate(img,rotation*90)
        self.randomRot = False

Grass = tile(p.image.load(tilePath+"/grass.png"),rotation.constant)
Sand = tile(p.image.load(tilePath+"/sand.png"),rotation.constant)
Stone = tile(p.image.load(tilePath+"/stone.png"),rotation.constant)
Brick = tile(p.image.load(tilePath+"/brick.png"),rotation.constant)
Grass2 = tile(p.image.load(tilePath+"/grass2.png"),rotation.constant)
Grass3 = tile(p.image.load(tilePath+"/grass3.png"),rotation.constant)
Grass_Stone = tile(p.image.load(tilePath+"/grass-stone.png"),rotation.constant)
Grass_Sand = tile(p.image.load(tilePath+"/grass-sand.png"),rotation.constant)





def load_map():
    return [[ Grass for x in range(100)] for y in range(100)]

map = load_map()

def get_map_size():
    return (len(map) , len(map[0]))

map_size = get_map_size()
tile_size = tile.Grass.get_height()

dict = [Grass, Sand, Stone, Brick]