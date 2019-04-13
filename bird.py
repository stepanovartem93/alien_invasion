import pygame

class Bird():
    def __init__(self, screen):
        """Инициализирует птичку и задаёт его начальную позицию"""
        self.screen = screen

        """Загрузка изображения птички и получение прямоугольника"""
        self.image = pygame.image.load('images/bird_2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """Каждая новая птичка появляется в центре экрана."""
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Рисует птичку в текущей позиции"""
        self.screen.blit(self.image, self.rect)