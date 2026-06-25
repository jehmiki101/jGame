import random

from code.Const import (WIN_WIDTH, WIN_HEIGHT, ICE_X, ICE_Y, ICE_WIDTH, ICE_HEIGHT,
                        PLAYER_SIZE, PENGUIN_SIZE)
from code.IceFloor import IceFloor
from code.Penguin import Penguin
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(name: str):
        if name == 'IceFloor':
            return IceFloor(name, (0, 0))

        if name == 'Player':
            # Posição inicial do player
            center_x = ICE_X + ICE_WIDTH // 2 - PLAYER_SIZE // 2
            center_y = ICE_Y + ICE_HEIGHT // 2 - PLAYER_SIZE // 2
            return Player(name, (center_x, center_y))

        if name == 'Penguin':
            # Direção dos pinguins
            pos_y = random.randint(ICE_Y, ICE_Y + ICE_HEIGHT - PENGUIN_SIZE)
            if random.choice([True, False]):
                return Penguin(name, (-PENGUIN_SIZE, pos_y), (1, 0))
            return Penguin(name, (WIN_WIDTH, pos_y), (-1, 0))

        return None
