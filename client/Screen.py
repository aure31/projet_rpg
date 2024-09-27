import pygame as p

class Screen:
    def __init__(self, width, height,fps):
        p.init()
        p.font.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.coord = (0,0)
        self.FPS = fps
        flags = p.RESIZABLE
        #crée une fenetre de taille (900,500)px dont on peut modifier la taille
        self.WIN = p.display.set_mode((width, height),flags)
        self.BACKGROUND = (28, 22, 79)
        self.CENTER = p.Vector2(self.WIDTH/2, self.HEIGHT/2)
        

    def clear(self):
        self.screen = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def draw():
        pass

    def render(self):
        return '\n'.join([''.join(row) for row in self.screen])
    

s = Screen(900,500,30)