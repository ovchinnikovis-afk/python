import pygame
pygame.init()
from pygame.color import THECOLORS
colors = ["red", "white", "green", "yellow", "magenta"]
screen = pygame.display.set_mode([640, 480])
screen.fill([0, 0, 0])
size = 20
col = 0
while size < 480:
    left = 320 - size // 2
    top = 240 - size // 2
    pygame.draw.rect(screen, THECOLORS[colors[col]], [left, top, size, size], 2)
    size = size + 20
    col = col + 1
    if col == 5:
        col = 0
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()