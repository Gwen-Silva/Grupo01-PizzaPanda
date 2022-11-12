import os
import pygame
from pygame.locals import *
import random

pygame.init()

#VARIAVEIS ESTATICAS
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Supa Pizza Panda")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 60
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

PIZZA_PEPPERONI = pygame.image.load(
    os.path.join('JOGO-1SEM','Assets', 'Side_pizza_2.png ')
)

PIZZA_PEPPERONI = pygame.transform.scale(PIZZA_PEPPERONI, (64, 64))

#variáveis dinâmicas
playing = True
spawn_time = 1
timer = 0
    #hitboxes
mc_hitbox = pygame.Rect(250, 360, DEFAULT_CHARACTER_WIDHT, DEFAULT_CHARACTER_HEIGHT)
pizza_refill_zone = pygame.Rect(0, ((HEIGHT - (HEIGHT * 0.20) * 3) // 1), (32), (256))
    #Listas
mc_projectiles = []
lanes_pos = [LANE_1.y, LANE_2.y, LANE_3.y, LANE_4.y]
enemy_alive_pos = []
enemy_alive_stats = []
    #inimigos
enemy_basico_stats = [1, 1]
enemy_basico_hitbox = pygame.Rect(WIDTH - DEFAULT_CHARACTER_WIDHT, (lanes_pos[random.randint(0, 3)]), 
DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT)
    #velocidades
vel = 5
projectile_vel = 10
#EVENTOS
SpawnClient = pygame.event.custom_type() + 1
SpawnClientEvent = pygame.event.Event(SpawnClient)

#funções
def movement(keys_pressed, mc_hitbox):
    if keys_pressed[pygame.K_a] and mc_hitbox.x - vel > 0:
            mc_hitbox.x -= vel

    if keys_pressed[pygame.K_d] and (mc_hitbox.x + DEFAULT_CHARACTER_WIDHT) + vel < WIDTH // 4:
            mc_hitbox.x += vel

    if keys_pressed[pygame.K_w] and mc_hitbox.y - vel > 0 + ((HEIGHT * 0.20 // 1)):
            mc_hitbox.y -= vel

    if keys_pressed[pygame.K_s] and mc_hitbox.y + vel < HEIGHT - DEFAULT_CHARACTER_HEIGHT:
            mc_hitbox.y += vel

def Jogo():
    point_time = 0
    run = True
    while run: 
        #spawn teste
        if playing == True:
            run_time = pygame.time.get_ticks()
        
        if run_time - point_time > 2000:
            point_time = run_time
            pygame.event.post(SpawnClientEvent)

        keys_pressed = pygame.key.get_pressed()
        movement(keys_pressed, mc_hitbox)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    projectile = pygame.Rect(
                        mc_hitbox.x + mc_hitbox.width, mc_hitbox.y + mc_hitbox.height/3 , 50 , 10)
                    mc_projectiles.append(projectile)
                
            if event == SpawnClientEvent:
                SpawnEnemy()

        ProjectileHandling()
        EnemyHandling()
        ColissionHandling()


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

        for enemy_basico_hitbox in enemy_alive_pos:
            pygame.draw.rect(WIN, RED, enemy_basico_hitbox)  

        for projectile in mc_projectiles:
            pygame.draw.rect(WIN, RED, projectile)
            WIN.blit(PIZZA_PEPPERONI, (projectile.x - 4, projectile.y - 36))

        pygame.display.update()


        CLOCK.tick(FPS)
    pygame.quit()

def MainMenu():
    print("placeholder")

def ProjectileHandling():
    for projectile in mc_projectiles:
        projectile.x += (projectile_vel) // 1
        if projectile.x > WIDTH:
            mc_projectiles.remove(projectile)
        elif projectile.x < 0: 
             mc_projectiles.remove(projectile)

def EnemyHandling():
    for enemy_basico_hitbox in enemy_alive_pos:
        enemy_basico_hitbox.x -= (enemy_basico_stats[1]) // 1

def ColissionHandling():
    for projectile in mc_projectiles:
        for enemy_basico_hitbox in enemy_alive_pos:
            if projectile.colliderect(enemy_basico_hitbox):
                mc_projectiles.remove(projectile)
                enemy_alive_pos.remove(enemy_basico_hitbox)


def SpawnEnemy():
    enemy_basico_hitbox = pygame.Rect(WIDTH - DEFAULT_CHARACTER_WIDHT, (lanes_pos[random.randint(0, 3)] + 40), 
    DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT)
    enemy_basico_stats = [1, 3]
    enemy_alive_pos.append(enemy_basico_hitbox)
    enemy_alive_stats.append(enemy_basico_stats)

Jogo()