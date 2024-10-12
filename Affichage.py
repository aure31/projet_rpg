import pygame as p
from tile import *
import anim as a
import os
from math import ceil

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
        p.display.set_caption('Pow Arena')
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
        self.relative[0] += x/self.map.tile_size
        self.relative[1] += y/self.map.tile_size
        rx, ry = (0,0)
        if self.relative[0] > 1.0:
            self.relative[0] -= 1
            rx -=1
        if self.relative[0] < 0.0 :
            self.relative[0] = 1 + self.relative[0]
            rx +=1
        if self.relative[1] >1.0 :
            self.relative[1] -= 1
            ry -=1
        if self.relative[1] < 0.0 :
            self.relative[1] = 1 + self.relative[1]
            ry +=1
        if rx != 0 or ry != 0:
            
            self.coord = (self.coord[0]+rx, self.coord[1]+ry)
            self.map.map_move(-rx,-ry)
        

    def update(self):
        print(s.WIN.get_size())
        self.WIDTH ,self.HEIGHT = s.WIN.get_size()
        s.CENTER.update(self.WIDTH/2, self.HEIGHT/2)
        main_caractere.updatePos()
        self.map.screen_map = self.map.calc_map_rect()
    
s = Screen(900,500,30)


class Caracter(a.anim_sprite):
    def __init__(self, speed:int, scale):
        
        img = p.image.load(os.path.join('Assets','textures','entities', 'player_sprites.png'))
        super().__init__(img, s.CENTER, scale , 12)
        self.speed = speed/s.FPS
        self.pressed = [False,False,False,False]
        self.relative = [0.5,0.5]

    def pressed_key(self, key, pressed):
        match key:
            case p.K_UP | p.K_z:
                self.pressed[0] = pressed
            case p.K_DOWN | p.K_s:
                self.pressed[1] = pressed
            case p.K_LEFT | p.K_q:
                self.pressed[2] = pressed
            case p.K_RIGHT | p.K_d:
                self.pressed[3] = pressed

    def move(self):
        offset = p.Vector2(0,0)
        if self.pressed[0]:
            offset.y -= 1
        if self.pressed[1]:
            offset.y += 1
        if self.pressed[2]:
            offset.x -= 1
        if self.pressed[3]:
            offset.x += 1
        if offset.length() > 0:
            offset = offset.normalize()
            s.move(offset.x*self.speed,offset.y*self.speed)
            

    def draw(self, win):
        super().draw(win)
        
        

    def get_speed(self):
        return self.speed
    
    def set_speed(self, speed):
        self.speed = speed

    def updatePos(self):
        print(s.CENTER)
        self.set_pos(s.CENTER.x,s.CENTER.y)


main_caractere = Caracter(1000,1)


class Map:

    def __init__(self):
        self.centerMap:tuple[int,int] = (map_size[0]/2,map_size[1]/2)
        self.tile_size = tile_size
        self.screen_map = self.calc_map_rect()
        self.show_map = self.screen_map

    def calc_map_coord(self,x,y) -> tuple[int,int]:
        '''
        transforme la coordornée de la matrice en coordonée de l'écran
        '''
        relativeX = (-x + (s.coord[0] - s.relative[0])) * self.tile_size
        relativeY = (-y + (s.coord[1] - s.relative[1])) * self.tile_size 
        return (relativeX,relativeY)
    
    def draw_map(self,win):
        show_map  = self.show_map
        print(show_map.x,show_map.width+show_map.x)
        print(show_map.y,show_map.width+show_map.y)
        for x in range(show_map.x,show_map.width+show_map.x):
            for y in range(show_map.y,show_map.height+show_map.y):
                try:
                    #print(x,y)
                    tile = map[x][y]
                    if x == 5 and y == 5:
                        print(tile)
                    win.blit(p.transform.scale(tile,(self.tile_size,self.tile_size)),self.calc_map_coord(x,y))
                except IndexError:
                    print('error',x,y)
                    pass


    def map_move(self,x:int,y:int):
        self.centerMap = (self.centerMap[0]+x,self.centerMap[1]+y)
        self.show_map = self.show_map.move(x,y)
        print(self.show_map.size,map_size)
        if abs(self.show_map.bottomleft[0]) > map_size[0] or abs(self.show_map.bottomleft[1]) > map_size[1]:
            print('bad')
            self.show_map.width = map_size[0] + self.show_map.bottomleft[0]
            self.show_map.height = map_size[1] + self.show_map.bottomleft[1]
        

    def calc_map_rect(self):
        midX = ceil(s.WIDTH/self.tile_size)
        midY = ceil(s.HEIGHT/self.tile_size)
        return p.Rect(s.coord[0],s.coord[1],s.coord[0]+2+midX,s.coord[1]+2+midY)
        #return p.Rect(0,0,2,2)

s.map = Map()


class NPC():

    def __init__(self,nom:str):
        self.nom = nom
        self.dialogue = []
    
    def add_dialogue(self,dialogue:str):
        self.dialogue.append(dialogue)
        return self
    

gerald = NPC('Gerald').add_dialogue('Bonjour, je suis Gerald, le marchand de la ville') 