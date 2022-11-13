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
BACKGROUND_1 = pygame.transform.scale(BACKGROUND_1, (WIDTH, HEIGHT)
)

MAIN_CHARACTER = pygame.image.load(
    os.path.join('JOGO-1SEM','Assets', 'Pizza_Panda.png')
)
MAIN_CHARACTER = pygame.transform.scale(
    MAIN_CHARACTER, (DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT)
)

PIZZA1_0 = pygame.image.load(
    os.path.join('JOGO-1SEM','Assets', 'Itens', 'Pizzas', '1.png')
)
PIZZA1_1 = pygame.transform.rotate(PIZZA1_0, 90)
PIZZA1_2 = pygame.transform.rotate(PIZZA1_0, 180)
PIZZA1_3 = pygame.transform.rotate(PIZZA1_0, 270)

PIZZA1 = [PIZZA1_0, PIZZA1_1, PIZZA1_2, PIZZA1_3]

PIZZA2_0 = pygame.image.load(
    os.path.join('JOGO-1SEM','Assets', 'Itens', 'Pizzas', '2.png')
)
PIZZA2_1 = pygame.transform.rotate(PIZZA2_0, 90)
PIZZA2_2 = pygame.transform.rotate(PIZZA2_0, 180)
PIZZA2_3 = pygame.transform.rotate(PIZZA2_0, 270)
PIZZA2 = [PIZZA2_0, PIZZA2_1, PIZZA2_2, PIZZA2_3]

PIZZA3_0 = pygame.image.load(
    os.path.join('JOGO-1SEM','Assets', 'Itens', 'Pizzas', '3.png')
)
PIZZA3_1 = pygame.transform.rotate(PIZZA3_0, 90)
PIZZA3_2 = pygame.transform.rotate(PIZZA3_0, 180)
PIZZA3_3 = pygame.transform.rotate(PIZZA3_0, 270)

PIZZA3 = [PIZZA3_0, PIZZA3_1, PIZZA3_2, PIZZA3_3]

PIZZA4_0 = pygame.image.load(
    os.path.join('JOGO-1SEM','Assets', 'Itens', 'Pizzas', '4.png')
)

PIZZA4_1 = pygame.transform.rotate(PIZZA4_0, 90)
PIZZA4_2 = pygame.transform.rotate(PIZZA4_0, 180)
PIZZA4_3 = pygame.transform.rotate(PIZZA4_0, 270)

PIZZA4 = [PIZZA4_0, PIZZA4_1, PIZZA4_2, PIZZA4_3]

Student1_0 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Student1', '0.png')
)
Student1_1 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Student1', '1.png')
)
Student1_2 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Student1', '2.png')
)
Student1_3 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Student1', '3.png')
)

Student1_0 =pygame.transform.scale(Student1_0, (105, 105))
Student1_1 =pygame.transform.scale(Student1_1, (105, 105))
Student1_2 =pygame.transform.scale(Student1_2, (105, 105))
Student1_3 =pygame.transform.scale(Student1_3, (105, 105))

Student1 = [Student1_0, Student1_1, Student1_2, Student1_3]

#variáveis dinâmicas
playing = True
spawn_time = 1
timer = 0
    #hitboxes
mc_hitbox = pygame.Rect(250, 360, DEFAULT_CHARACTER_WIDHT, DEFAULT_CHARACTER_HEIGHT)
pizza_refill_zone = pygame.Rect(0, ((HEIGHT - (HEIGHT * 0.20) * 3) // 1), (32), (256))
    #Listas
mc_projectiles = []
mc_projectiles_type = []
lanes_pos = [LANE_1.y, LANE_2.y, LANE_3.y, LANE_4.y]
enemy_alive_pos = []
enemy_alive_stats = []
    #inimigos
enemy_basico_stats = [1, 1]
enemy_basico_hitbox = pygame.Rect(WIDTH  - DEFAULT_CHARACTER_WIDHT, (lanes_pos[random.randint(0, 3)]), 
DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT)
    #velocidades
vel = 5
projectile_vel = 3
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
    all_pizzas = [PIZZA1, PIZZA2, PIZZA3, PIZZA4]
    sprite_order = 0
    point_time = 0
    point_time1 = 0
    run = True
    while run: 

        if playing == True:
            run_time = pygame.time.get_ticks()
        
        if run_time - point_time > 2000:
            point_time = run_time
            pygame.event.post(SpawnClientEvent)

        if run_time - point_time1 > 100:
            point_time1 = run_time
            sprite_order += 1

        keys_pressed = pygame.key.get_pressed()
        movement(keys_pressed, mc_hitbox)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    projectile = pygame.Rect(
                        mc_hitbox.x + mc_hitbox.width, mc_hitbox.y + mc_hitbox.height/8 , 40 , 40)
                    mc_projectiles.append(projectile)
                    projectile_type = all_pizzas[random.randint(0, 3)]
                    mc_projectiles_type.append(projectile_type)

            if event == SpawnClientEvent:
                SpawnEnemy()

        ProjectileHandling()
        EnemyHandling()
        ColissionHandling()


        #UPDATE DA TELA
        
        #preenche a tela
        WIN.blit(BACKGROUND_1, (0, 0))
        show_hitboxes = False
        if show_hitboxes == True:
            pygame.draw.rect(WIN, WHITE, LANE_1)
            pygame.draw.rect(WIN, BLACK, LANE_2)
            pygame.draw.rect(WIN, WHITE, LANE_3)
            pygame.draw.rect(WIN, BLACK, LANE_4)
            pygame.draw.rect(WIN, BLACK, pizza_refill_zone)

            pygame.draw.rect(WIN, BLACK, mc_hitbox)

            for enemy_basico_hitbox in enemy_alive_pos:
                pygame.draw.rect(WIN, RED, enemy_basico_hitbox)  

            for projectile in mc_projectiles:
                pygame.draw.rect(WIN, RED, projectile)
        
        for enemy_basico_hitbox in enemy_alive_pos:
            WIN.blit(Student1[sprite_order % 3], 
            (enemy_basico_hitbox.x - 30, enemy_basico_hitbox.y - 20)
            )

        for projectile in mc_projectiles:
            WIN.blit(all_pizzas[projectile[1] % 4][(sprite_order % 4)], 
            (projectile.x - 10, projectile.y - 12)
            )

        WIN.blit(MAIN_CHARACTER, (mc_hitbox.x, mc_hitbox.y))

        pygame.display.update()
        
        print(PIZZA1)

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
    enemy_basico_hitbox = pygame.Rect(WIDTH + DEFAULT_CHARACTER_WIDHT, 
    (lanes_pos[random.randint(0, 3)] + 40), DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT)
    enemy_basico_stats = [1, 3]
    enemy_alive_pos.append(enemy_basico_hitbox)
    enemy_alive_stats.append(enemy_basico_stats)

Jogo()