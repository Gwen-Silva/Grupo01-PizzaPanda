#puxa a lib do pygame pra dentro do arquivo
from os import system
from turtle import width
import pygame

#Definindo variáveis globais (Sempre deixo no começo pra ficar mais fácil de encontrar)
running = True

#todas as varaveis Maiusculas são valores constantes que não devem ser modificados dentro do código
WINDOW_HEIGHT = 768
WINDOW_WIDTH = 1024

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
DARKGREEN = (10,50,10)

VELOCITY = 20
FPS = 60


#inicializa a lib do joguenho.
pygame.init()

#Definindo o tamanho da Janela
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("I like to: MOVE IT!")

panda_image = pygame.image.load("./Assets/Pizza_Panda.png")
panda_rec = panda_image.get_rect()
panda_rec.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


#definindo o fps e o clock do jogo pra nada ficar ultra rápido
clock = pygame.time.Clock()


#Os jogos funcionam com base num loop, dentro desse loop sempre tentamos colocar o máximo de itens que
# o nosso jogo vai executar. Então aqui dentro tem o "cérebro" do jogo.
while running:
    #capturando os eventos
    for event in pygame.event.get():
        print(event)
        running = not event.type == pygame.QUIT

    keys = pygame.key.get_pressed()

    panda_rec.x -= VELOCITY if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and panda_rec.left > 0 else 0
    panda_rec.x += VELOCITY if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and panda_rec.right < WINDOW_WIDTH else 0
    panda_rec.y -= VELOCITY if (keys[pygame.K_UP] or keys[pygame.K_w]) and panda_rec.top > 0 else 0
    panda_rec.y += VELOCITY if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and panda_rec.bottom < WINDOW_HEIGHT else 0

    display_surface.fill((0,0,0))
    display_surface.blit(panda_image, panda_rec)
    pygame.display.update()

    #Força o loop aguardar o número definido pelo fps
    clock.tick(FPS)

pygame.quit()