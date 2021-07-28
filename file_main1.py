import pygame
import random
import math

from pygame import mixer
pygame.init()
# create a new screen
screen = pygame.display.set_mode((800, 500))

# background
background = pygame.image.load('background.png')
mixer.music.load('background.wav')
mixer.music.play(-1)

# title and logo
pygame.display.set_caption("ban sung")
icon = pygame.image.load('spaceship.png')  # dòng này để load ảnh? cái icon gị là biến à?
pygame.display.set_icon(icon)  # dòng này để set icon và display?

# player
playerImg = pygame.image.load("viet3.png")
playerX = 400
playerY = 400
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6
for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("guitar.png"))
    enemyX.append(random.randint(0, 750))
    enemyY.append(random.randint(23, 130))
    enemyX_change.append(0.1 * 20)
    enemyY_change.append(0.005 * 20)

# bullet
bulletImg = pygame.image.load("fitness-ball.png")
bulletX = 0
bulletY = 400
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# game over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 25, y + 25))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance <= 40:
        return True
    else:
        return False


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 0, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("game over", True, (255, 255, 255))
    screen.blit(over_text, (300, 300))


# game loop
running = True
while running:
    screen.fill((0, 0, 128))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed, check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2 * 20
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2 * 20
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2 * 20
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2 * 20
    # nếu để or ntn thì sẽ chạy về 1 hướng khi bỏ ra
    # nếu bằng 0 thì bỏ ra là đứng yên
    # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #    playerX_change = 0.1
    # nếu dùng ntn thì bỏ ra sẽ giữ nguyên hướng

    # cái playerX+ ở đây cũng được, dưới cũng được
    # adding boundary
    '''if playerX <= 0:
        playerX = 0
    elif playerX >= 750:
        playerX = 750'''
    # thử code xem có quay đầu không || quay ddaafu thaatj nay! success
    if playerX <= 0:
        playerX_change = 0.1 * 20
    elif playerX >= 800 - 50:
        playerX_change = -0.1 * 20

    # enemy movement
    for i in range(num_of_enemy):
        if enemyY[i] > 200:
            for j in range(num_of_enemy):
                enemyY[i] = 2000
            game_over_text()
            break

        if enemyX[i] <= 0:
            enemyX_change[i] = -enemyX_change[i]
        elif enemyX[i] >= 800 - 64:
            enemyX_change[i] = -enemyX_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            enemyX[i] = random.randint(0, 750)
            enemyY[i] = random.randint(23, 130)

        enemy(enemyX[i], enemyY[i], i)
        enemyX[i] += enemyX_change[i]
        enemyY[i] += enemyY_change[i]

    # bawsn nhieu vien
    if bulletY <= 0:
        bulletY = 400
        bullet_state = "ready"

    # ntn ban dk 1 vien
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    playerX += playerX_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
