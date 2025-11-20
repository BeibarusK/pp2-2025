import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
fps = 60
FramePerSec = pygame.time.Clock()
 
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
 
screen_w = 400
screen_h = 600
speed = 5
score = 0
score_plus = 0
coin_count = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("You lost", True, black)
 
background = pygame.image.load("AnimatedStreet.png")
 
display_s = pygame.display.set_mode((400,600))
display_s.fill(white)
pygame.display.set_caption("Knyaz Myshkin's Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_w-40), 0)  
 
    def move(self):
        global score
        global score_plus
        self.rect.move_ip(0,speed)
        if self.rect.top > 600:
            score += 1
            score_plus += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_w - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, y_pos):
        global r1
        super().__init__()
        coin = pygame.image.load("dollar.png")
        r1 = random.randint(25, 55)
        self.image = pygame.transform.scale(coin, (r1, r1))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, screen_w-50), y_pos)
        
    def move(self):
        pass
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed[K_a]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < screen_w and pressed[K_d]:
            self.rect.move_ip(5, 0)
 
P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

first_coin = Coin(P1.rect.centery)
coins.add(first_coin)
all_sprites.add(first_coin)

new_coin_e = pygame.USEREVENT + 2
pygame.time.set_timer(new_coin_e, 1500)
 
while True:
    for event in pygame.event.get(): 
        if event.type == new_coin_e:
            if len(coins) == 0:
                coin = Coin(P1.rect.centery)
                coins.add(coin)
                all_sprites.add(coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    display_s.blit(background, (0,0))
    
    score_count = font_small.render(str(score), True, black)
    display_s.blit(score_count, (10,10))

    if score_plus>=4:
        speed+=0.7
        score_plus=0
    

    coins_count = font_small.render(f"Coins: {coin_count}", True, black)
    display_s.blit(coins_count, (screen_w - 100, 10))

    for coin in coins:
        coin.rect.centery = P1.rect.centery

    for entity in all_sprites:
        display_s.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)          
        display_s.fill(red)
        display_s.blit(game_over, (90,250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        coin_count += 1
        size = coin.rect.width

        if size < 35:
            score += 1
            score_plus += 1
        elif 35 <= size <= 45:
            score += 2
            score_plus += 2
        else:
            score += 3
            score_plus += 3
        all_sprites.remove(coin)
         
    pygame.display.update()
    FramePerSec.tick(fps)