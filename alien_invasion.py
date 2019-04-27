import pygame
from settings import Settings
from ship import Ship
from bird import Bird
import game_functions as gf

def run_game():

    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Создание корабля.
    ship = Ship(ai_settings, screen)
    bird = Bird(screen)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, bird)

run_game()
