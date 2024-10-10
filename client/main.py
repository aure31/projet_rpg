import pygame as p
#import tools as t
import os
import anim as a
import caracter as c
from Screen import *

print('start')
bg = p.image.load(os.path.join('Assets', 'grassbg.jpg'))
player_img = p.image.load(os.path.join('Assets','textures','entities', 'player_sprites.png'))




clock = p.time.Clock()
p.display.set_caption('Hello World!')

def draw_window(s:Screen):
	s.draw()
	c.main_caractere.draw(s.WIN)
	

def main():
	#taille de l'ecran
	global localBG
	global anim_test
	anim_test = a.anim_sprite(player_img,s.CENTER,1.8,5)
	localBG = p.transform.scale(bg,(s.WIDTH,s.HEIGHT))

	while True:
		# Process player inputs.
		# event (evenement qui se passe)
		for event in p.event.get():
			if event.type == p.KEYDOWN:
				c.main_caractere.pressed_key(event.key,True)
			if event.type == p.KEYUP:
				c.main_caractere.pressed_key(event.key,False)

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
		c.main_caractere.move()
		
		#colorie le fond en violet
		#WIN.fill("violet")
		# Render the graphics here.
		# ...
		draw_window(s)

		p.display.flip()  # Refresh on-screen display
		#permet de faire attendre la boucle pour attaindre FPS par second
		clock.tick(s.FPS)   

  

if __name__ == "__main__":
	main()