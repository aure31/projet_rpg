import pygame as p

class anim_sprite():
    def __init__(self,img:p.Surface,coord:tuple,Scale:int,fps:int):
        super().__init__()
        print(img.get_size(),coord,Scale) 
        self.img = p.transform.scale(img, (img.get_width()*Scale, img.get_height()*Scale))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.tcoord = (coord[0]-5,coord[1]-5)
        self.coord = (coord[0]-self.height/2,coord[1]-self.height/2)
        self.rect = p.Rect(0,0,self.height,self.height)
        self.size = self.height
        self.max_frame = self.img.get_width() // self.size
        self.fps = fps
        self.frame = 0
        self.count = 0
        self.scale = Scale
        print(self.rect.size,coord,Scale)

    def draw(self, win):
        win.blit(self.img, self.coord,\
                  self.rect.move(self.size*self.frame, 0))
        image = p.Surface((10, 10))
        image.fill((255, 255, 255))
        win.blit(image,self.tcoord)
        self.count += 1
        if self.count >= self.fps:
            self.count = 0
            self.frame += 1
        if self.frame >= self.max_frame:
            self.frame = 0
        