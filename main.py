import pygame as p
import tools as t

print('start')

p.init()
p.font.init()
FPS = 30
flags = p.RESIZABLE
#crée une fenetre de taille (900,500)px dont on peut modifier la taille
WIN = p.display.set_mode((900, 500),flags)
global WIDTH 
global HEIGHT
WIDTH ,HEIGHT = WIN.get_size()
BACKGROUND = (28, 22, 79)
bg = p.image.load("Assets\\background.jpeg")


clock = p.time.Clock()
p.display.set_caption('Hello World!')

def main():
	#taille de l'ecran
	 
	while True:
    	# Process player inputs.
		# event (evenement qui se passe)
		for event in p.event.get():
			if event.type == p.QUIT:
				p.quit()
				raise SystemExit
			#quand la taille est changer
			if event.type == p.VIDEORESIZE :
				print("resize")
				WIDTH ,HEIGHT = WIN.get_size()
				p.transform.scale(bg,(WIDTH,HEIGHT))
				print("resize2")

    	# Do logical updates here.
    	# ...

		#colorie le fond en violet
		WIN.blit(bg,(0,0))  # Fill the display with a solid color
		#crée un text puis l'affiche
		print(p.display.get_surface())
		tex = t.texte(["je t'aime mon bb"],WIDTH/2,HEIGHT/2,90,(255, 135, 247))
		tex.affiche(WIN)
    	# Render the graphics here.
    	# ...

		p.display.flip()  # Refresh on-screen display
		#permet de faire attendre la boucle pour attaindre FPS par second
		clock.tick(FPS)   

  

if __name__ == "__main__":
	main()