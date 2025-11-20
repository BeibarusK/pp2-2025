import pygame
from pygame.locals import *
import random

pygame.init()

running = True
speed = 10

up = 0
down = 1
left = 2
right = 3

level = 0
score = 0

clock = pygame.time.Clock()

the_dissapearing = pygame.USEREVENT+1
pygame.time.set_timer(the_dissapearing, 5000)

class Snake():
    def __init__(self):
        self.body = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
        self.body_color = pygame.Surface((10,10))
        self.body_color.fill((168, 8, 249))
        self.head_color = pygame.Surface((10,10))
        self.head_color.fill((200, 200, 200))
        self.direction = right

    def move(self):
        head_x, head_y = self.body[-1]
        
        if self.direction == right:
            new_head = (head_x + 10, head_y)
        elif self.direction == up:
            new_head = (head_x, head_y - 10)
        elif self.direction == down:
            new_head = (head_x, head_y + 10)
        elif self.direction == left:        
            new_head = (head_x - 10, head_y)
            
        self.body.append(new_head)
        self.body.pop(0)

    def hit_self(self):
        head = self.body[-1]
        body = self.body[:-1]
        return head in body
    
    def hit_wall(self, screen_size):
        x, y = self.body[-1]
    
        if x >= screen_size: 
            return True
        if x < 0: 
            return True  
        if y >= screen_size: 
            return True
        if y < 0: 
            return True
    
        return False

    def eat_apple(self, apple_pos):
        return self.body[-1] == apple_pos
    
    def grow(self):
        self.body.insert(0, self.body[0])


class Apple():
    def __init__(self):
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.pos = (0, 0)
        self.random_pos(400)
    
    def random_pos(self, screen_size):
        x = random.randrange(0, screen_size, 10)
        y = random.randrange(0, screen_size, 10)
        self.pos = (x, y)

class Banana():
    def __init__(self):
        self.image = pygame.Surface((10, 10))
        self.image.fill((249, 252, 41))
        self.pos = (0, 0)
        self.random_pos(400)
    
    def random_pos(self, screen_size):
        x = random.randrange(0, screen_size, 10)
        y = random.randrange(0, screen_size, 10)
        self.pos = (x, y)

class Orange():
    def __init__(self):
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 133, 1))
        self.pos = (0, 0)
        self.random_pos(400)
    
    def random_pos(self, screen_size):
        x = random.randrange(0, screen_size, 10)
        y = random.randrange(0, screen_size, 10)
        self.pos = (x, y)


screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
snake = Snake()
apple = Apple()
banana = Banana()
orange = Orange()
pygame.display.set_caption("Oblomov's snake game")


while running:
    clock.tick(speed)
    snake.move()
    font = pygame.font.SysFont('Times New Roman', 20)
    text = font.render(f"Level {level}", True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                running = False

            elif event.key==K_w and snake.direction != down:
                snake.direction = up 

            elif event.key==K_a and snake.direction != right:
                snake.direction = left

            elif event.key==K_s and snake.direction != up:                
                snake.direction = down

            elif event.key==K_d and snake.direction != left:
                snake.direction = right

        if event.type == the_dissapearing:
            apple.random_pos(400)
            orange.random_pos(400)
            banana.random_pos(400)
    
    if snake.hit_wall(400) or snake.hit_self():
        running  = False

    if snake.eat_apple(apple.pos):
        apple.random_pos(400)
        score += 1
        snake.grow()
        if score >= 3:
            speed += 0.9
            level += 1
            score = 0

    if snake.eat_apple(banana.pos):
        banana.random_pos(400)
        score += 2
        snake.grow()
        if score >= 3:
            speed += 0.9
            level += 1
            score = 0

    if snake.eat_apple(orange.pos):
        orange.random_pos(400)
        score += 3
        snake.grow()
        if score >= 3:
            speed += 0.9
            level += 1
            score = 0
    
    screen.fill((0,0,0))
    for snake_pos in snake.body[0:-1]:
        screen.blit(snake.body_color, snake_pos)
    screen.blit(snake.head_color, snake.body[-1])
    screen.blit(banana.image, banana.pos)
    screen.blit(apple.image, apple.pos)
    screen.blit(orange.image, orange.pos)
    screen.blit(text,(1, 1))

    pygame.display.update()

pygame.quit()