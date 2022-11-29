from math import sin, cos
import pygame

pygame.init()

WIN = pygame.display.set_mode((400, 400))
BLACK = 0, 0, 0
angle = 0
run = True
ponto0x = 200
ponto0y = 200


x1 = 0
y1 = 0
x2 = 0

while run:
    angle += 0.001
    raio = (x1 + x2) * 0.10

    #ponto0y += 0.01
    x1 = ponto0x + raio * sin(angle)
    y1 = ponto0y + raio * cos(angle)

    x2 = ponto0x - raio * sin(angle)
    y2 = ponto0y - raio * cos(angle)

    #WIN.fill(BLACK)

    pygame.draw.line(WIN, (255, 0, 0), (x1, y1), (x2, y2), 5)
    pygame.draw.line(WIN, (255, 0, 0), (150, 300), (250, 300), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()