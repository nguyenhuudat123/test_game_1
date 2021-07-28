import pygame
pygame.init()
#create a new screen
screen = pygame.display.set_mode((800, 500))

#background
background = pygame.image.load('background.png')

#title and logo
pygame.display.set_caption("ban sung")
icon = pygame.image.load('spaceship.png')       #dòng này để load ảnh? cái icon gị là biến à?
pygame.display.set_icon(icon)                   #dòng này để set icon và display?

#player
playerImg = pygame.image.load("viet3.png")
playerX = 400
playerY = 400
playerX_change = 0.1 * 20

#enemy
enemyImg = pygame.image.load("guitar.png")
enemyX = 200
enemyY = 100
enemyX_change = 0.1 * 20
enemyY_change= 0    #test thooi, k roi dau

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))



#game loop
running = True
while running:
    screen.fill((0, 0, 128))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed, check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                playerX_change = -playerX_change
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                playerX_change = playerX_change

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                enemyX_change = -enemyX_change
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                enemyX_change = enemyX_change
    '''        if event.type == pygame.KEYUP:
           if event.key == pygame.K_e:
               playerX_change = -playerX_change'''

#đã xong chuyển động như trong game, dùng 1 phím để điều khiển.
#đơn giản là bó cái keyup đi là nó tự duy trì trạng thái chạy sau khi bấm phím
#nếu giữu cái keyup nó sẽ quay lại của quay lại, công cốc
    if playerX <= 0:
        playerX_change = 0.1 * 20
    elif playerX >= 800-50:
        playerX_change = -0.1 * 20

    if enemyX <= 0:
        enemyX_change = 0.1 * 20
    elif enemyX >= 800-64:
        enemyX_change = -0.1 * 20


    playerX += playerX_change
    enemyX += enemyX_change
    enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()