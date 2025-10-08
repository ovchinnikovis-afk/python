import pygame, random
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen_width, screen_height = 800, 600
screen.fill([0, 0, 0])
r = 2
z = random.randint(50, 100)
text_y = z
text_x = random.randint(z, 600 - z)
dtext_y = 6
R = random.randint(0, 255)
G = random.randint(0, 255)
B = random.randint(0, 255)
p = ([R, G, B])
font = pygame.font.Font(None, z)
text = font.render("*", 1, p, [R, G, B])
screen.blit(text, [text_x, text_y])
pygame.display.flip()
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([0, 0, 0])
    text_y = text_y + dtext_y
    font = pygame.font.Font(None, z)
    text = font.render("*", 1, p)
    screen.blit(text, [text_x, text_y])
    if 0 <= text_y - r <= screen_width:
        text = font.render("*", 1, p)
    else:
        z = random.randint(50, 100)
        text_x = random.randint(r, 232)
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        p = ([R, G, B])
        screen.fill([0, 0, 0])
        z = random.randint(50, 100)
        text_y = 0
        text_y = text_y + dtext_y
        font = pygame.font.Font(None, z)
        text = font.render("*", 1, p)
        screen.blit(text, [text_x, text_y])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()



