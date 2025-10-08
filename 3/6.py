import pygame
pygame.init()
from pygame.color import THECOLORS
colors=["red","white","green","yellow","magenta"]
screen = pygame.display.set_mode([500,500])
screen.fill([0,0,0]) # цвет экрана черный
x=0
y=0
col=0
while x<500:
    pygame.draw.circle(screen, THECOLORS[colors[col]],[x,y], 20, 0)
    x=x+20
    y=y+20
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
