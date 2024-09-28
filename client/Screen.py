import pygame as p

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

    def draw():
        pass

    def set_coord(self, x:int, y:int):
        self.coord = (x,y)

    def move(self, x:int, y:int):
        self.coord = (self.coord+x, self.coord+y)
    

s = Screen(900,500,30)