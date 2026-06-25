import pygame

from code.Const import PENGUIN_SIZE, PENGUIN_SPEED
from code.Entity import Entity


class Penguin(Entity):
    def __init__(self, name: str, position: tuple, velocity: tuple):
        super().__init__(name, position)
        self.dx, self.dy = velocity
        base = pygame.transform.scale(self.surf, (PENGUIN_SIZE, PENGUIN_SIZE))
        if self.dx < 0:
            base = pygame.transform.flip(base, True, False)
        elif self.dy > 0:
            base = pygame.transform.rotate(base, -90)
        elif self.dy < 0:
            base = pygame.transform.rotate(base, 90)
        self.surf = base
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = PENGUIN_SPEED

    def move(self):
        self.rect.x += self.speed * self.dx
        self.rect.y += self.speed * self.dy
