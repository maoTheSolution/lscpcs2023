import pygame
pygame.init()
gamepad = pygame.display.set_mode((1024,512))

bg = pygame.image.load('./img01.jpg')
bg2= bg.copy()
clock = pygame.time.Clock()
character = pygame.image.load('./boy.png')
character = pygame.transform.scale(character, (150, 100))
bg_x = 0
bg2_x = 1024

con = False
while(not con):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            con = True

    bg_x = bg_x - 2
    bg2_x = bg2_x - 2

    if bg_x == -1024:
        bg_x == 0
    if bg2_x == 0:
        bg2_x == 1024

    gamepad.blit(bg, (bg_x, 0))
    gamepad.blit(bg2, (bg2_x, 0))
    gamepad.blit(character, (0, 200))


    pygame.display.update()
    clock.tick(60)

