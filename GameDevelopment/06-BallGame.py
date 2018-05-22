import pygame
import random

# Initialize pygame
pygame.init()

red = 255,180,0
green = 0,255,0
blue = 0,0,255
white = 255,255,255
black = 0,0,0

width = 1000
height = 600

color_list = [green,black,white,blue]
color = random.choice(color_list)

screen = pygame.display.set_mode((width, height))
x = 50
y = 50
move_x = 2
move_y = 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()          # quit python

    screen.fill(red)
    pygame.draw.circle(screen,color,[x,y],50)

    x += move_x
    y += move_y

    if x > width - 50 or x < 50:
        move_x = -move_x
        color = random.choice(color_list)
    elif y > height - 50 or y < 50:
        move_y = -move_y
        color = random.choice(color_list)

    pygame.display.update()