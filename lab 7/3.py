import pygame

pygame.init()

width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
x = width // 2
y = height // 2
radius = 25

pygame.display.set_caption("Red Swan")

running = True

while running:
    screen.fill((252, 252, 252))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and y + radius + 20 <= height:
                y += 20
            elif event.key == pygame.K_w and y - radius - 20 >= 0:
                y -= 20
            elif event.key == pygame.K_a and x - radius - 20 >= 0:
                x -= 20
            elif event.key == pygame.K_d and x + radius + 20 <= width:
                x += 20

    pygame.draw.circle(screen, 'Red', (x, y), 25)

    
    pygame.display.update()