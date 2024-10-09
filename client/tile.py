import pygame as p
import os

map =[]

tilePath = os.path.join("Assets","textures","tiles")
class tile(enumerate):
    Grass = p.image.load(tilePath+"/grass.png")
    Sand = p.image.load(tilePath+"/sand.png")
    Stone = p.image.load(tilePath+"/stone.png")


def load_map():
    global map
    map = [ tile.Grass for x in range(10) for y in range(10)]

load_map()

def get_map_size():
    return (len(map),len(map[0]))



dict = {1:tile.Grass, 2:tile.Sand, 3:tile.Stone}

