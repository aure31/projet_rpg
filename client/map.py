from Screen import s
from caracter import main_caractere
from tile import *

class map:

    def __init__(self):
        self.centerMap:tuple[int,int] = (map_size[0]/2,map_size[1]/2)
        self.tile_size = tile_size

    def calc_map_coord(self,x,y) -> tuple[int,int]:
        relativeX = (x - self.centerMap[0]) * self.tile_size + main_caractere.relative[0]
        relativeY = (y - self.centerMap[1]) * self.tile_size + main_caractere.relative[0]
        return (relativeX , relativeY)