import os
import sys
import pygame
from math import sin, cos
from pygame.locals import *
from pygame import mixer
from random import randint, choice

pygame.init()


directory = os.getcwd()

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
ALLPIZZA = pygame.font.Font(os.path.join(directory, 'Assets', 'Fontes', 'Allpizza-Regular.ttf'), 64)

DEFAULT_CHARACTER_HEIGHT, DEFAULT_CHARACTER_WIDHT = (64, 64)

music = False

sprite_sheets = []
menu_particles = []
particles_remove = []

def Jogo():

    global holding_pizzas
    global hit_points
    global music
    
    mixer.music.load(os.path.join('JOGO-1SEM', 'Assets', 'Sons', 'In game Hijinx.wav'))
    mixer.music.play(-1)

    # Listas
    mc_projectiles = []
    enemy_alive = []
    pizzas_in_line = []
    temp_pizza_sprite = []
    explosions = []

    # hitboxes
    mc_hitbox = pygame.Rect(
        250, 360, DEFAULT_CHARACTER_WIDHT, DEFAULT_CHARACTER_HEIGHT)
    pizza_refill_zone = pygame.Rect(
        95, HEIGHT - (HEIGHT * 0.22) * 3, WIDTH * 0.05, HEIGHT * 0.70)
    pizza_hold_hud = pygame.Rect(123, 74, 128, 64)

    # velocidades
    vel = 6
    projectile_vel = 4
    pizza_vel = 2
    enemy_vel = 1

    # limites
    max_pizzas_in_line = 8
    max_holding_pizzas = 2

    # atributos
    hit_points = 5
    holding_pizzas = 0

    # Estados
    run = True
    playing = True
    interval = False
    mc_running = False
    mc_throwing = False

    # EVENTOS
    CustomEvent1 = pygame.event.custom_type() + 1
    SpawnEnemyEvent = pygame.event.Event(CustomEvent1)

    # ControleDeSpawn
    spawn_rate = 4000
    fire_rate = 4000

    # Controles
    sprite_order = 0
    sprite_time = 112
    throw_sprite = 0
    round_split = 0
    round = 0

    # Timers
    point_time = 0
    point_time1 = 0
    point_time2 = 0
    point_time3 = 0
    point_time4 = 0
    point_time5 = 0

    def ScreenUpdate():

        holding_pizzas_cords = [(mc_hitbox.x + 40, mc_hitbox.y + 25), (mc_hitbox.x + 40, mc_hitbox.y + 19)]

        WIN.blit(Get_Sprite(0, 0, 320, 576, 7), (0, HEIGHT * 0.20))
        WIN.blit(Get_Sprite(0, 0, 960, 576, 6), (WIDTH * 0.25, HEIGHT * 0.20))
        
        show_hitboxes = False
        if show_hitboxes == True:
            pygame.draw.rect(WIN, BLACK, pizza_refill_zone)

            pygame.draw.rect(WIN, RED, mc_hitbox)

            for i in range(len(explosions)):
                pygame.draw.rect(WIN, RED, explosions[i])            

            for i in range(len(enemy_alive)):
                pygame.draw.rect(WIN, RED, enemy_alive[i][0])

            for i in range(len(mc_projectiles)):
                pygame.draw.rect(WIN, RED, mc_projectiles[i][0])

            for i in range(len(pizzas_in_line)):
                pygame.draw.rect(WIN, RED, pizzas_in_line[i][0])


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
                     (enemy_alive[i][0].x - 4, enemy_alive[i][0].y - 8)
                     )                     

        WIN.blit(Get_Sprite(0, 0, 1280, 720, 8), (0, 0))

        WIN.blit(Get_Sprite(0, 0, 60, 537, 9), (320, 155))

        WIN.blit(Get_Sprite(223, 27 + (5 - hit_points)
                 * 44, 149, 38, 3), (278, 75))
        
        WIN.blit(Get_Sprite(2 + 64 * (round_split % 5), 1, 61, 63, 13), (1120, 65))

        WIN.blit(Get_Sprite(0, 0, 128, 64, 17), (pizza_hold_hud.x, pizza_hold_hud.y))

        for i in range(len(temp_pizza_sprite)):
            WIN.blit(Get_Sprite(0 + (((temp_pizza_sprite[i]) % 3)*64),
                                0 + (((temp_pizza_sprite[i])//3)*64), 64, 64, 5), 
                                (pizza_hold_hud.x + 64 * i, pizza_hold_hud.y)
                            )

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
        
        for i in range(len(explosions)):
            WIN.blit(ALLPIZZA.render('kaboom', True, 'Black'), (explosions[i][0] + (explosions[i][2] * 0.5) - 80, explosions[i][1] + (explosions[i][3] * 0.5) - 50))

        if mc_throwing:
            WIN.blit(Get_Sprite(34 + (128 * (throw_sprite % 3)),
                    31, 64, 64, 15), (mc_hitbox.x, mc_hitbox.y))

        elif not mc_running:
            WIN.blit(Get_Sprite(34 + (128 * (sprite_order % 18)),
                    32, 54, 64, 0), (mc_hitbox.x, mc_hitbox.y))
        else:
            WIN.blit(Get_Sprite(34 + (128 * (sprite_order % 2)),
                    31, 54, 64, 14), (mc_hitbox.x, mc_hitbox.y))

        if holding_pizzas == 1:
            WIN.blit(Get_Sprite(0, 12, 32, 8, 16), (holding_pizzas_cords[0]))

        elif holding_pizzas == 2:
            for i in range(len(holding_pizzas_cords)):
                WIN.blit(Get_Sprite(0, 12, 32, 8, 16), (holding_pizzas_cords[i]))

        pygame.display.update()

    def PositionHandling():
        global hit_is_taken
        hit_is_taken = 0

        for i in range(len(mc_projectiles)):
            if mc_projectiles[i][1][0] != 6:
                mc_projectiles[i][0].x += projectile_vel
            else:
                mc_projectiles[i][0].x += projectile_vel * 0.7

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
            if enemy_alive[i][0].x > 380:
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
                        explosions.append(mc_projectiles[i][0])
                        mc_projectiles[i][1][1] = False

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

        if explosions != []:
            for i in range(len(explosions)):
                for i2 in range(len(enemy_alive)):
                    if explosions[i].colliderect(enemy_alive[i][0]):
                        enemy_alive[i][1][2] -= 1

        if hit_is_taken > 0 and hit_points > 0:
            hit_points = hit_points - hit_is_taken

    def SpawnEnemy():
        enemy_hitbox = pygame.Rect(WIDTH + DEFAULT_CHARACTER_WIDHT,
                                   (choice([210, 250, 300, 350, 400, 450, 500, 550, 600])), 
                                   DEFAULT_CHARACTER_WIDHT * 0.5, DEFAULT_CHARACTER_HEIGHT * 1.2)
        enemy_stats = [0, randint(0, 3), 1, enemy_vel]
        enemy_alive.append([enemy_hitbox, enemy_stats])

    def SpawnProjectile():
        projectile = pygame.Rect(
            mc_hitbox.x + mc_hitbox.width, mc_hitbox.y + mc_hitbox.height/8, 40, 40)
        projectile_stats = [temp_pizza_sprite[0], True]
        if temp_pizza_sprite[0] == 4 or temp_pizza_sprite[0] == 5:
            projectile_stats.append(1)
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
        for_removal4 = []
        for i in range(len(mc_projectiles)):
            if mc_projectiles[i][1][1] == False:
                for_removal.append(mc_projectiles[i])

        for i in range(len(enemy_alive)):
            if enemy_alive[i][1][2] < 1:
                for_removal2.append(enemy_alive[i])

        for i in range(len(pizzas_in_line)):
            if pizzas_in_line[i][1][2] == False:
                for_removal3.append(pizzas_in_line[i])
        
        for i in range(len(explosions)):
            if explosions[i][3] > 500:
                for_removal4.append(explosions[i])

        for i in range(len(for_removal)):
            mc_projectiles.remove(for_removal[i])

        for i in range(len(for_removal2)):
            enemy_alive.remove(for_removal2[i])

        for i in range(len(for_removal3)):
            pizzas_in_line.remove(for_removal3[i])
        
        for i in range(len(for_removal4)):
            explosions.remove(for_removal4[i])

    def explosion():
        for i in range(len(explosions)):
            explosions[i][0] -= 200
            explosions[i][1] -= 200
            explosions[i][2] += 400
            explosions[i][3] += 400

    def Movement(keys_pressed, mc_hitbox):
        global running

        if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) and mc_hitbox.x - vel > 90:
            mc_hitbox.x -= vel
        elif mc_hitbox.x - vel <= 90:
            mc_hitbox.x = 91

        if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) and (mc_hitbox.x + DEFAULT_CHARACTER_WIDHT) + vel < 350:
            mc_hitbox.x += vel

        elif (mc_hitbox.x + DEFAULT_CHARACTER_WIDHT) + vel > 350:
            mc_hitbox.x = 346 - DEFAULT_CHARACTER_WIDHT

        if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]) and mc_hitbox.y - vel > 0 + ((HEIGHT * 0.20)):
            mc_hitbox.y -= vel

        if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN])  and mc_hitbox.y + vel < HEIGHT - DEFAULT_CHARACTER_HEIGHT - 28:
            mc_hitbox.y += vel
        elif mc_hitbox.y + vel >= HEIGHT - DEFAULT_CHARACTER_HEIGHT - 28: 
            mc_hitbox.y = HEIGHT - DEFAULT_CHARACTER_HEIGHT - 29

    while run:

        mc_running = False

        if playing == True:
            run_time = pygame.time.get_ticks()

        if run_time - point_time > spawn_rate and not interval:
            point_time = run_time
            pygame.event.post(SpawnEnemyEvent)

        if run_time - point_time1 > sprite_time:
            point_time1 = run_time
            sprite_order += 1
            if explosions != []:
                explosion()

        if run_time - point_time2 > fire_rate and fire_rate != 0:
            if len(pizzas_in_line) < max_pizzas_in_line:
                point_time2 = run_time
                SpawnPizza()
        
        if run_time - point_time3 > 6400 and round_split < 4:
                point_time3 = run_time
                round_split += 1
        
        if round_split == 4:
            round_split = 5
            point_time4 = run_time
            interval = True

        if round_split == 5 and run_time - point_time4 > 6400:
            round_split = 0
            round += 1
            interval = False
            spawn_rate = spawn_rate * 0.90
            fire_rate = fire_rate * 0.95
            if round % 3 == 0:
                enemy_vel = enemy_vel * 1.15

        if run_time - point_time5 > 64 and throw_sprite < 3 and mc_throwing == True:
            point_time5 = run_time
            throw_sprite += 1 
          
        if throw_sprite > 2:
            mc_throwing = False
            throw_sprite = 0

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_w] or keys_pressed[pygame.K_s] or keys_pressed[pygame.K_a] or keys_pressed[pygame.K_d] or keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT]:
            Movement(keys_pressed, mc_hitbox)
            mc_running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    music = False
                    run = False

                if event.key == pygame.K_SPACE and mc_throwing == False:
                    if holding_pizzas > 0:
                        SpawnProjectile()
                        holding_pizzas -= 1
                        mc_throwing = True
                
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
    global music
    music = False
    run = True

    point_time = 0
    order = 0

    mixer.music.fadeout(3200)
    while run:
        run_time = pygame.time.get_ticks()

        if run_time - point_time > 16:
            order += 6
        
        if order <= 720:
            WIN.blit(Get_Sprite(0, 0, 1280, 720, 12), (0, HEIGHT - order))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if order > 1200:
            run = False
            WIN.fill(MENU_BLUE)
            pygame.display.update()


        CLOCK.tick(FPS)



