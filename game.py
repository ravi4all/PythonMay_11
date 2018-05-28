import pygame
import random
import time

# Initialize pygame
pygame.init()

red = 255,180,0
black = 0,0,0

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))

game_bg = pygame.image.load("images/background.png")
# game_left_bg = pygame.image.load("images/background.png")
# game_right_bg = pygame.image.load("images/background.png")

background_x = -game_bg.get_width()/2

zombie_1 = pygame.image.load("images/zombie_1.gif")
zombie_2 = pygame.image.load("images/zombie_2.png")
zombie_3 = pygame.image.load("images/zombie_3.png")
zombie_4 = pygame.image.load("images/zombie_4.png")

blood_patch = pygame.image.load("images/zombie_blood.png")

zombie_list = [zombie_1, zombie_2, zombie_3, zombie_4]

zombie_image = random.choice(zombie_list)

zombie_width = zombie_image.get_width()
zombie_height = zombie_image.get_height()

zombie_x = random.randint(0, width - zombie_width)
zombie_y = random.randint(0, height - zombie_height)

zombie_scale_x = 0
zombie_scale_y = 0

gun_pointer = pygame.image.load('images/aim_pointer.png')

gun_image = pygame.image.load("images/gun_1.png")

shot_sound = pygame.mixer.Sound("sounds/shot_sound.wav")
zombie_sound = pygame.mixer.Sound("sounds/zombie_shot.wav")

background_music = pygame.mixer.Sound("sounds/background.wav")
background_music.play(-1)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()   # quit pygame
            quit()          # quit python

        if event.type == pygame.MOUSEBUTTONDOWN:
            shot_sound.play()
            if zombie_rect.colliderect(pointer_rect):
                zombie_sound.play()
                # screen.blit(blood_patch, (zombie_x, zombie_y))
                time.sleep(0.8)
                zombie_scale_x = 10
                zombie_scale_y = 10
                # zombie_image = random.choice(zombie_list)
                # zombie_x = random.randint(0, width - zombie_width)
                # zombie_y = random.randint(0, height - zombie_height)

    pos_x, pos_y = pygame.mouse.get_pos()

    zombie_rect = pygame.Rect(zombie_x, zombie_y, zombie_width, zombie_height)
    pointer_rect = pygame.Rect(pos_x, pos_y, gun_pointer.get_width(), gun_pointer.get_height())

    screen.blit(game_bg, (0,0))

    zombie_image = pygame.transform.scale(zombie_image,
                                          (zombie_width, zombie_height))

    zombie_width -= zombie_scale_x
    zombie_height -= zombie_scale_y

    if zombie_width <= 10 or zombie_height <= 10:
        zombie_image = random.choice(zombie_list)
        zombie_x = random.randint(0, width - zombie_width)
        zombie_y = random.randint(0, height - zombie_height)
        zombie_width = zombie_image.get_width()
        zombie_height = zombie_image.get_height()
        zombie_scale_x = 0
        zombie_scale_y = 0

    screen.blit(zombie_image, (zombie_x, zombie_y))

    screen.blit(gun_pointer,
                (pos_x - gun_pointer.get_width()/2,
                 pos_y - gun_pointer.get_height()/2))

    screen.blit(gun_image,
                (pos_x,
                 height - 300))

    pygame.display.update()