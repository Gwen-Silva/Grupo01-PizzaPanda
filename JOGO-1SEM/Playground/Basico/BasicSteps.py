#puxa a lib do pygame pra dentro do arquivo
import pygame

#Definindo variáveis globais (Sempre deixo no começo pra ficar mais fácil de encontrar)
running = True

#todas as varaveis Maiusculas são valores constantes que não devem ser modificados dentro do código
WINDOW_HEIGHT = 300
WINDOW_WIDTH = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)


#inicializa a lib do joguenho.
pygame.init()

#Definindo o tamanho da Janela
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello Wordl!")

display_surface.fill(BLUE)

#Desenha uma linha na tela. Você tem que indicar os seguintes itens
# display_surface = aqui é em qual tela isso será desenhado
# (0,0) Posição inicial, 
# (100,100) Posição final
# 5 Grossura da linha
pygame.draw.line(display_surface, RED, (0,0), (100,100), 5)
pygame.draw.line(display_surface, GREEN, (100,100), (200,300), 1)


#Desenha um circulo na tela. Você tem que indicar os seguintes itens
# display_surface = aqui é em qual tela isso será desenhado
# WHITE Cor do círculo
# (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) Posição do círculo (aqui usamos '//' pra garantir que o resto da divisão vai ser um inteiro), 
# 200 Raio do círculo
# 6 tamanho do círculo
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 195, 0)

#Desenha um retângulo na tela. Você tem que indicar os seguintes itens
# display_surface = aqui é em qual tela isso será desenhado
# WHITE Cor do círculo
# (500, 0, 100,100) os 4 parâmetros da tupla são os seguintes
# 500 posição X
# 0 posição y
# 100 altura
# 100 largura
pygame.draw.rect(display_surface, CYAN, (500, 0, 100,100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50,100))


#Os jogos funcionam com base num loop, dentro desse loop sempre tentamos colocar o máximo de itens que
# o nosso jogo vai executar. Então aqui dentro tem o "cérebro" do jogo.
while running:
    #capturando os eventos
    for event in pygame.event.get():
        print(event)
        running = not event.type == pygame.QUIT

    pygame.display.update()

pygame.quit()