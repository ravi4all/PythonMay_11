import pygame
import random

# Initialize pygame
pygame.init()

red = 255,180,0
black = 0,0,0

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))

frog = pygame.image.load("frog.png")

frog_x = random.randint(0,width - frog.get_width())
frog_y = random.randint(0,height - frog.get_height())
# print(frog_x, frog_y)

x = 0
y = 0
snake_length = 50
move_x = 0
move_y = 0

snake_head = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()          # quit python
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 1
                move_y = 0
            if event.key == pygame.K_LEFT:
                move_x = -1
                move_y = 0
            if event.key == pygame.K_DOWN:
                move_y = 1
                move_x = 0
            if event.key == pygame.K_UP:
                move_y = -1
                move_x = 0

    screen.fill(red)
    snake_rect = pygame.draw.rect(screen,black,[x,y,snake_length,50])
    screen.blit(frog,(frog_x, frog_y))

    x += move_x
    y += move_y

    frog_rect = pygame.Rect(frog_x, frog_y, frog.get_width(), frog.get_height())

    snakelist = []
    snake_head.append(x)
    snake_head.append(y)
    snakelist.append(snake_head)
    print(snakelist)

    if snake_rect.colliderect(frog_rect):
        # print("Collision")
        frog_x = random.randint(0, width - frog.get_width())
        frog_y = random.randint(0, height - frog.get_height())
        snake_length += 25


    pygame.display.update()