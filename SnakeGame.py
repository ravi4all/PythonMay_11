import pygame
import random

pygame.init()

width = 900
height = 600

white = 255,255,255
red = 255,0,0
blue = 0,0,255

screen = pygame.display.set_mode((width, height))

apple = pygame.image.load("apple.png")

clock = pygame.time.Clock()

snakeBg = pygame.image.load("snakebg.jpg")

point = pygame.mixer.Sound('point.wav')

# def homeScreen():
#     font = pygame.font.SysFont(None, 50)
#     welcometext = font.render("Welcome to Snake Game", True, white)
#     starttext = font.render("Press SPACE to Start Game", True, white)
#     while True:
#
#         for event in pygame.event.get():
#
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     game()
#
#         screen.blit(snakeBg, (0,0))
#         screen.blit(welcometext, (230,100))
#         screen.blit(starttext, (200, 200))
#         pygame.display.update()


def gameOver():
    font = pygame.font.SysFont(None, 70)
    text = font.render("Game Over", True, blue)
    screen.blit(text, (width/2 - 150, height/2 - 30))

def score(counter):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score :"+str(counter), True, blue)
    screen.blit(text, (10, 10))

def snake(snakeList):
    for i in snakeList:
        pygame.draw.rect(screen, red, [i[0], i[1], 50, 50])


def game():
    x = 0
    y = 0

    move_x = 0
    move_y = 0

    apple_x = random.randint(0, width - 54)
    apple_y = random.randint(0, height - 68)

    snakeList = []
    snakeLength = 1
    FPS = 90

    counter = 0

    main = True
    
    while main:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 5
                    move_y = 0
                elif event.key == pygame.K_LEFT:
                    move_x = -5
                    move_y = 0
                elif event.key == pygame.K_DOWN:
                    move_y = 5
                    move_x = 0
                elif event.key == pygame.K_UP:
                    move_y = -5
                    move_x = 0

        screen.fill(white)
        screen.blit(apple, (apple_x, apple_y))

        snake_rect = pygame.Rect(x,y,50,50)
        apple_rect = pygame.Rect(apple_x, apple_y, apple.get_width(), apple.get_height())

        x += move_x
        y += move_y

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)

        snakeList.append(snakeHead)
        #print(snakeList)
        #print(snakeHead)
        #print(snakeList)
        snake(snakeList)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        for each in snakeList[:-1]:
            if each == snakeList[-1]:
                print("Game Over")
                gameOver()
                main = False

        if snake_rect.colliderect(apple_rect):
            point.play()
            apple_x = random.randint(0, width - 54)
            apple_y = random.randint(0, height - 68)
            snakeLength += 5
            FPS += 1
            counter += 1

        score(counter)

        pygame.display.update()
        clock.tick(FPS)

game()
# homeScreen()
