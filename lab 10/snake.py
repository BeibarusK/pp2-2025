import pygame
from pygame.locals import *
import random
import sys
import time
import psycopg2


def connect_db():
    return psycopg2.connect(
        host="localhost",
        dbname="snake",
        user="postgres",
        password="1845"
    )

def get_user_id(username):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s", (username,))
            user = cur.fetchone()
            if user:
                return user[0]
            else:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                new_id = cur.fetchone()[0]
                conn.commit()
                return new_id

def load_progress(user_id):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT score, level 
                FROM user_score 
                WHERE user_id = %s 
                ORDER BY saved_at DESC 
                LIMIT 1
            """, (user_id,))
            row = cur.fetchone()
            return row if row else (0, 0)

def save_progress(user_id, score, level):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_score (user_id, score, level)
                VALUES (%s, %s, %s)
            """, (user_id, score, level))
            conn.commit()
    print(f"Progress saved: user_id={user_id}, score={score}, level={level}")

username = input("Enter your username: ")
user_id = get_user_id(username)
score, level = load_progress(user_id)

pygame.init()

running = True
speed = 10

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Purple = (128, 0, 128)
Pink = (255, 192, 203)
Gray = (128, 128, 128)


up = 0
down = 1
left = 2
right = 3
font = pygame.font.SysFont("Arial", 24)
level = 0
score = 0
score_cnt = 0
width, height = 600, 600
cell_s = 20

grid_width = width // cell_s
grid_height = height // cell_s

clock = pygame.time.Clock()
def get_level(score):
    if score < 5:
        return 0
    elif score < 10:
        return 1
    else:
        return 2

def get_speed(level):
    if level == 0:
        return 8
    elif level == 1:
        return 12
    else:
        return 15

game_over = False
level = get_level(score)
speed = get_speed(level)
the_dissapearing = pygame.USEREVENT+1
pygame.time.set_timer(the_dissapearing, 5000)


def pause_game():
    save_progress(user_id, score, level)

    paused_text = font.render("Paused: Press C to continue, Q to quit", True, Yellow)
    paused = True
    while paused:
        screen.fill(Black)
        screen.blit(paused_text, (width//2 - paused_text.get_width()//2, height//2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(user_id, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    save_progress(user_id, score, level)
                    pygame.quit()
                    sys.exit()

class Snake():
    def __init__(self):
        start_x, start_y = 10 * cell_s, 10 * cell_s
        self.body = [
            (start_x, start_y),
            (start_x - cell_s, start_y), 
            (start_x - 2 * cell_s, start_y),
            (start_x - 3 * cell_s, start_y),
            (start_x - 4 * cell_s, start_y)
        ]

        self.body_color = pygame.Surface((cell_s, cell_s))
        self.body_color.fill((168, 8, 249))
        self.head_color = pygame.Surface((cell_s, cell_s))
        self.head_color.fill((200, 200, 200))
        self.direction = right


    def move(self):
        head_x, head_y = self.body[-1]
        
        if self.direction == right:
            new_head = (head_x + cell_s, head_y)
        elif self.direction == up:
            new_head = (head_x, head_y - cell_s)
        elif self.direction == down:
            new_head = (head_x, head_y + cell_s)
        elif self.direction == left:        
            new_head = (head_x - cell_s, head_y)
            
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
        self.image = pygame.Surface((cell_s, cell_s))
        self.image.fill((255, 0, 0))
        self.pos = (0, 0)
        self.random_pos(width)
    
    def random_pos(self, screen_size):
        x = random.randrange(0, screen_size, cell_s)
        y = random.randrange(0, screen_size, cell_s)
        self.pos = (x, y)

class Banana():
    def __init__(self):
        self.image = pygame.Surface((cell_s, cell_s))
        self.image.fill((249, 252, 41))
        self.pos = (0, 0)
        self.random_pos(width)
    
    def random_pos(self, screen_size):
        x = random.randrange(0, screen_size, cell_s)
        y = random.randrange(0, screen_size, cell_s)
        self.pos = (x, y)

class Orange():
    def __init__(self):
        self.image = pygame.Surface((cell_s, cell_s))
        self.image.fill((255, 133, 1))
        self.pos = (0, 0)
        self.random_pos(width)
    
    def random_pos(self, screen_size):
        x = random.randrange(0, screen_size, cell_s)
        y = random.randrange(0, screen_size, cell_s)
        self.pos = (x, y)


screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
snake = Snake()
apple = Apple()
banana = Banana()
orange = Orange()
pygame.display.set_caption("Oblomov's snake game")

while running:
    clock.tick(speed)
    if not game_over:
        snake.move()
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

                elif event.key == K_p:
                    pause_game()


            if event.type == the_dissapearing:
                apple.random_pos(width)
                orange.random_pos(width)
                banana.random_pos(width)

        if snake.hit_wall(width) or snake.hit_self():
            game_over = True

        if snake.eat_apple(apple.pos):
            apple.random_pos(width)
            score += 1
            score_cnt += 1
            snake.grow()
            if score >= 3:
                speed += 0.9
                level += 1
                score = 0

        if snake.eat_apple(banana.pos):
            banana.random_pos(width)
            score += 2
            score_cnt += 2
            snake.grow()
            if score >= 3:
                speed += 0.9
                level += 1
                score = 0

        if snake.eat_apple(orange.pos):
            orange.random_pos(width)
            score += 3
            score_cnt += 3
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

        s1 = font.render(f"User: {username}", True, (255, 255, 255))
        s2 = font.render(f"Score: {score_cnt}", True, (255, 255, 255))
        s3 = font.render(f"Level: {level}", True, (255, 255, 255))
        
        screen.blit(s1, (10, 10))
        screen.blit(s2, (10, 40))
        screen.blit(s3, (10, 70))

        pygame.display.update()

    else:
        screen.fill(Black)
        go_text = font.render("Game Over! Press R to Restart", True, Yellow)
        sc_text = font.render(f"Final Score: {score_cnt}", True, White)
        screen.blit(go_text, (width//2 - go_text.get_width()//2, height//2 - 30))
        screen.blit(sc_text, (width//2 - sc_text.get_width()//2, height//2 + 10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(user_id, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    snake = Snake()
                    snake.direction = down
                    score, level = 0, 0
                    speed = get_speed(level)
                    game_over = False
                elif event.key == pygame.K_q:
                    save_progress(user_id, score, level)
                    pygame.quit()
                    sys.exit()