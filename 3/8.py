import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
strip_height = 50
strip_y = 200
strip_height1 = 50
strip_y1 = 100
strip_height2 = 50
strip_y2 = 300
for x in range(640):
    intensity = int(255 * (1 - x / 639))
    color = (0, 0, intensity)
    pygame.draw.line(screen, color, [x, strip_y], [x, strip_y + strip_height], 1)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()