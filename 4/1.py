import pygame
pygame.init()
from pygame.color import THECOLORS
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
r = 20
x = r
y = 480 // 2
dx = 2
direction = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([255, 255, 255])
    x = x + dx * direction
    if x >= 640 - r:
        direction = -1
    elif x <= r:
        direction = 1
    pygame.draw.circle(screen, THECOLORS['blue'], [int(x), y], r, 0)
    pygame.time.delay(10)
    pygame.display.flip()
pygame.quit()
