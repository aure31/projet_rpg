import pygame as p
import os




tilePath = os.path.join("Assets","textures","tiles")

class rotation:
    constant= 0
    _90 = 1
    _180 = 2
    _270 = 3

class tile:
    def __init__(self, img:p.Surface):
        self.img = img

    def set_rotation(self,rotation:int):
        self.img = p.transform.rotate(self.img,rotation*90)


Sand = tile(p.image.load(tilePath+"/sand.png"))
Stone = tile(p.image.load(tilePath+"/stone.png"))
Brick = tile(p.image.load(tilePath+"/brick.png"))

# All Grass Variants
Grass = tile(p.image.load(tilePath+"/grass.png"))
Grass2 = tile(p.image.load(tilePath+"/grass2.png"))
Grass3 = tile(p.image.load(tilePath+"/grass3.png"))
Grass_Stone = tile(p.image.load(tilePath+"/grass-stone.png"))
Grass_Sand = tile(p.image.load(tilePath+"/grass-sand.png"))
Grass_Sand_Ext_Corner = tile(p.image.load(tilePath+"/grass-sand-ext-corner.png"))
Grass_Sand_Int_Corner = tile(p.image.load(tilePath+"/grass-sand-int-corner.png"))
Grass_Stone_Ext_Corner = tile(p.image.load(tilePath+"/grass-stone-ext-corner.png"))
Grass_Stone_Int_Corner = tile(p.image.load(tilePath+"/grass-stone-int-corner.png"))

Grass_Brick_est = tile(p.image.load(tilePath+"/grass-brick-est.png"))
Grass_Brick_west = tile(p.image.load(tilePath+"/grass-brick-west.png"))
Grass_Brick_south = tile(p.image.load(tilePath+"/grass-brick-south.png"))
Grass_Brick_north = Grass_Brick_south.set_rotation(rotation._180)

Grass_Brick_ext_corner_west = tile(p.image.load(tilePath+"/grass-brick-ext-corner-west.png"))
Grass_Brick_ext_corner_est = tile(p.image.load(tilePath+"/grass-brick-ext-corner-est.png"))
Grass_Brick_int_corner_west = tile(p.image.load(tilePath+"/grass-brick-int-corner-west.png"))
Grass_Brick_int_corner_est = tile(p.image.load(tilePath+"/grass-brick-int-corner-est.png"))





def load_map():
    return [[ Grass for x in range(100)] for y in range(100)]

map = load_map()

def get_map_size():
    return (len(map) , len(map[0]))

map_size = get_map_size()
tile_size = Grass.img.get_height()
#est, west, south, north
# normal , int , ext
VarGrass = [Grass,Grass2,Grass3]
BrickGrass = [Grass_Brick_est,Grass_Brick_west,Grass_Brick_south,Grass_Brick_north]