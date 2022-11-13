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

Student1_0 = pygame.transform.scale(Student1_0, (105, 105))
Student1_1 = pygame.transform.scale(Student1_1, (105, 105))
Student1_2 = pygame.transform.scale(Student1_2, (105, 105))
Student1_3 = pygame.transform.scale(Student1_3, (105, 105))

Student1 = [Student1_0, Student1_1, Student1_2, Student1_3]

Adult1_0 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult1', '0.png')
)
Adult1_1 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult1', '1.png')
)
Adult1_2 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult1', '2.png')
)
Adult1_3 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult1', '3.png')
)

Adult1_0 = pygame.transform.scale(Adult1_0, (105, 105))
Adult1_1 = pygame.transform.scale(Adult1_1, (105, 105))
Adult1_2 = pygame.transform.scale(Adult1_2, (105, 105))
Adult1_3 = pygame.transform.scale(Adult1_3, (105, 105))

Adult1 = [Adult1_0, Adult1_1, Adult1_2, Adult1_3]

Adult2_0 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult2', '0.png')
)
Adult2_1 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult2', '1.png')
)
Adult2_2 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult2', '2.png')
)
Adult2_3 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult2', '3.png')
)

Adult2_0 = pygame.transform.scale(Adult2_0, (105, 105))
Adult2_1 = pygame.transform.scale(Adult2_1, (105, 105))
Adult2_2 = pygame.transform.scale(Adult2_2, (105, 105))
Adult2_3 = pygame.transform.scale(Adult2_3, (105, 105))

Adult2 = [Adult2_0, Adult2_1, Adult2_2, Adult2_3]

Adult3_0 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult3', '0.png')
)
Adult3_1 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult3', '1.png')
)
Adult3_2 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult3', '2.png')
)
Adult3_3 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult3', '3.png')
)

Adult3_0 = pygame.transform.scale(Adult3_0, (105, 105))
Adult3_1 = pygame.transform.scale(Adult3_1, (105, 105))
Adult3_2 = pygame.transform.scale(Adult3_2, (105, 105))
Adult3_3 = pygame.transform.scale(Adult3_3, (105, 105))

Adult3 = [Adult3_0, Adult3_1, Adult3_2, Adult3_3]

Adult4_0 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult4', '0.png')
)
Adult4_1 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult4', '1.png')
)
Adult4_2 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult4', '2.png')
)
Adult4_3 = pygame.image.load(
    os.path.join('JOGO-1SEM', 'Assets', 'Inimigos', 'Adult4', '3.png')
)

Adult4_0 = pygame.transform.scale(Adult4_0, (105, 105))
Adult4_1 = pygame.transform.scale(Adult4_1, (105, 105))
Adult4_2 = pygame.transform.scale(Adult4_2, (105, 105))
Adult4_3 = pygame.transform.scale(Adult4_3, (105, 105))

Adult4 = [Adult4_0, Adult4_1, Adult4_2, Adult4_3]

playing = False
    #hitboxes
