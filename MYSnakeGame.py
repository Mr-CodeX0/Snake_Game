import pygame
import time
import random

pygame.init()


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

width, hight = 1080, 720
display = pygame.display.set_mode((width, hight))

clock = pygame.time.Clock()
#snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100 - 10, 50]]
#food
food = [random.randrange(0, width, 10), random.randrange(0, hight, 10)]

points = 0

game_over = False
direction = 'RIGHT'
new_direction = None
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                new_direction = 'UP'
            if event.key == pygame.K_s:
                new_direction = 'DOWN'
            if event.key == pygame.K_a:
                new_direction = 'LEFT'
            if event.key == pygame.K_d:
                new_direction = 'RIGHT'

    if new_direction == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if new_direction == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if new_direction == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if new_direction == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    if snake_pos[0] == width or snake_pos[0] == 0 or snake_pos[1] == hight or snake_pos[1] == 0:
        game_over = True
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food[0] and snake_pos[1] == food[1]:
        print('yummy')
        points += 1
        food = [random.randrange(0, width, 10), random.randrange(0, hight, 10)]
    else:
        snake_body.pop()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    display.fill(blue)
    pygame.draw.rect(display, black, (food[0], food[1], 10, 10))
    for pos in snake_body:
        pygame.draw.rect(display, green, (pos[0], pos[1], 10, 10))

    pygame.display.update()
    clock.tick(20)
pygame.quit()
time.sleep(2)
print('points : ' + str(points))
quit()
