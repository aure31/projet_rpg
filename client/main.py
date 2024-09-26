import pygame as p
import tools as t
import os
from network import *
import anim as a

print('start')

p.init()
p.font.init()
FPS = 30
flags = p.RESIZABLE
#crée une fenetre de taille (900,500)px dont on peut modifier la taille
WIN = p.display.set_mode((900, 500),flags)
BACKGROUND = (28, 22, 79)
WIDTH ,HEIGHT = WIN.get_size()
bg = p.image.load(os.path.join('Assets', 'grassbg.jpg'))
player_img = p.image.load(os.path.join('Assets','textures','entities', 'golden_gobelin_sprites-52x52.png'))


clock = p.time.Clock()
p.display.set_caption('Hello World!')


def draw_window(win):
	WIN.blit(localBG,(0,0))
	win.fill(BACKGROUND)
	anim_test.draw(win)

def main():
	#taille de l'ecran
	global WIDTH
	global HEIGHT
	global localBG
	global anim_test
	anim_test = a.anim_sprite(player_img,(WIDTH/2, HEIGHT/2),3,5)
	localBG = p.transform.scale(bg,(WIDTH,HEIGHT))

	n = Network()
	startPos = n.getPos() # Get the starting position from the server

	while True:
		# Process player inputs.
		# event (evenement qui se passe)
		for event in p.event.get():
			if event.type == p.QUIT:
				p.quit()
				raise SystemExit
			#quand la taille est changer
			if event.type == p.VIDEORESIZE :
				WIDTH ,HEIGHT = WIN.get_size()
				localBG = p.transform.scale(bg,(WIDTH,HEIGHT))

		# Do logical updates here.
		# ...

		#colorie le fond en violet
		#WIN.fill("violet")
		# Render the graphics here.
		# ...
		draw_window(WIN)

		p.display.flip()  # Refresh on-screen display
		#permet de faire attendre la boucle pour attaindre FPS par second
		clock.tick(FPS)   

  

if __name__ == "__main__":
	main()