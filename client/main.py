import pygame as p
import tools as t
import os
from network import *
import anim as a
import caracter as c
from Screen import *
from tile import *

print('start')
bg = p.image.load(os.path.join('Assets', 'grassbg.jpg'))
player_img = p.image.load(os.path.join('Assets','textures','entities', 'golden_gobelin_sprites-52x52.png'))

main_caractere = c.Caracter(6,2)


clock = p.time.Clock()
p.display.set_caption('Hello World!')


def draw_window(win):
	#win.blit(localBG,(0,0))
	Screen.draw()
	#anim_test.draw(win)
	main_caractere.draw(win)

def main():
	#taille de l'ecran
	global localBG
	global anim_test
	anim_test = a.anim_sprite(player_img,s.CENTER,1.8,5)
	localBG = p.transform.scale(bg,(s.WIDTH,s.HEIGHT))

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
				WIDTH ,HEIGHT = s.WIN.get_size()
				s.CENTER.update(WIDTH/2, HEIGHT/2)
				localBG = p.transform.scale(bg,(WIDTH,HEIGHT))

		# Do logical updates here.
		# ...

		#colorie le fond en violet
		#WIN.fill("violet")
		# Render the graphics here.
		# ...
		draw_window(s.WIN)

		p.display.flip()  # Refresh on-screen display
		#permet de faire attendre la boucle pour attaindre FPS par second
		clock.tick(s.FPS)   

  

if __name__ == "__main__":
	main()