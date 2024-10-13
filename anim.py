import pygame as p
import time as t
from math import ceil
class anim_sprite():
    def __init__(self,img:p.Surface,coord:p.Vector2,Scale:int,fps:int = -1,hitbox:p.Rect = None):
        
        self.raw_img = img
        self.img = p.transform.scale(img, (img.get_width()*Scale, img.get_height()*Scale))
        self.raw_rect = hitbox
        if hitbox == None:
            self.width = self.img.get_width()
            self.height = self.img.get_height()
            self.rect = p.Rect(0,0,self.height,self.height)
        else:
            self.rect = hitbox
            self.width = self.rect.width
            self.height = self.rect.height
        self.raw_coord = coord
        self.coord = p.Vector2(coord.x-self.height/2,coord.y-self.height/2)
        self.rect = hitbox
        self.size = self.img.get_height()
        self.max_frame = self.img.get_width() // self.size
        self.fps_time = 1000//fps
        self.last_time = get_time_millis()
        self.frame = 0
        self.scale = Scale
        self.anim = 0

    def draw(self, win:p.Surface):
        win.blit(self.img, self.coord,\
                self.rect.move(self.size*self.frame, 0))
        self.next_frame()
        from Affichage import debug
        if debug:
            p.draw.circle(win,(255,0,0),self.raw_coord,5)
        
    def get_height(self):
        pixel = self.img.get_at((ceil(self.width/2),0))
        height = self.img.get_height()
        while pixel.a == 0 and height > 0:
            height -= 1
            pixel = self.img.get_at((ceil(self.width/2),height))
        return height
    
    def get_width(img):
        pixel = img.get_at((0,ceil(img.get_height/2)))
        width = self.img.get_width()
        while pixel.a == 0 and width > 0:
            width -= 1
            pixel = self.img.get_at((width,ceil(self.height/2)))
        return width

    def next_frame(self):
        if self.fps_time <= 0 or (not get_time_millis() - self.last_time >= self.fps_time):
             return
        
        self.last_time = get_time_millis()
        self.frame += 1
        if self.frame >= self.max_frame:
            self.frame = 0
    
    def set_frame(self,frame:int):
        self.frame = frame

    def set_anim(self,anim:int):
        self.anim = anim
    
    def get_pos(self):
        return self.coord

    def set_pos(self,x,y):
        self.coord = p.Vector2(x-self.height/2,y-self.height/2)
        self.raw_coord = p.Vector2(x,y)

    def set_scale(self,scale:int):
        self.img = p.transform.scale(self.raw_img, (self.raw_img.get_width()*scale, self.raw_img.get_height()*scale))
        if self.raw_rect == None:
            self.width = self.img.get_width()
            self.height = self.img.get_height()
            self.rect = p.Rect(0,0,self.height,self.height)
        else:
            self.rect = self.raw_rect.scale_by(scale,scale)
            self.width = self.rect.width
            self.height = self.rect.height
        self.size = self.height
        self.max_frame = self.img.get_width() // self.size
        self.scale = scale
        self.set_pos(self.raw_coord.x,self.raw_coord.y)


class entity(anim_sprite):
    def __init__(self,img: p.Surface,coord:tuple,Scale:float,fps:int,speed:float):
        super().__init__(img,coord,Scale,fps)
        self.speed = speed

    def draw(self,win):
        super().draw(win)

    def move_pos(self,vec2:p.Vector2):
        self.coord[0] += vec2.x
        self.coord[1] += vec2.y

    def get_speed(self):
        return self.speed

    def set_speed(self,speed):
        self.speed = speed
        print(self.speed)


def get_time_millis():
    return round(t.time() * 1000)