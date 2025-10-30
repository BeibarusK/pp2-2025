import pygame
import datetime


pygame.init()


width, height = 1440, 1000

screen = pygame.display.set_mode((width, height))


pygame.display.set_caption("Dostoevsky's mickey clock")
mickey_clock = pygame.image.load('base_micky.jpg')
minute = pygame.image.load("minute.png")
second = pygame.image.load("second.png")

running = True

while running:
    screen.blit(mickey_clock, (10, 5))

    t = datetime.datetime.now()
    sec = t.second
    minu = t.minute

    sec_angle = -sec * 6
    min_angle = -(minu * 6 + sec / 10) - 45

    r_sec = pygame.transform.rotate(second, sec_angle)
    r_min = pygame.transform.rotate(minute, min_angle)

    screen.blit(r_min, r_min.get_rect(center=(720, 530)))
    screen.blit(r_sec, r_sec.get_rect(center=(720, 530)))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()