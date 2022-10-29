from asyncio.windows_events import NULL
from sre_constants import JUMP
import pygame

class Hero(pygame.sprite.Sprite):

    JUMP_VELOCITY =  list([(i / 2.0) - 10.5 for i in range(0, 43)])
    JUMP_VELOCITY_INDEX = 0
    FLOOR = 0
    MAXWIDTH = 0
    JUMPING = False
    X_VELOCITY = 10
    

    def __init__(self, floor, width):
        print(self.JUMP_VELOCITY)
        pygame.sprite.Sprite.__init__(self)
        self.LoadSprites()
        self.FLOOR = floor
        self.MAXWIDTH = width

    def Move(self):
        keyPressed = pygame.key.get_pressed()
        self.rect.left -= self.X_VELOCITY if (keyPressed[pygame.K_LEFT] or keyPressed[pygame.K_a]) and self.rect.left > 0 else 0
        self.rect.right += self.X_VELOCITY if (keyPressed[pygame.K_RIGHT] or keyPressed[pygame.K_d]) and self.rect.right <=self.MAXWIDTH else 0
        self.rect.top -= self.X_VELOCITY if (keyPressed[pygame.K_UP] or keyPressed[pygame.K_w]) and self.rect.top > 0 else 0
        self.rect.bottom += self.X_VELOCITY if (keyPressed[pygame.K_DOWN] or keyPressed[pygame.K_s]) and self.rect.bottom <=self.MAXWIDTH else 0

    def Jump(self, keyPressed):
        if keyPressed[pygame.K_BACKSPACE] or keyPressed[pygame.K_w] or keyPressed[pygame.K_UP]:
            self.JUMPING = True
        if self.JUMPING:
            self.rect.y += self.JUMP_VELOCITY[self.JUMP_VELOCITY_INDEX]
            self.JUMP_VELOCITY_INDEX += 1 if self.JUMP_VELOCITY_INDEX < len(self.JUMP_VELOCITY)-1 else 0
            
            if self.rect.y > self.FLOOR:
                self.rect.y = self.FLOOR
                self.JUMPING = False
                self.JUMP_VELOCITY_INDEX = 0
        #return self.image.get_rect(center=(self.rect.x, ))

    def ChangeImage(self, image):
        image = pygame.transform.scale(image, (100,100))
        self.image = image
        self.rect = pygame.Rect((self.rect.x, self.rect.y), (100,100))

    def LoadSprites(self):
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
        

    def idle(self):
        self.idle_animation = True

    def update(self,speed):
        if self.idle_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.idle_animation = False

        self.image = self.sprites[int(self.current_sprite)]