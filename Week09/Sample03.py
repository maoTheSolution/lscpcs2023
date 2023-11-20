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
y_change = 200

con = False
while(not con):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            con = True


    bg_x = bg_x - 2
    bg2_x = bg2_x - 2

    # 배경을 이동하는 코드
    if bg_x == -1024:
        bg_x == 0
    if bg2_x == 0:
        bg2_x == 1024

    # 캐릭터가 이동하는 코드 
    if event.type == pygame.KEYDOWN:
        if event.type == pygame.K_UP:
            y_change = -5
        elif event.type == pygame.K_DOWN:
            y_change = 5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            y_change = 0

    # 이미지를 표현하는 코드
    gamepad.blit(bg, (bg_x, 0))
    gamepad.blit(bg2, (bg2_x, 0))
    gamepad.blit(character, (0, y_change))


    pygame.display.update()
    clock.tick(60)

