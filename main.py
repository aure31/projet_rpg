import pygame as p
#import tools as t
import os
import anim as a
from Affichage import *

print('start')
bg = p.image.load(os.path.join('Assets', 'grassbg.jpg'))
player_img = p.image.load(os.path.join('Assets','textures','entities', 'player_sprites.png'))

clock = p.time.Clock()

def draw_window(s:Screen):
	s.draw()
	main_caractere.draw(s.WIN)

def main():
	#taille de l'ecran
	global localBG
	global anim_test
	anim_test = a.anim_sprite(player_img,s.CENTER,1.8,5)
	localBG = p.transform.scale(bg,(s.WIDTH,s.HEIGHT))
	print('main')
	while True:

		for event in p.event.get():
			if event.type == p.KEYDOWN:
				main_caractere.pressed_key(event.key,True)
			if event.type == p.KEYUP:
				main_caractere.pressed_key(event.key,False)

			if event.type == p.QUIT:
				p.quit()
				raise SystemExit
			#quand la taille est changer
			if event.type == p.VIDEORESIZE :
				s.update()
		
		main_caractere.move()

		draw_window(s)

		p.display.flip()  # Refresh on-screen display
		#permet de faire attendre la boucle pour attaindre FPS par second
		clock.tick(s.FPS)   

  

if __name__ == "__main__":
	main()