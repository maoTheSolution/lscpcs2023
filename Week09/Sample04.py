import pygame

# variables
win_width = 1024
win_height = 512
bg_xPos = 0
bg_yPos = 0
pygame.init()
gamepad = pygame.display.set_mode((win_width, win_height))
background01 = pygame.image.load('./img01.jpg')
con = False
force = 0
while(not con):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            con = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            force = -5
        elif keys[pygame.K_DOWN]:
            force = 5
        if event.type == pygame.KEYUP:
            force = 0


    bg_yPos = bg_yPos + force
    gamepad.blit(background01, (bg_xPos,bg_yPos))



    pygame.display.update()

