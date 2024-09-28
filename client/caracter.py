import pygame as p
import anim as a
import os
from Screen import *

class Caracter(a.anim_sprite):
    def __init__(self, speed, zomm):
        img = p.image.load(os.path.join('Assets','textures','entities', 'golden_gobelin_sprites-52x52.png'))
        super().__init__(img, s.CENTER, zomm , -1)
        self.speed = speed

    def move(self, direction:p.Vector2):
        if direction == 'up':
            s.move(0,-self.speed)
        elif direction == 'down':
            s.move(0,self.speed)
        elif direction == 'left':
            s.move(-self.speed,0)
        elif direction == 'right':
            s.move(self.speed,0)

    def draw(self, win):
        super().draw(win)


    def get_speed(self):
        return self.speed
    def set_speed(self, speed):
        self.speed = speed