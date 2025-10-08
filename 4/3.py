import pygame, random
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = (0, 0, 0)
CIRCLE_COLOR = (0, 0, 255)
circle_radius = 30
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
dx = 5
dy = 4
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    circle_x += dx
    circle_y += dy
    if circle_x - circle_radius <= 0 or circle_x + circle_radius >= WIDTH:
        dx = -dx
    if circle_y - circle_radius <= 0 or circle_y + circle_radius >= HEIGHT:
        dy = -dy
    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, CIRCLE_COLOR, (int(circle_x), int(circle_y)), circle_radius)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()