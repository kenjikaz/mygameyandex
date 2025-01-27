import pygame
from pygame import mixer

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

pokeballImg = pygame.image.load('pokeball.png')
pokeballX = 0
pokeballY = 480
pokeballX_change = 0
pokeballY_change = 2
pokeball_state = "ready"


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

gameover_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score():


def pause_menu():
    paused = True
    mixer.music.stop()
    menu.play(-1)
    while paused:
        pass



def game_over_text():
    gameover_text = gameover_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(gameover_text, (200, 250))
    mixer.music.stop()
    menu.play(0)


def player():


def enemy():


def fire_bullet():
    global bullet_state


def is_collision():
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    # изменение координаты Х игрока = -1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    # изменение координаты Х игрока = 1
        # тут будет изменение движения врагов
        # тут будет изменение движение снаряда
        # тут будет проверка коллизий
        # тут будет обновления счета игрока

        pygame.display.update()
