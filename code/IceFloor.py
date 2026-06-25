import pygame

from code.Const import (ICE_X, ICE_Y, ICE_WIDTH, ICE_HEIGHT,
                        WIN_WIDTH, WIN_HEIGHT)
from code.Entity import Entity


class IceFloor(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.water_surf = pygame.image.load('./asset/Water.png').convert_alpha()
        self.water_surf = pygame.transform.scale(self.water_surf, (WIN_WIDTH, WIN_HEIGHT))
        self.ice_surf = pygame.transform.scale(self.surf, (ICE_WIDTH, ICE_HEIGHT))
        self.rect = pygame.Rect(ICE_X, ICE_Y, ICE_WIDTH, ICE_HEIGHT)

    def draw(self, window: pygame.Surface):
        window.blit(self.water_surf, (0, 0))
        window.blit(self.ice_surf, (ICE_X, ICE_Y))

    def move(self):
        pass
