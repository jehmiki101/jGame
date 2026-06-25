from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(f'./asset/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = 0

    def get_name(self) -> str:
        return self.name

    def get_surf(self) -> pygame.Surface:
        return self.surf

    def get_rect(self) -> pygame.Rect:
        return self.rect

    def get_hitbox(self) -> pygame.Rect:
        content = self.surf.get_bounding_rect()
        return content.move(self.rect.x, self.rect.y)

    def set_surf(self, surf: pygame.Surface):
        self.surf = surf
        self.rect = self.surf.get_rect(topleft=(self.rect.x, self.rect.y))

    @abstractmethod
    def move(self):
        pass
