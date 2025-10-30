from pygame import mixer
import pygame

pygame.init()
mixer.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Chehov's music player")

font = pygame.font.SysFont('Times New Roman', 50)
text = font.render("Chehov's MP3 player", True, (252, 252, 252))

songs_of_Chehov = ["ForestWalk-320bit(chosic.com).mp3", "Reaching-Out(chosic.com).mp3", "Winter-Long-Version(chosic.com).mp3"]
i = 0

mixer.music.load(songs_of_Chehov[i])

running = True
while running:
    screen.fill((189, 0, 252))
    screen.blit(text, (350, 250))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer.music.play()

            elif event.key == pygame.K_s:
                mixer.music.pause()

            elif event.key == pygame.K_w:
                mixer.music.unpause()

            elif event.key == pygame.K_d:
                i += 1
                if i >= len(songs_of_Chehov):
                    i = 0
                mixer.music.load(songs_of_Chehov[i])
                mixer.music.play()

            elif event.key == pygame.K_a:
                i -= 1
                if i < 0:
                    i = len(songs_of_Chehov) - 1
                pygame.mixer.music.load(songs_of_Chehov[i])
                pygame.mixer.music.play()

            elif event.key == pygame.K_q:
                mixer.music.stop()
                running = False