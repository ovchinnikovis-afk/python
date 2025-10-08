import pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_radius = 20
ball_x = ball_radius
ball_y = ball_radius
speed = 5
direction = 0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    if direction == 0:
        ball_x += speed
        if ball_x >= WIDTH - ball_radius:
            direction = 1
            ball_x = WIDTH - ball_radius
    elif direction == 1:
        ball_y += speed
        if ball_y >= HEIGHT - ball_radius:
            direction = 2
            ball_y = HEIGHT - ball_radius
    elif direction == 2:
        ball_x -= speed
        if ball_x <= ball_radius:
            direction = 3
            ball_x = ball_radius
    elif direction == 3:
        ball_y -= speed
        if ball_y <= ball_radius:
            direction = 0
            ball_y = ball_radius
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()