def MainMenu():
    global run
    global run_menu
    global particle_order
    global particle_order1
    global music

    point_time0 = 0
    point_time1 = 0
    particle_order = 0
    particle_order1 = 0

    click = False

    start_button = pygame.Rect(295, 560, 230, 72)
    close_button = pygame.Rect(755, 560, 230, 72)

    run_menu = True

    while run_menu:
        if music == False:
            mixer.music.load(os.path.join('JOGO-1SEM', 'Assets', 'Sons', 'menu.wav'))
            mixer.music.play(-1)
            music = True
        
        mouseX, mouseY = pygame.mouse.get_pos()

        WIN.fill(MENU_BLUE)

        run_time = pygame.time.get_ticks()

        if run_time - point_time0 > randint(0, 16) +  1 * len(menu_particles):
            point_time0 = run_time
            particle_order += 1
            Create_MenuParticle()

        if run_time - point_time1 > 32:
            point_time1 = run_time
            particle_order1 += 0.25
        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if start_button.collidepoint((mouseX, mouseY)):
            if click == True:
                menu_particles.clear()
                Jogo()

        if close_button.collidepoint((mouseX, mouseY)):
            if click == True:
                run_menu = False
    
        Handle_MenuParticle()

        WIN.blit(Get_Sprite(26, 68, 460 ,386, 11), (410, 20))
        WIN.blit(Get_Sprite(15, 84, 230 ,72, 10), (start_button.x, start_button.y))
        WIN.blit(Get_Sprite(12, 350, 230 ,72, 10), (close_button.x, close_button.y))

        pygame.display.update()

        CLOCK.tick(FPS)


