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


#inicializa a lib do joguenho.
pygame.init()

#Definindo o tamanho da Janela
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bota na tela pikachu!")

dragon_left_image = pygame.image.load("./Playground/Som_Imagem/Panda.jpeg")
dragon_left_rec = dragon_left_image.get_rect()
dragon_left_rec.topleft = (0,0)

dragon_right_image = pygame.image.load("./Playground/Som_Imagem/Panda.jpeg")
dragon_right_rec = dragon_left_image.get_rect()
dragon_right_rec.topright = (WINDOW_WIDTH,0)

system_font = pygame.font.Font('./Playground/Som_Imagem/BabyBlocks.ttf', 32)
custom_font = pygame.font.Font('./Playground/Som_Imagem/Pixelhour.ttf', 32)

pygame.mixer.music.load('./Playground/Som_Imagem/Menu.wav')
pygame.mixer.music.play(-1, 0.0, -2)

#Os jogos funcionam com base num loop, dentro desse loop sempre tentamos colocar o máximo de itens que
# o nosso jogo vai executar. Então aqui dentro tem o "cérebro" do jogo.
while running:
    #capturando os eventos
    for event in pygame.event.get():
        print(event)
        running = not event.type == pygame.QUIT

    system_text = system_font.render("Pizza Panda Studios", True, GREEN, DARKGREEN)
    system_text_rect = system_text.get_rect()
    system_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

    system_custom = custom_font.render("Pizza Panda Studios", True, GREEN, DARKGREEN)
    system_custom_rect = system_custom.get_rect()
    system_custom_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)

    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(system_custom, system_custom_rect)

    display_surface.blit(dragon_left_image, dragon_left_rec)
    display_surface.blit(dragon_right_image, dragon_right_rec)
    pygame.display.update()

pygame.quit()