import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Загрузка изображения корабля и получение прямоугольник.
        self.image = pygame.image.load('images/ship.png')
        self.image.set_colorkey((240, 240, 240))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        #Флаги перемещения
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Обновляет позицию коробля с учетом флага."""
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factory
        if self.moving_left == True and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factory
        self.rect.centerx = self.center


    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.center = self.screen_rect.centerx
