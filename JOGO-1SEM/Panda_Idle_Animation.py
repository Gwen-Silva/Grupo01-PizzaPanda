import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.idle_animation = False
		self.sprites = []

		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda1.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda2.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda3.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda4.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda5.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda6.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda7.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda8.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda9.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda10.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda11.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda12.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda13.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda14.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda15.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda16.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda17.png'))
		self.sprites.append(pygame.image.load('Assets/Panda_Sprite/Pizza_Panda18.png'))

		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def idle(self):
		self.idle_animation = True

	def update(self,speed):
		if self.idle_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.idle_animation = False

		self.image = self.sprites[int(self.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		else:
			player.idle()

	# Drawing
	screen.fill((0,0,0))
	moving_sprites.draw(screen)
	moving_sprites.update(0.25)
	pygame.display.flip()
	clock.tick(60)