mc_hitbox = pygame.Rect(250, 360, DEFAULT_CHARACTER_WIDHT, DEFAULT_CHARACTER_HEIGHT)
pizza_refill_zone = pygame.Rect(0, ((HEIGHT - (HEIGHT * 0.20) * 3) // 1), (32), (256))
    #Listas
mc_projectiles = []
lanes_pos = [LANE_1.y, LANE_2.y, LANE_3.y, LANE_4.y]
enemy_alive = []
    #inimigos
enemy_basico_hitbox = pygame.Rect(WIDTH  - DEFAULT_CHARACTER_WIDHT, (lanes_pos[random.randint(0, 3)]), 
DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT)
    #velocidades
vel = 5
projectile_vel = 3
#EVENTOS
CustomEvent1 = pygame.event.custom_type() + 1
SpawnEnemyEvent = pygame.event.Event(CustomEvent1)

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
    all_adults = [Adult1, Adult2, Adult3, Adult4]
    all_students = [Student1]
    all_enemies = [all_adults, all_students]

    sprite_order = 0
    spawn_rate = 2000

    point_time = 0
    point_time1 = 0

    run = True
    playing = True
    while run: 

        if playing == True:
            run_time = pygame.time.get_ticks()
        
        if run_time - point_time > spawn_rate and spawn_rate != 0:
            point_time = run_time
            pygame.event.post(SpawnEnemyEvent)

        if run_time - point_time1 > 80:
            point_time1 = run_time
            sprite_order += 1

        keys_pressed = pygame.key.get_pressed()
        movement(keys_pressed, mc_hitbox)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    SpawnProjectile()

            if event == SpawnEnemyEvent:
                SpawnEnemy()

        ProjectileHandling()
        EnemyHandling()
        ColissionHandling()
        RemoveEntities()

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

            for enemy_basico_hitbox in enemy_alive:
                pygame.draw.rect(WIN, RED, enemy_basico_hitbox)  

            for projectile in mc_projectiles:
                pygame.draw.rect(WIN, RED, projectile)
        
        for i in range(len(enemy_alive)):
                WIN.blit(all_enemies[enemy_alive[i][1][0]][enemy_alive[i][1][1]][sprite_order % 3], 
                (enemy_alive[i][0].x - 30, enemy_alive[i][0].y - 20)
                )
 

        for i in range(len(mc_projectiles)):
            WIN.blit(all_pizzas[mc_projectiles[i][1]][(sprite_order % 4)], 
            (mc_projectiles[i][0].x - 10, mc_projectiles[i][0].y - 12)
            )

        WIN.blit(MAIN_CHARACTER, (mc_hitbox.x, mc_hitbox.y))

        pygame.display.update()
        
        print(PIZZA1)

        CLOCK.tick(FPS)
    pygame.quit()

def MainMenu():
    print("Fazer")

def ProjectileHandling():
    for i in range(len(mc_projectiles)):
        mc_projectiles[i][0].x += (projectile_vel) // 1
        if mc_projectiles[i][0].x > WIDTH:
            mc_projectiles[i][2] = False
        elif mc_projectiles[i][0].x < 0: 
            mc_projectiles[i][2] = False

def EnemyHandling():
    for i in range(len(enemy_alive)):
        enemy_alive[i][0].x -= (enemy_stats[2]) // 1

def ColissionHandling():    
    for i in range(len(mc_projectiles)):
        for i2 in range(len(enemy_alive)):
                if mc_projectiles[i][0].colliderect(enemy_alive[i2][0]):
                    mc_projectiles[i][2] = False
                    enemy_alive[i2][1][3] -= 1


def SpawnEnemy():
    global enemy_stats
    enemy_hitbox = pygame.Rect(WIDTH + DEFAULT_CHARACTER_WIDHT, 
    (lanes_pos[random.randint(0, 3)] + 40), DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT)
    enemy_stats = [0, random.randint(0, 3), 3, 1]
    enemy_alive.append([enemy_hitbox, enemy_stats])

def SpawnProjectile():
    projectile = pygame.Rect(mc_hitbox.x + mc_hitbox.width, mc_hitbox.y + mc_hitbox.height/8 , 40 , 40)
    mc_projectiles.append([projectile, random.randint(0, 3), True])

def RemoveEntities():
    for_removal = []
    for_removal2 = []
    for i in range(len(mc_projectiles)):
        if mc_projectiles[i][2] == False:
            for_removal.append(mc_projectiles[i])
    
    for i2 in range(len(enemy_alive)):
        if enemy_alive[i2][1][3] < 1:
            for_removal2.append(enemy_alive[i2])

    for i in range(len(for_removal)):
        mc_projectiles.remove(for_removal[i])

    for i in range(len(for_removal2)):
        enemy_alive.remove(for_removal2[i])
def intro():
    print("Fazer")
Jogo()