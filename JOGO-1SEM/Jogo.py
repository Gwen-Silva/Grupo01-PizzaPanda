import os
import pygame
from math import sin, cos
from pygame.locals import *
from random import randint, choice

pygame.init()

# VARIAVEIS ESTATICAS
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Pizza Panic")
pygame.display.toggle_fullscreen()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
MENU_BLUE = (104, 145, 195)

FPS = 60
CLOCK = pygame.time.Clock()

DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT = (64, 64)

LANE_1 = pygame.Rect((WIDTH - (WIDTH * 0.75)), 560,
                     (WIDTH * 0.75), (120)
                     )
LANE_2 = pygame.Rect((WIDTH - (WIDTH * 0.75)), 440,
                     (WIDTH * 0.75), (120)
                     )
LANE_3 = pygame.Rect((WIDTH - ((WIDTH * 0.75))), 320,
                     (WIDTH * 0.75), (120)
                     )
LANE_4 = pygame.Rect((WIDTH - (WIDTH * 0.75)), 200,
                     (WIDTH * 0.75), (120)
                     )

run_menu = True
run_intro = True

COUNTER = pygame.image.load(os.path.join(
    'JOGO-1SEM', 'Assets', 'Cenario', 'BalcaoTerminado.png'))
COUNTER = pygame.transform.scale(COUNTER, (WIDTH * 0.08, HEIGHT * 0.8))

sprite_sheets = []
menu_particles = []
particles_remove = []

