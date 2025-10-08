import pygame
pygame.init()
from pygame.color import THECOLORS
colors=["red","white","green","yellow","magenta"]
screen = pygame.display.set_mode([640,480])
screen.fill([0,0,0]) # цвет экрана черный
x=0
col=0
while x<640:
    pygame.draw.rect(screen, THECOLORS[colors[col]], (x, 220, 40, 40))
    x=x+40
    col=col+1
    if col==5:
        col=0
pygame.display.flip()
running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

