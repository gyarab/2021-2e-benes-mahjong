import pygame
import random
from pygame.version import PygameVersion
pygame.init()

PADDLE_HEIGHT = 150
PADDLE_SPEED = 3
BALL_SPEED = 1
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

scr = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
playery = 0
circle_x = 400
circle_y = 250
ball_vertical_speed = random.randint(0, 10) / 10
is_started = False
direction = -1
vertical_direction = random.choice([-1, 1])
score = 100
while running:
    scr.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            is_started = True
        if event.type == pygame.QUIT:
            running = False

    ball = pygame.draw.circle(scr, (255, 255, 255), (circle_x, circle_y), 15)
    paddle = pygame.draw.rect(scr, (255, 255, 255), pygame.Rect(30, playery, 30, PADDLE_HEIGHT-score))

    if not is_started:
        pygame.display.flip()
        continue

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        playery -= PADDLE_SPEED
    elif keys[pygame.K_s]:
        playery += PADDLE_SPEED
    if playery < 0:
        playery = 0
    elif playery > SCREEN_HEIGHT - PADDLE_HEIGHT + score:
        playery = SCREEN_HEIGHT - PADDLE_HEIGHT + score

    if (x:= paddle.colliderect(ball)) or circle_x + 15 > SCREEN_WIDTH:
        direction = -direction
        if x:
            circle_x = 60 + 15
            score += 1
        ball_vertical_speed = random.randint(0, 10) / 10
    if circle_x + 15 < 0:
        print("GAME OVER BOI")
        print("score: " + str(score))
        break
    if circle_y -15 < 0 or circle_y + 15 > SCREEN_HEIGHT:
        vertical_direction = -vertical_direction
    
    circle_x += direction * BALL_SPEED
    circle_y += vertical_direction * ball_vertical_speed

    pygame.display.flip()


pygame.quit()

