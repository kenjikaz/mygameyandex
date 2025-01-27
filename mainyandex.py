import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PokeWars")
bullet_state = ""

# тут будут всяческие переменные и константы по типу координат игрока и врагов и тп.

def show_score():


def game_over_text():


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
