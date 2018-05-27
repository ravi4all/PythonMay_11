import pygame
import random

# Initialize pygame
pygame.init()

red = 255,180,0
black = 0,0,0

width = 900
height = 600

screen = pygame.display.set_mode((width, height))

frog = pygame.image.load("frog.png")

snake_bg = pygame.image.load("snakebg.jpg")

def home_screen():
    font = pygame.font.SysFont(None, 80)
    text = font.render("Press SPACE to start Game", True, black)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # quit pygame
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.blit(snake_bg, (0,0))
        screen.blit(text, (50, 100))

        pygame.display.update()

def gameOver():
    font = pygame.font.SysFont(None, 100)
    text = font.render("Game Over",True, black)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   # quit pygame
                quit()
        screen.blit(text, (200,100))

        pygame.display.update()

def snake(snakelist):
    for i in snakelist:
        pygame.draw.rect(screen, black, (i[0], i[1], 50, 50))

def game():
    frog_x = random.randint(0, width - frog.get_width())
    frog_y = random.randint(0, height - frog.get_height())
    # print(frog_x, frog_y)

    x = 0
    y = 0
    snake_length = 1
    move_x = 0
    move_y = 0

    snakelist = []

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
        snake_rect = pygame.Rect(x,y,50,50)
        screen.blit(frog,(frog_x, frog_y))

        x += move_x
        y += move_y

        frog_rect = pygame.Rect(frog_x, frog_y, frog.get_width(), frog.get_height())

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snakelist.append(snake_head)
        # print(snakelist)

        if len(snakelist) > snake_length:
            del snakelist[0]

        snake(snakelist)

        for each in snakelist[:-1]:
            if each == snakelist[-1]:
                # print("Game Over")
                gameOver()

        if snake_rect.colliderect(frog_rect):
            # print("Collision")
            frog_x = random.randint(0, width - frog.get_width())
            frog_y = random.randint(0, height - frog.get_height())
            snake_length += 25


        pygame.display.update()

# game()
home_screen()