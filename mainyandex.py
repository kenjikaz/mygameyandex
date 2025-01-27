import pygame
from pygame import mixer
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PokeWars")

menu = pygame.mixer.Sound("menu.wav")
mixer.music.load("background.wav")
mixer.music.play(-1)
mixer.music.set_volume(5)

pygame.display.set_caption("PokeWars")
icon = pygame.image.load('pokeball.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('abrakadabra.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

pokeballImg = pygame.image.load('pokeball.png')
pokeballX = 0
pokeballY = 480
pokeballX_change = 0
pokeballY_change = 2
pokeball_state = "ready"


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
gameover_font = pygame.font.Font('freesansbold.ttf', 64)

textX = 10
testY = 10



def show_score(x , y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def pause_menu():
    paused = True
    mixer.music.stop()
    menu.play(-1)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    mixer.music.play(-1)

        text = font.render("Пауза", True, "white")
        screen.blit(text, (800 // 2 - text.get_width() // 2, 600 // 2 - text.get_height() // 2))
        pygame.display.flip()



def game_over_text():
    gameover_text = gameover_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(gameover_text, (200, 250))
    mixer.music.stop()
    menu.play(0)


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global pokeball_state
    pokeball_state = "fire"
    screen.blit(pokeballImg, (x + 16, y + 10))


def is_collision():
    pass


running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerX_change = 1
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_a or event.key == pygame.K_LEFT) or (event.key == pygame.K_d
                                                                           or event.key == pygame.K_RIGHT):
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += 0.5 * enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        if pokeballY <= 0:
            pokeballY = 480
            pokeball_state = "ready"

        if pokeball_state == "fire":
            fire_bullet(pokeballX, pokeballY)
            pokeballY -= pokeballY_change
    pygame.display.update()

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
