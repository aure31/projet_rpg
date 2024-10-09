import pygame as p
from tile import *

class Screen:
    def __init__(self, width, height,fps):
        p.init()
        p.font.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.coord:tuple[float] = (0,0)
        self.mapCoord:tuple[int] = (get_map_size()[0]/2,get_map_size()/2[1])
        self.FPS = fps
        flags = p.RESIZABLE
        #crée une fenetre de taille (900,500)px dont on peut modifier la taille
        self.WIN = p.display.set_mode((width, height),flags)
        self.BACKGROUND = (28, 22, 79)
        self.CENTER = p.Vector2(self.WIDTH/2, self.HEIGHT/2)

        self.show_map = map

    def draw(self):
        self.WIN.fill(self.BACKGROUND)
        self.draw_map()

    def draw_map(self):
        for x in range(10):
            for y in range(10):
                img = map[x+y*10]
                win.blit(p.transform.scale(img,(img.get_width()*Scale,img.  get_height()*Scale)),(x*50*Scale,y*50*Scale))

    def set_coord(self, x:int, y:int):
        self.coord = (x,y)


    def calc_map_coord(self):
        tempMap = self.mapCoord
        for x in range(10):
            for y in range(10):
                if self.coord[0] > x*50*Scale and self.coord[0] < (x+1)*50*Scale:
                    tempMap[0] = x
                if self.coord[1] > y*50*Scale and self.coord[1] < (y+1)*50*Scale:
                    tempMap[1] = y

    def move(self, x:int, y:int):
        self.coord = (self.coord[0]+x , self.coord[1]+y)
        #print(self.coord)
    

s = Screen(900,500,30)