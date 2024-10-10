import pygame as p
import anim as a
import os
from Screen import s


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