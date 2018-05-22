import pygame

# Initialize pygame
pygame.init()

white = 255,255,255

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball_2.png")
game_bg = pygame.image.load("game_bg.jpg")

x = 50
y = 50
move_x = 8
move_y = 8
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()          # quit python

    # screen.fill(white)
    screen.blit(game_bg, (0,0))

    screen.blit(ball,(x,y))

    x += move_x
    y += move_y

    if x > width - 150 or x < 0:
        move_x = -move_x
    elif y > height - 155 or y < 0:
        move_y = -move_y

    pygame.display.update()