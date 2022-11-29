import math
import pygame
from pygame.locals import *

radar = (100,100)
radar_len = 50
x = radar[0] + math.cos(math.radians(angle)) * radar_len
y = radar[1] + math.sin(math.radians(angle)) * radar_len

# then render the line radar->(x,y)
pygame.draw.line(screen, Color("black"), radar, (x,y), 1)