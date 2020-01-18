import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf

def run_game():
    #Инциализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    #Создание корабля.
    ship = Ship(ai_settings, screen)
    #Создание группы для хранения пуль и группы пришельцев.
    bullets = Group()
    aliens = Group()
    #Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #Создание кнопки Play.
    play_button = Button(ai_settings, screen, 'Play')

    #Запуск основного цикла.
    while True:
        #Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb,
                         ship, aliens, bullets, play_button)
        
run_game()
