import pygame
pygame.init()
gamepad = pygame.display.set_mode((1024,512))
bg = pygame.image.load('./img01.jpg')
clock = pygame.time.Clock()
con = False
while(not con):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            con = True

    gamepad.blit(bg,(0,0))
    pygame.display.update()
    clock.tick(60)