def Load_Sprite_Game():

    mc_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Panda', 'Pizza_Panda_Without_Pizza_Idle.png')).convert()
    bg_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Cenario', 'MainCenario.png')).convert()
    conveyor_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Cenario', 'Esteira.png')).convert()
    HUD_hp_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Hud', 'Vida.png'))
    enemy_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Inimigos', 'Adultos.png')).convert()
    projectile_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Itens', 'PizzasFinal.png')).convert()
    chao_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Cenario', 'ChaoFinal.png')).convert()
    cozinha_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Cenario', 'ChaoCozinha.png')).convert()
    walls_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Cenario', 'Scenario_Walls.png')).convert()
    counter_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Cenario', 'Balcão.png')).convert()
    botoes_menu_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Gui', 'Botoes.png')).convert()
    titulo_menu_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Gui', 'Titulo.png')).convert()
    game_over_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Gui', 'Tela de game over.png')).convert()
    timer_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Hud', 'Timer.png')).convert()    
    mc_running_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Panda', 'Pizza_Panda_Without_Pizza_Walking.png')).convert()   
    mc_throw_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Panda', 'Pizza_Panda_Without_Pizza_Throw.png')).convert()
    pizza_box_sheet = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Itens', 'Pizza_Box.png')).convert()
    HUD_holding_pizza = pygame.image.load(os.path.join(
        'JOGO-1SEM', 'Assets', 'Hud', 'HoldingPizzas.png')).convert()    

    bg_sheet = pygame.transform.scale(bg_sheet, (360, 485))
    mc_sheet = pygame.transform.scale(mc_sheet, (2304, 128))
    projectile_sheet = pygame.transform.scale(
        projectile_sheet, (768 * 0.25, 768 * 0.25))
    botoes_menu_sheet = pygame.transform.scale(botoes_menu_sheet, (512 * 0.5, 1024 * 0.5))
    mc_running_sheet = pygame.transform.scale(mc_running_sheet, (256, 128))
    mc_throw_sheet = pygame.transform.scale(mc_throw_sheet, (384, 128))
    pizza_box_sheet = pygame.transform.scale(pizza_box_sheet, (32, 32))


    sprite_sheets.append(mc_sheet) #0
    sprite_sheets.append(bg_sheet) #1
    sprite_sheets.append(conveyor_sheet) #2
    sprite_sheets.append(HUD_hp_sheet) #3
    sprite_sheets.append(enemy_sheet) #4
    sprite_sheets.append(projectile_sheet) #5
    sprite_sheets.append(chao_sheet) #6
    sprite_sheets.append(cozinha_sheet) #7
    sprite_sheets.append(walls_sheet) #8
    sprite_sheets.append(counter_sheet) #9
    sprite_sheets.append(botoes_menu_sheet) #10
    sprite_sheets.append(titulo_menu_sheet) #11
    sprite_sheets.append(game_over_sheet) #12
    sprite_sheets.append(timer_sheet) #13
    sprite_sheets.append(mc_running_sheet) #14
    sprite_sheets.append(mc_throw_sheet) #15
    sprite_sheets.append(pizza_box_sheet) #16
    sprite_sheets.append(HUD_holding_pizza) #17


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

        raio = menu_particles[i][0][1]
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

Load_Sprite_Game()
MainMenu()
pygame.quit()
sys.exit()