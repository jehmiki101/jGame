import pygame

from code.Const import (PLAYER_SIZE, PLAYER_SPEED,
                        PLAYER_KEY_UP, PLAYER_KEY_DOWN,
                        PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT)
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (PLAYER_SIZE, PLAYER_SIZE))
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = PLAYER_SPEED

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_KEY_UP]:
            self.rect.y -= self.speed
        if pressed_keys[PLAYER_KEY_DOWN]:
            self.rect.y += self.speed
        if pressed_keys[PLAYER_KEY_LEFT]:
            self.rect.x -= self.speed
        if pressed_keys[PLAYER_KEY_RIGHT]:
            self.rect.x += self.speed