import pygame as p
from tile import *
import anim as a
import os
from math import ceil

debug = True


class Screen:

    def __init__(self, width, height, fps):
        p.init()
        p.font.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.FPS = fps
        flags = p.RESIZABLE
        #crée une fenetre de taille (900,500)px dont on peut modifier la taille
        self.WIN = p.display.set_mode((width, height), flags)
        self.BACKGROUND = (28, 22, 79)
        self.CENTER = p.Vector2(self.WIDTH / 2, self.HEIGHT / 2)
        self.map: Map = None
        self.zoom = 1
        p.display.set_icon(p.image.load(os.path.join('Assets', 'logo.png')))
        p.display.set_caption('Pow Arena')
        self.relative = [0.5, 0.5]

    def draw(self):
        self.WIN.fill(self.BACKGROUND)
        self.map.draw_map(self.WIN)

    def set_zoom(self, zoom: int):
        self.zoom = zoom
        print(zoom)
        self.map.tile_size = tile_size * zoom

    def add_zoom(self, zoom: int):
        if zoom == 0:
            return
        raw_zoom = zoom
        zoom = zoom / abs(zoom)
        zoom *= 0.1
        if self.zoom + zoom < 0.8 or self.zoom + zoom > 3:
            return
        print(self.zoom + zoom, zoom)

        s.set_zoom(self.zoom + zoom)
        true_coord = ((self.relative[0] + self.map.x) * zoom,
                      (self.relative[0] + self.map.x) * zoom)
        true_relative = (true_coord[0] - int(true_coord[0]),
                         true_coord[1] - int(true_coord[1]))
        self.set_relative(true_relative[0], true_relative[1])
        print(self.relative)
        s.map.calc_tile_box()
        main_caractere.set_scale(self.zoom)

    def set_coord(self, x: int, y: int):
        self.coord = (x, y)

    def move(self, x: int, y: int):
        '''
        déplace les tiles de x et y pixel sur l'écran
        up:Y-1, down:Y+1, left:X-1, right:X+1
        '''
        self.relative[0] += x / self.map.tile_size
        self.relative[1] += y / self.map.tile_size
        rx, ry = (0, 0)
        if self.relative[0] > 1.0:
            self.relative[0] -= 1
            rx += 1
        if self.relative[0] < 0.0:
            self.relative[0] = 1 + self.relative[0]
            rx -= 1
        if self.relative[1] > 1.0:
            self.relative[1] -= 1
            ry += 1
        if self.relative[1] < 0.0:
            self.relative[1] = 1 + self.relative[1]
            ry -= 1
        if rx != 0 or ry != 0:
            self.map.tile_box_move(rx, ry)

    def set_relative(self, x, y):
        print(self.relative)
        self.relative[0] += x
        self.relative[1] += y
        print(self.relative)
        rx, ry = (0, 0)
        if self.relative[0] > 1.0:
            self.relative[0] -= int(self.relative[0])
            rx += int(self.relative[0])
        if self.relative[0] < 0.0:
            self.relative[0] = 1 + self.relative[0] - int(self.relative[0])
            rx -= int(self.relative[0])
        if self.relative[1] > 1.0:
            self.relative[1] -= int(self.relative[1])
            ry += int(self.relative[1])
        if self.relative[1] < 0.0:
            self.relative[1] = 1 + self.relative[1] - int(self.relative[1])
            ry -= int(self.relative[1])
        if rx != 0 or ry != 0:
            self.map.tile_box_move(rx, ry)

    def update(self):
        print(s.WIN.get_size())
        self.WIDTH, self.HEIGHT = s.WIN.get_size()
        s.CENTER.update(self.WIDTH / 2, self.HEIGHT / 2)
        main_caractere.updatePos()
        self.map.calc_tile_box()


s = Screen(900, 500, 30)


class Caracter(a.anim_sprite):

    def __init__(self, speed: int, scale):

        img = p.image.load(
            os.path.join('Assets', 'textures', 'entities',
                         'player_sprites.png'))
        super().__init__(img, s.CENTER, scale, 12, p.Rect(55, 160, 149, 96))
        self.speed = speed / s.FPS
        self.momuntum = 0

        #liste des touches pressées :
        #0:up, 1:down, 2:left, 3:right
        self.pressed = [False, False, False, False]
        self.relative = [0.5, 0.5]

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
        offset = p.Vector2(0, 0)
        #0:up, 1:down, 2:left, 3:right
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
            s.move(offset.x * self.speed, offset.y * self.speed)

    def draw(self, win):
        super().draw(win)

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def updatePos(self):
        print(s.CENTER)
        self.set_pos(s.CENTER.x, s.CENTER.y)


main_caractere = Caracter(1000, 1)


class Map:

    def __init__(self, x=0, y=0):
        '''
        initialise la map et met l'ecran sur la tile box (x,y)
        '''
        self.x = x
        self.y = y
        self.tile_size = tile_size
        self.calc_tile_box()

    def calc_map_coord(self, x, y) -> tuple[int, int]:
        '''
        transforme la coordornée de la tile box en coordonée de l'écran
        '''
        relativeX = (x - s.relative[0]) * self.tile_size
        relativeY = (y - s.relative[1]) * self.tile_size
        return (relativeX, relativeY)

    def draw_map(self, win: p.Surface):
        '''
        dessine la map sur l'écran
        '''
        for x in range(self.tile_box.x, self.tile_box.x + self.tile_box.width):
            for y in range(self.tile_box.y,
                           self.tile_box.y + self.tile_box.height):
                if x < 0 or y < 0 or x >= map_size[0] or y >= map_size[1]:
                    continue
                tile = map[x][y]
                calc = self.calc_map_coord(x - self.tile_box.x - 0.5,
                                           y - self.tile_box.y - 0.5)
                win.blit(
                    p.transform.scale(
                        tile.img, (self.tile_size + 1, self.tile_size + 1)),
                    calc)
                if debug:
                    squared = p.Rect(calc, (self.tile_size, self.tile_size))
                    p.draw.rect(win, (255, 0, 0), squared, 2)

    def tile_box_move(self, x: int, y: int):
        '''
        déplace la tile box de x et y tile dans la matrice
        '''
        #print(x,y,self.tile_box)
        self.tile_box = self.tile_box.move(x, y)
        self.x += x
        self.y += y

    def calc_tile_box(self):
        '''
        calcule la tile box (la zone de la map qui est affichée)
        '''

        tileWidth = ceil(s.WIDTH / self.tile_size)
        tileHeight = ceil(s.HEIGHT / self.tile_size)
        self.tile_box = p.Rect(self.x - 1 - tileWidth // 2,
                               self.y - 1 - tileHeight // 2, tileWidth + 2,
                               tileHeight + 2)
        print(self.tile_box)


s.map = Map()


class NPC():

    def __init__(self, nom: str):
        self.nom = nom
        self.dialogue = []

    def add_dialogue(self, dialogue: str):
        self.dialogue.append(dialogue)
        return self


gerald = NPC('Gerald').add_dialogue(
    'Bonjour, je suis Gerald, le marchand de la ville')
