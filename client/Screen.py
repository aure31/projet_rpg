import pygame as p
from tile import *
from caracter import main_caractere

class Screen:
    def __init__(self, width, height,fps):
        p.init()
        p.font.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.coord:tuple[float] = (0,0)
        self.centerMap:tuple[int,int] = (map_size[0]/2,map_size[1]/2)
        self.FPS = fps
        flags = p.RESIZABLE
        #crée une fenetre de taille (900,500)px dont on peut modifier la taille
        self.WIN = p.display.set_mode((width, height),flags)
        self.BACKGROUND = (28, 22, 79)
        self.CENTER = p.Vector2(self.WIDTH/2, self.HEIGHT/2)
        self.show_map = map
        self.zoom = 1
        self.tile_size = tile_size

    def draw(self):
        self.WIN.fill(self.BACKGROUND)
        self.draw_map()

    def set_zoom(self,zoom:int):
        self.zoom = zoom
        self.tile_size = tile_size*zoom
        

    def draw_map(self):
        for x in range(map_size[0]):
            for y in range(map_size[1]):
                tile = map[x][y]
                self.WIN.blit(p.transform.scale(tile,self.tile_size),self.calc_map_coord(x,y))

    def set_coord(self, x:int, y:int):
        self.coord = (x,y)


    def calc_map_coord(self,x,y) -> tuple[int,int]:
        relativeX = (x - self.centerMap[0]) * self.tile_size + self.CENTER + main_caractere.
        relativeY = (y - self.centerMap[1]) * self.tile_size + self.CENTER
        return (relativeX , relativeY)
                

    def move(self, x:int, y:int):
        self.coord = (self.coord[0]+x , self.coord[1]+y)
        #print(self.coord)
    

s = Screen(900,500,30)