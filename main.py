import pygame as p

print('start')

p.init()
p.font.init()
FPS = 60
WIDTH, HEIGHT = 900, 500
WIN = p.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = (28, 22, 79)

clock = p.time.Clock()
p.display.set_caption('Hello World!')

def main():
	while True:
    	# Process player inputs.
		for event in p.event.get():
			if event.type == p.QUIT:
				p.quit()
				raise SystemExit

    	# Do logical updates here.
    	# ...

		WIN.fill("purple")  # Fill the display with a solid color

    	# Render the graphics here.
    	# ...

		p.display.flip()  # Refresh on-screen display
		clock.tick(60)   

  

if __name__ == "__main__":
	main()