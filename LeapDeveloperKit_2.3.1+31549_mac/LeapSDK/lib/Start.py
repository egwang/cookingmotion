import pygame
from GameObject import GameObject


class Start(GameObject):
    @staticmethod
    def init():
        Start.startImage = pygame.image.load('images/start.png').convert_alpha()
    
    def __init__(self, x, y):
        super(Start, self).__init__(x, y, Start.startImage, 30)