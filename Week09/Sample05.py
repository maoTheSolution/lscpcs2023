import pygame
import random

# variables
win_width = 1024
win_height = 512
bg_xPos = 0
bg_yPos = 0
bg2_xPos = win_width
ch_xPos = 0
ch_yPos = 0
con = False
force = 0
temp = 0

pygame.init()
gamepad = pygame.display.set_mode((win_width, win_height))
background01 = pygame.image.load('./img01.jpg')
background02 = background01.copy()
character = pygame.image.load('./boy.png')
character = pygame.transform.scale(character, (150, 100))
clock = pygame.time.Clock()
obs = pygame.image.load('./pumkin.png')
obs = pygame.transform.scale(obs, (100, 100))
obs_y = random.randint(0, 512)
obs_x = 1024

while(not con):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            con = True
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            force = -2
        elif keys[pygame.K_DOWN]:
            force = 2
        if event.type == pygame.KEYUP:
            force = 0

    bg_xPos = bg_xPos - 8
    bg2_xPos = bg2_xPos - 8

    if bg_xPos +  win_width == 0:
        bg_xPos = 0
        bg2_xPos = win_width

    ch_yPos = ch_yPos + force * clock.tick(60)

    obs_x = obs_x - 8
    if(obs_x < 0):
        obs_x = 1024
        obs_y = random.randint(0, 512)

    gamepad.blit(background01, (bg_xPos,bg_yPos))
    gamepad.blit(background02, (bg2_xPos, bg_yPos))
    gamepad.blit(character, (ch_xPos, ch_yPos))
    gamepad.blit(obs, (obs_x, obs_y))

    pygame.display.update()
    clock.tick(60)

