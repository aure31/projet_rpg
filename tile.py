import pygame as p
import os




tilePath = os.path.join("Assets","textures","tiles")
class tile(enumerate):
    Grass = p.image.load(tilePath+"/grass.png")
    Sand = p.image.load(tilePath+"/sand.png")
    Stone = p.image.load(tilePath+"/stone.png")


def load_map():
    return [[ tile.Grass for x in range(100)] for y in range(100)]

map = load_map()

def get_map_size():
    return (len(map) , len(map[0]))

map_size = get_map_size()
tile_size = tile.Grass.get_height()

dict = {1:tile.Grass, 2:tile.Sand, 3:tile.Stone}