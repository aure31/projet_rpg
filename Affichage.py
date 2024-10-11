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
        self.coord:tuple[int] = (0,0)
        self.FPS = fps
        flags = p.RESIZABLE
        #crée une fenetre de taille (900,500)px dont on peut modifier la taille
        self.WIN = p.display.set_mode((width, height),flags)
        self.BACKGROUND = (28, 22, 79)
        self.CENTER = p.Vector2(self.WIDTH/2, self.HEIGHT/2)
        self.map:Map = None
        self.zoom = 1
        p.display.set_icon(p.image.load(os.path.join('Assets','logo.png')))
        self.relative = [0.5,0.5]

    def draw(self):
        self.WIN.fill(self.BACKGROUND)
        self.map.draw_map(self.WIN)

    def set_zoom(self,zoom:int):
        self.zoom = zoom
        self.map.tile_size = tile_size*zoom
        

    def set_coord(self, x:int, y:int):
        self.coord = (x,y)

    def move(self, x:int, y:int):
        print(self.coord,self.relative)
        print(x,y)
        self.relative[0] += x/self.map.tile_size
        self.relative[1] += y/self.map.tile_size
        print(self.coord,self.relative)
        rx, ry = self.coord
        if self.relative[0] > 1.0:
            print('1')
            self.relative[0] -= 1
            rx -=1
        if self.relative[0] < 0.0 :
            print('3')
            self.relative[0] = 1 + self.relative[0]
            rx +=1
        if self.relative[1] >1.0 :
            print('2')
            self.relative[1] -= 1
            ry -=1
        if self.relative[1] < 0.0 :
            print('4')
            self.relative[1] = 1 + self.relative[1]
            ry +=1
        self.coord = (rx, ry)
        print(self.coord,self.relative)

    def update(self):
        print(s.WIN.get_size())
        self.WIDTH ,self.HEIGHT = s.WIN.get_size()
        s.CENTER.update(self.WIDTH/2, self.HEIGHT/2)
        main_caractere.updatePos()
    
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
        offset = p.Vector2(0,0)
        if self.pressed[0]:
            print('up')
            offset.y -= 1
        if self.pressed[1]:
            print('down')
            offset.y += 1
        if self.pressed[2]:
            print('left')
            offset.x -= 1
        if self.pressed[3]:
            print('right')
            offset.x += 1
        if offset.length() > 0:
            offset = offset.normalize()
            self.cal_move(offset.x*self.speed,offset.y*self.speed)
            

    def draw(self, win):
        super().draw(win)

    def cal_move(self,x,y):
        s.move(x,y)
        

    def get_speed(self):
        return self.speed
    
    def set_speed(self, speed):
        self.speed = speed

    def updatePos(self):
        print(s.CENTER)
        self.set_pos(s.CENTER.x,s.CENTER.y)


main_caractere = Caracter(10,1)


class Map:

    def __init__(self):
        self.centerMap:tuple[int,int] = (map_size[0]/2,map_size[1]/2)
        self.tile_size = tile_size

    def calc_map_coord(self,x,y) -> tuple[int,int]:
        '''
        transforme la coordornée de la matrice en coordonée de l'écran
        '''
        relativeX = ((x - self.centerMap[0]) + (s.coord[0] - s.relative[0])) * self.tile_size
        relativeY = ((y - self.centerMap[1]) + (s.coord[1] - s.relative[1])) * self.tile_size 

        return (relativeX,relativeY)
    
    def draw_map(self,win):
        for x in range(map_size[0]):
            for y in range(map_size[1]):
                tile = map[x][y]
                win.blit(p.transform.scale(tile,(self.tile_size,self.tile_size)),self.calc_map_coord(x,y)) 

s.map = Map()