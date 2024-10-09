import pygame as p
import os

map =[]

tilePath = os.path.join("Assets","tiles")
class tile(enumerate):
    Grass = p.image.load(tilePath+"/texturregrass.png")
    Dirt = p.image.load(tilePath+"/dirt.png")
    Water = p.image.load(tilePath+"/water.png")


def load_map():
    map = [ tile.Grass for x in range(10) for y in range(10)]

load_map()

dict = {1:tile.Grass, 2:tile.Dirt, 3:tile.Water}

dict[1]
tile.mro

