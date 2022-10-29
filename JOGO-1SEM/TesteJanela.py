#puxa a lib do pygame pra dentro do arquivo
from Hero import Hero
import pygame
from pygame.locals import *

#Definindo variáveis globais (Sempre deixo no começo pra ficar mais fácil de encontrar)
running = True

#todas as varaveis Maiusculas são valores constantes que não devem ser modificados dentro do código
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
SCENARIO_FLOOR = 560
FPS = 75


#inicializa a lib do joguenho.
pygame.init()

#Definindo o tamanho da Janela
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), HWSURFACE | DOUBLEBUF)
pygame.display.set_caption("I like to: MOVE IT!")

background_image = pygame.image.load("./Assets/Background.jpg")

characters = pygame.sprite.LayeredUpdates()
hero = Hero(SCENARIO_FLOOR, WINDOW_WIDTH)
characters.add(hero)

#pygame.mixer.music.load('Menu.wav')
#pygame.mixer.music.play(-1, 0.0, -2)

#definindo o fps e o clock do jogo pra nada ficar ultra rápido
clock = pygame.time.Clock()


#Os jogos funcionam com base num loop, dentro desse loop sempre tentamos colocar o máximo de itens que
# o nosso jogo vai executar. Então aqui dentro tem o "cérebro" do jogo.
while running:
    #capturando os eventos
    for event in pygame.event.get():
        running = not event.type == pygame.QUIT

    hero.Move()    
    hero.idle()
    hero.update(0.25)

    characters.add(hero)

    display_surface.fill((0,0,0))
    display_surface.blit(background_image, (0,0))
    characters.draw(display_surface)
    pygame.display.update()

    #Força o loop aguardar o número definido pelo fps
    clock.tick(FPS)

pygame.quit()