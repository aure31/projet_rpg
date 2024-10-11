import pygame as p
from tile import *
import anim as a
import os

class Screen:
    def __init__(self, width, height,fps):
        p.init()
        p.font.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.coord:tuple[float] = (0,0)
        self.FPS = fps
        flags = p.RESIZABLE
        #crée une fenetre de taille (900,500)px dont on peut modifier la taille
        self.WIN = p.display.set_mode((width, height),flags)
        self.BACKGROUND = (28, 22, 79)
        self.CENTER = p.Vector2(self.WIDTH/2, self.HEIGHT/2)
        self.map:Map = None
        self.zoom = 1

    def draw(self):
        self.WIN.fill(self.BACKGROUND)
        self.map.draw_map(self.WIN)

    def set_zoom(self,zoom:int):
        self.zoom = zoom
        self.map.tile_size = tile_size*zoom
        

    def set_coord(self, x:int, y:int):
        self.coord = (x,y)

    def move(self, x:int, y:int):
        self.coord = (self.coord[0]+x , self.coord[1]+y)
        #print(self.coord)
    
s = Screen(900,500,30)


class Caracter(a.anim_sprite):
    def __init__(self, speed, scale):
        
        img = p.image.load(os.path.join('Assets','textures','entities', 'player_sprites.png'))
        super().__init__(img, s.CENTER, scale , -1)
        self.speed = speed
        self.pressed = [False,False,False,False]
        self.relative = [0.5,0.5]

    def pressed_key(self, key, pressed):
        match key:
            case p.K_UP:
                self.pressed[0] = pressed
            case p.K_DOWN:
                self.pressed[1] = pressed
            case p.K_LEFT:
                self.pressed[2] = pressed
            case p.K_RIGHT:
                self.pressed[3] = pressed

    def move(self):
        if self.pressed[0]:
            print('up')
            self.cal_move(0,-self.speed)
        if self.pressed[1]:
            print('down')
            self.cal_move(0,self.speed)
        if self.pressed[2]:
            print('left')
            self.cal_move(-self.speed,0)
        if self.pressed[3]:
            print('right')
            self.cal_move(self.speed,0)
            

    def draw(self, win):
        super().draw(win)

    def cal_move(self,x,y):
        s.move(x,y)
        self.relative[0] =+ x
        self.relative[1] =+ y
        if self.relative[0] >= 1 :
            self.relative[0] -= 1
        if self.relative[1] >=1 :
            self.relative[1] -= 1

    def get_speed(self):
        return self.speed
    
    def set_speed(self, speed):
        self.speed = speed


main_caractere = Caracter(1.5,1.2)


class Map:

    def __init__(self):
        self.centerMap:tuple[int,int] = (map_size[0]/2,map_size[1]/2)
        self.tile_size = tile_size

    def calc_map_coord(self,x,y) -> tuple[int,int]:
        '''
        transforme la coordornée de la matrice en coordonée de l'écran
        '''
        relativeX = (x - self.centerMap[0]) * self.tile_size + main_caractere.relative[0] + (s.CENTER.x - self.tile_size/2)
        relativeY = (y - self.centerMap[1]) * self.tile_size + main_caractere.relative[1] + (s.CENTER.y - self.tile_size/2)

        return (relativeX,relativeY)
    
    def draw_map(self,win):
        for x in range(map_size[0]):
            for y in range(map_size[1]):
                tile = map[x][y]
                win.blit(p.transform.scale(tile,(self.tile_size,self.tile_size)),self.calc_map_coord(x,y)) 

s.map = Map()