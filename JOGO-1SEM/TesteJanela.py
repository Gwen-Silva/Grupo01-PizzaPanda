import os
from tkinter import W
import pygame
from pygame.locals import *

pygame.init()

#VARIAVEIS ESTATICAS
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Supa Pizza Panda")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60
VEL = 5
PROJECTILE_VEL = 15
CLOCK = pygame.time.Clock()

DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT = (64, 64)

LANE_1 = pygame.Rect((WIDTH - ((WIDTH * 0.75) // 1)), (HEIGHT - ((HEIGHT * 0.20) // 1)), 
    (WIDTH * 0.75) // 1, (HEIGHT * 0.20) // 1
)
LANE_2 = pygame.Rect((WIDTH - ((WIDTH * 0.75) // 1)), (HEIGHT - ((HEIGHT * 0.20) // 1) * 2), 
    (WIDTH * 0.75) // 1, (HEIGHT * 0.20) // 1
)
LANE_3 = pygame.Rect((WIDTH - ((WIDTH * 0.75) // 1)), (HEIGHT - ((HEIGHT * 0.20) // 1) * 3), 
    (WIDTH * 0.75) // 1, (HEIGHT * 0.20) // 1
)
LANE_4 = pygame.Rect((WIDTH - ((WIDTH * 0.75) // 1)), (HEIGHT - ((HEIGHT * 0.20) // 1) * 4), 
    (WIDTH * 0.75) // 1, (HEIGHT * 0.20) // 1
)

BACKGROUND_1 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Background.jpg')
)

MAIN_CHARACTER = pygame.image.load(
    os.path.join('JOGO-1SEM','Assets', 'panda.jpg')
)
MAIN_CHARACTER = pygame.transform.scale(
    MAIN_CHARACTER, (DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT)
)

TEST_DUMMY = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'panda.jpg')
)
TEST_DUMMY = pygame.transform.scale(TEST_DUMMY, (DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT))

PIZZA_PEPPERONI = pygame.image.load(
    os.path.join('JOGO-1SEM','Assets', 'Side_pizza.png ')
)
PIZZA_PEPPERONI = pygame.transform.scale(PIZZA_PEPPERONI, (64, 64))

#variáveis dinâmicas
    #hitboxes
mc_hitbox = pygame.Rect(250, 360, DEFAULT_CHARACTER_WIDHT, DEFAULT_CHARACTER_HEIGHT)
enemy_hitbox = pygame.Rect(700, 360, DEFAULT_CHARACTER_WIDHT, DEFAULT_CHARACTER_HEIGHT)
pizza_refill_zone = pygame.Rect(0, ((HEIGHT - (HEIGHT * 0.20) * 3) // 1), (32), (256))
    #Listas
mc_projectiles = []
enemy_alive = []
waves = []
#EVENTOS
enemy_hit = pygame.USEREVENT + 1

#funções
def movement(keys_pressed, mc_hitbox):
    if keys_pressed[pygame.K_a] and mc_hitbox.x - VEL > 0:
            mc_hitbox.x -= VEL

    if keys_pressed[pygame.K_d] and (mc_hitbox.x + DEFAULT_CHARACTER_WIDHT) + VEL < WIDTH // 4:
            mc_hitbox.x += VEL

    if keys_pressed[pygame.K_w] and mc_hitbox.y - VEL > 0 + ((HEIGHT * 0.20 // 1)):
            mc_hitbox.y -= VEL

    if keys_pressed[pygame.K_s] and mc_hitbox.y + VEL < HEIGHT - DEFAULT_CHARACTER_HEIGHT:
            mc_hitbox.y += VEL

def pizza_trow(mc_projectiles, projectile):
        mc_projectiles.append(projectile)

def main():
    run = True
    while run: 
        
        keys_pressed = pygame.key.get_pressed()
        movement(keys_pressed, mc_hitbox)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    projectile = pygame.Rect(
                        mc_hitbox.x + mc_hitbox.width, mc_hitbox.y + mc_hitbox.height/2, 50 , 4)
                    mc_projectiles.append(projectile)

        for projectile in mc_projectiles:
            projectile.x += (PROJECTILE_VEL) // 1
            if enemy_hitbox.colliderect(projectile):
                mc_projectiles.remove(projectile)
            if projectile.x > WIDTH:
                mc_projectiles.remove(projectile)
            elif projectile.x < 0: 
                         mc_projectiles.remove(projectile)

        #UPDATE DA TELA
        
        #preenche a tela
        WIN.blit(BACKGROUND_1, (0, 0))
        pygame.draw.rect(WIN, WHITE, LANE_1)
        pygame.draw.rect(WIN, BLACK, LANE_2)
        pygame.draw.rect(WIN, WHITE, LANE_3)
        pygame.draw.rect(WIN, BLACK, LANE_4)
        pygame.draw.rect(WIN, BLACK, pizza_refill_zone)

        pygame.draw.rect(WIN, BLACK, mc_hitbox)
        WIN.blit(MAIN_CHARACTER, (mc_hitbox.x, mc_hitbox.y))

        pygame.draw.rect(WIN, RED, enemy_hitbox)
        
        for projectile in mc_projectiles:
            WIN.blit(PIZZA_PEPPERONI, (projectile))
            pygame.draw.rect(WIN, RED, projectile)

        pygame.display.update()


        CLOCK.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()