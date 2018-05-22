import pygame

# Initialize pygame
pygame.init()

red = 255,180,0
black = 0,0,0

screen = pygame.display.set_mode((1000,600))

x = 0
y = 0

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()          # quit python

    screen.fill(red)

    pygame.draw.rect(screen,black,[x,y,50,50])
    x = x + 10
    # y = y + 1
    pygame.display.update()