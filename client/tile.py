import pygame as p

map =[]

class tile(enumerate):
    Grass = p.image.load("client/assets/grass.png")
    Dirt = p.image.load("client/assets/dirt.png")
    Water = p.image.load("client/assets/water.png")


def load_map():
    map = [ tile.Grass for x in range(10) for y in range(10)]

load_map()

dict = {1:tile.Grass, 2:tile.Dirt, 3:tile.Water}

dict[1]
tile.mro

