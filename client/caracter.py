import pygame as p
import anim as a
import os
from Screen import *

class Caracter(a.anim_sprite):
    def __init__(self, speed, zomm):
        img = p.image.load(os.path.join('Assets','textures','entities', 'player_sprites.png'))
        super().__init__(img, s.CENTER, zomm , -1)
        self.speed = speed
        self.pressed = [False,False,False,False]

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
            s.move(0,-self.speed)
        if self.pressed[1]:
            print('down')
            s.move(0,self.speed)
        if self.pressed[2]:
            print('left')
            s.move(-self.speed,0)
        if self.pressed[3]:
            print('right')
            s.move(self.speed,0)

    def draw(self, win):
        super().draw(win)


    def get_speed(self):
        return self.speed
    def set_speed(self, speed):
        self.speed = speed