def Jogo():
    Load_Sprite_Game()

    global holding_pizzas
    global hit_points

    # Listas
    lanes_pos = [LANE_1.y, LANE_2.y, LANE_3.y, LANE_4.y]
    mc_projectiles = []
    enemy_alive = []
    pizzas_in_line = []
    temp_pizza_sprite = []

    # hitboxes
    mc_hitbox = pygame.Rect(
        250, 360, DEFAULT_CHARACTER_WIDHT, DEFAULT_CHARACTER_HEIGHT)
    pizza_refill_zone = pygame.Rect(
        95, HEIGHT - (HEIGHT * 0.22) * 3, WIDTH * 0.05, HEIGHT * 0.70)
    enemy_basico_hitbox = pygame.Rect(WIDTH - DEFAULT_CHARACTER_WIDHT, (lanes_pos[randint(0, 3)]),
                                      DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT)

    # velocidades
    vel = 7.5
    projectile_vel = 8
    pizza_vel = 3
    enemy_vel = 5

    # limites
    max_pizzas_in_line = 7
    max_holding_pizzas = 2
    max_bounces = 20

    # atributos
    hit_points = 5
    holding_pizzas = 0
    bounce_yspeed = 3
    explosion_size = 300

    # Estados
    run = True
    playing = True

    # EVENTOS
    CustomEvent1 = pygame.event.custom_type() + 1
    SpawnEnemyEvent = pygame.event.Event(CustomEvent1)

    # ControleDeSpawn
    spawn_rate = 4000
    fire_rate = 3200

    # ControleDeSprites
    sprite_order = 0
    sprite_time = 64

    # Timers
    point_time = 0
    point_time1 = 0
    point_time2 = 0

    def ScreenUpdate():
        WIN.blit(Get_Sprite(0, 0, 320, 576, 7), (0, HEIGHT * 0.20))
        WIN.blit(Get_Sprite(0, 0, 960, 576, 6), (WIDTH * 0.25, HEIGHT * 0.20))
        
        show_hitboxes = True
        if show_hitboxes == True:
            pygame.draw.rect(WIN, WHITE, LANE_1)
            pygame.draw.rect(WIN, BLACK, LANE_2)
            pygame.draw.rect(WIN, WHITE, LANE_3)
            pygame.draw.rect(WIN, BLACK, LANE_4)
            pygame.draw.rect(WIN, BLACK, pizza_refill_zone)

            pygame.draw.rect(WIN, RED, mc_hitbox)

            for i in range(len(enemy_alive)):
                pygame.draw.rect(WIN, RED, enemy_alive[i][0])

            for i in range(len(mc_projectiles)):
                pygame.draw.rect(WIN, RED, mc_projectiles[i][0])

            for i in range(len(pizzas_in_line)):
                pygame.draw.rect(WIN, RED, pizzas_in_line[i][0])

        WIN.blit(COUNTER, (WIDTH * 0.24, HEIGHT * 0.2))

        WIN.blit(Get_Sprite(0 + (sprite_order % 6 + 1) * 64, 0, 64,
                 64, 2), (pizza_refill_zone.x, pizza_refill_zone.y))
        for i in range(0, 6):
            WIN.blit(Get_Sprite(0 + (sprite_order % 6 + 1) * 64, 64, 64, 64, 2),
                     (pizza_refill_zone.x, pizza_refill_zone.y + (i + 1) * 64))

        for i in range(len(pizzas_in_line)):
            WIN.blit(Get_Sprite(0 + (((pizzas_in_line[i][1][0]) % 3)*64),
                                0 + (((pizzas_in_line[i][1][0])//3)*64), 64, 64, 5),
                     (pizzas_in_line[i][0].x, pizzas_in_line[i][0].y)
                     )

        for i in range(len(enemy_alive)):
            WIN.blit(Get_Sprite(40 + (sprite_order % 3) * 128, 12 + (enemy_alive[i][1][1] * 128), 40, 92, 4),
                     (enemy_alive[i][0].x - 30, enemy_alive[i][0].y - 16)
                     )                     

        WIN.blit(Get_Sprite(0, 0, 1280, 720, 8), (0, 0))

        WIN.blit(Get_Sprite(223, 27 + (5 - hit_points)
                 * 44, 149, 38, 3), (1100, 40))

        for i in range(len(mc_projectiles)):
            if mc_projectiles[i][1][0] != 6:
                WIN.blit(pygame.transform.rotate(Get_Sprite(0 + (((mc_projectiles[i][1][0]) % 3)*64),
                                                            0 + (((mc_projectiles[i][1][0]) // 3)*64), 64, 64, 5),
                                                 (90*(sprite_order % 4))),
                         (mc_projectiles[i][0].x - 10,
                          mc_projectiles[i][0].y - 12)
                         )
            else:
                WIN.blit(
                    Get_Sprite(0 + (((mc_projectiles[i][1][0]) % 3)*64),
                               0 + (((mc_projectiles[i][1][0])//3)*64), 64, 64, 5),
                    (mc_projectiles[i][0].x - 10, mc_projectiles[i][0].y - 12)
                )



        WIN.blit(Get_Sprite(34 + (128 * (sprite_order % 18)),
                 32, 72, 64, 0), (mc_hitbox.x, mc_hitbox.y))

        pygame.display.update()

    def PositionHandling():
        global hit_is_taken
        hit_is_taken = 0

        for i in range(len(mc_projectiles)):
            mc_projectiles[i][0].x += projectile_vel
            if mc_projectiles[i][1][0] == 4 or mc_projectiles[i][1][0] == 5:

                if mc_projectiles[i][0].y < 150:
                    mc_projectiles[i][1][2] -= 1

                if mc_projectiles[i][0].y > HEIGHT - 64:
                    mc_projectiles[i][1][2] -= 1

                if mc_projectiles[i][1][2] % 2 == 0:
                    mc_projectiles[i][0].y -= projectile_vel

                else:
                    mc_projectiles[i][0].y += projectile_vel

            if mc_projectiles[i][0].x > 1180:
                mc_projectiles[i][1][1] = False
            elif mc_projectiles[i][0].x < 0:
                mc_projectiles[i][1][1] = False

        for i in range(len(enemy_alive)):
            if enemy_alive[i][0].x > WIDTH * 0.32:
                enemy_alive[i][0].x -= (enemy_alive[i][1][3])
            else:
                enemy_alive[i][1][2] = 0
                hit_is_taken += 1

        for i in range(len(pizzas_in_line)):
            if pizzas_in_line[i][0].y > 300 + ((i - 1) * 64):
                pizzas_in_line[i][0].y -= (pizzas_in_line[i][1][1]) // 1

    def ColissionHandling():
        global holding_pizzas
        global hit_points
        global hit_is_taken
        global game_over

        for i in range(len(mc_projectiles)):
            for i2 in range(len(enemy_alive)):
                if mc_projectiles[i][0].colliderect(enemy_alive[i2][0]) and mc_projectiles[i][1][1] == True:
                    if mc_projectiles[i][1][0] == 3:
                        mc_projectiles[i][0] = pygame.Rect(
                            mc_projectiles[i][0].x - (explosion_size *
                                                      1.5 - (mc_projectiles[i][0].w * 6) // 1),
                            mc_projectiles[i][0].y -
                            (explosion_size -
                             (mc_projectiles[i][0].h * 4) // 1),
                            explosion_size * 1.5, explosion_size
                        )
                        explosion()

                    if mc_projectiles[i][1][0] == 4 or mc_projectiles[i][1][0] == 5:
                        mc_projectiles[i][1][2] -= 1

                    elif mc_projectiles[i][1][0] != 3 and mc_projectiles[i][1][0] != 6:
                        mc_projectiles[i][1][1] = False
                    enemy_alive[i2][1][2] -= 1

        for i in range(len(pizzas_in_line)):
            if pizzas_in_line[i][0].colliderect(mc_hitbox):
                if holding_pizzas < max_holding_pizzas and pizzas_in_line[i][1][2] == True:
                    holding_pizzas += 1
                    pizzas_in_line[i][1][2] = False
                    temp_pizza_sprite.append(pizzas_in_line[i][1][0])

        if hit_is_taken > 0 and hit_points > 0:
            hit_points = hit_points - hit_is_taken

    def SpawnEnemy():
        enemy_hitbox = pygame.Rect(WIDTH + DEFAULT_CHARACTER_WIDHT,
                                   (lanes_pos[randint(0, 3)] + 40), DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT)
        enemy_stats = [0, randint(0, 3), 1, enemy_vel]
        enemy_alive.append([enemy_hitbox, enemy_stats])

    def SpawnProjectile():
        projectile = pygame.Rect(
            mc_hitbox.x + mc_hitbox.width, mc_hitbox.y + mc_hitbox.height/8, 40, 40)
        projectile_stats = [temp_pizza_sprite[0], True]
        if temp_pizza_sprite[0] == 4 or temp_pizza_sprite[0] == 5:
            projectile_stats.append(max_bounces)
            mc_projectiles.append([projectile, projectile_stats])

        else:
            mc_projectiles.append([projectile, projectile_stats])
        temp_pizza_sprite.pop(0)

    def SpawnPizza():
        global pizza_type_control  # variável de debug
        pizza_type_control = randint(0, 6)

        pizza = pygame.Rect(pizza_refill_zone.x, HEIGHT, 64, 64)
        pizza_stat = [pizza_type_control, pizza_vel, True]
        pizzas_in_line.append([pizza, pizza_stat])

    def RemoveEntities():
        for_removal = []
        for_removal2 = []
        for_removal3 = []
        for i in range(len(mc_projectiles)):
            if mc_projectiles[i][1][1] == False:
                for_removal.append(mc_projectiles[i])

            if mc_projectiles[i][1][0] == 4:
                if mc_projectiles[i][1][2] <= 0:
                    for_removal.append(mc_projectiles[i])

        for i in range(len(enemy_alive)):
            if enemy_alive[i][1][2] < 1:
                for_removal2.append(enemy_alive[i])

        for i in range(len(pizzas_in_line)):
            if pizzas_in_line[i][1][2] == False:
                for_removal3.append(pizzas_in_line[i])

        for i in range(len(for_removal)):
            mc_projectiles.remove(for_removal[i])

        for i in range(len(for_removal2)):
            enemy_alive.remove(for_removal2[i])

        for i in range(len(for_removal3)):
            pizzas_in_line.remove(for_removal3[i])

    def explosion():
        for i in range(len(mc_projectiles)):
            for i2 in range(len(enemy_alive)):
                if mc_projectiles[i][0].colliderect(enemy_alive[i2][0]) and mc_projectiles[i][1][1] == True:
                    enemy_alive[i2][1][3] -= 1
                    if i2 == len(enemy_basico_hitbox) - 1:
                        mc_projectiles[i][1][1] = False

    def Movement(keys_pressed, mc_hitbox):
        if keys_pressed[pygame.K_a] and mc_hitbox.x - vel > 0:
            mc_hitbox.x -= vel

        if keys_pressed[pygame.K_d] and (mc_hitbox.x + DEFAULT_CHARACTER_WIDHT) + vel < WIDTH // 4:
            mc_hitbox.x += vel

        if keys_pressed[pygame.K_w] and mc_hitbox.y - vel > 0 + ((HEIGHT * 0.20)):
            mc_hitbox.y -= vel

        if keys_pressed[pygame.K_s] and mc_hitbox.y + vel < HEIGHT - DEFAULT_CHARACTER_HEIGHT:
            mc_hitbox.y += vel

    while run:

        if playing == True:
            run_time = pygame.time.get_ticks()

        if run_time - point_time > spawn_rate and spawn_rate != 0:
            point_time = run_time
            pygame.event.post(SpawnEnemyEvent)

        if run_time - point_time1 > sprite_time:
            point_time1 = run_time
            sprite_order += 1

        if run_time - point_time2 > fire_rate and fire_rate != 0:
            if len(pizzas_in_line) < max_pizzas_in_line:
                point_time2 = run_time
                SpawnPizza()

        keys_pressed = pygame.key.get_pressed()
        Movement(keys_pressed, mc_hitbox)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MainMenu()

                if event.key == pygame.K_SPACE:
                    if holding_pizzas > 0:
                        SpawnProjectile()
                        holding_pizzas -= 1

                if event.key == pygame.K_ESCAPE:
                    run = False

            if event == SpawnEnemyEvent:
                SpawnEnemy()

        PositionHandling()
        ColissionHandling()
        RemoveEntities()
        ScreenUpdate()

        if hit_points <= 0:
            run = False
            GameOver()

        CLOCK.tick(FPS)


def GameOver():
    print("Game Over")


def MainMenu():
    global run
    global run_menu
    global particle_order
    global particle_order1

    point_time0 = 0
    point_time1 = 0
    particle_order = 0
    particle_order1 = 0

    particle_in_screen = 0

    while run_menu:
        WIN.fill(MENU_BLUE)

        run_time = pygame.time.get_ticks()

        if run_time - point_time0 > randint(0, 32) +  3 * len(menu_particles):
            point_time0 = run_time
            particle_order += 1
            Create_MenuParticle()

        if run_time - point_time1 > 32:
            point_time1 = run_time
            particle_order1 += 0.25

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    menu_particles.clear()
                    Jogo()
                if event.key == pygame.K_ESCAPE:
                    run_menu = False
        
        Handle_MenuParticle()

        pygame.display.update()

        CLOCK.tick(FPS)


def Load_Sprite_Game():

    mc_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Panda', 'Idle', 'Pizza_Panda_Idle.png')).convert()
    bg_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Cenario', 'MainCenario.png'))
    conveyor_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Cenario', 'Esteira.png'))
    HUD_hp_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Hud', 'Vida.png'))
    enemy_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Inimigos', 'Adultos.png'))
    projectile_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Itens', 'PizzasFinal.png'))
    chao_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Cenario', 'ChaoFinal.png'))
    cozinha_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Cenario', 'ChaoCozinha.png'))
    walls_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Cenario', 'Scenario_Walls.png'))

    bg_sheet = pygame.transform.scale(bg_sheet, (360, 485))
    mc_sheet = pygame.transform.scale(mc_sheet, (2304, 128))
    projectile_sheet = pygame.transform.scale(
        projectile_sheet, (768 * 0.25, 768 * 0.25))

    sprite_sheets.append(mc_sheet)
    sprite_sheets.append(bg_sheet)
    sprite_sheets.append(conveyor_sheet)
    sprite_sheets.append(HUD_hp_sheet)
    sprite_sheets.append(enemy_sheet)
    sprite_sheets.append(projectile_sheet)
    sprite_sheets.append(chao_sheet)
    sprite_sheets.append(cozinha_sheet)
    sprite_sheets.append(walls_sheet)


def Get_Sprite(x, y, w, h, sheet):
    sprite = pygame.Surface((w, h))
    sprite.set_colorkey((GREEN))
    sprite.blit(sprite_sheets[sheet], (0, 0), (x, y, w, h))
    return sprite


def Create_MenuParticle():
    particle_x = randint(20, 1260)
    particle_pos = [particle_x, randint(15, 50), -5]
    menu_particles.append([particle_pos, randint(2, 5), randint(4, 10), 
    randint(2,4), choice([-1, 1]), choice([0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1])])


def Handle_MenuParticle():
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    raio = 0

    for i in range(len(menu_particles)):

        menu_particles[i][0][2] -= - menu_particles[i][2]

        raio = (menu_particles[i][0][0] + menu_particles[i][0][1]) - menu_particles[i][0][0]
        x1 = menu_particles[i][0][0] + raio * sin((particle_order1 * menu_particles[i][4]) * menu_particles[i][5]) 
        y1 = menu_particles[i][0][2] + raio * cos((particle_order1 * menu_particles[i][4]) * menu_particles[i][5])
        x2 = menu_particles[i][0][0] - raio * sin((particle_order1 * menu_particles[i][4]) * menu_particles[i][5])
        y2 = menu_particles[i][0][2] - raio * cos((particle_order1 * menu_particles[i][4]) * menu_particles[i][5])

        pygame.draw.line(WIN, YELLOW, (x1, y1), (x2, y2), menu_particles[i][1])


    for i in range(len(menu_particles)): 
        if menu_particles[i][0][2] > 780:
            particles_remove.append(menu_particles[i])
    
    for i in range(len(particles_remove)):
        menu_particles.remove(particles_remove[i])

    particles_remove.clear()

    
def Intro():
    point_time = 0
    while run_intro:
        current = pygame.time.get_ticks()
        WIN.fill(BLACK)

        CLOCK.tick(FPS)


MainMenu()
pygame.quit()