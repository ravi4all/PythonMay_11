import pygame

# Initialize pygame
pygame.init()

red = 255,180,0
black = 0,0,0

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))
x = 0
y = 0
move_x = 0
move_y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()          # quit python
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 2
                # move_y = 0
            if event.key == pygame.K_LEFT:
                move_x = -2
                # move_y = 0
            if event.key == pygame.K_DOWN:
                move_y = 2
                # move_x = 0
            if event.key == pygame.K_UP:
                move_y = -2
                # move_x = 0



    screen.fill(red)
    pygame.draw.rect(screen,black,[x,y,50,50])
    # x = x + 10
    # y = y + 1

    x += move_x
    y += move_y

    if x > width - 50 or x < 0:
        move_x = -move_x
    elif y > height - 50 or y < 0:
        move_y = -move_y

    pygame.display.update()