from code.Const import WIN_WIDTH, WIN_HEIGHT, PENGUIN_SIZE
from code.IceFloor import IceFloor
from code.Penguin import Penguin
from code.Player import Player


class EntityMediator:
    @staticmethod
    def __get_player(entity_list: list):
        for entity in entity_list:
            if isinstance(entity, Player):
                return entity
        return None

    @staticmethod
    def __get_ice(entity_list: list):
        for entity in entity_list:
            if isinstance(entity, IceFloor):
                return entity
        return None

    @staticmethod
    def verify_collision(entity_list: list):
        player = EntityMediator.__get_player(entity_list)
        if player is None:
            return
        player_hb = player.get_hitbox()
        for entity in entity_list:
            if isinstance(entity, Penguin):
                penguin_hb = entity.get_hitbox()
                if player_hb.colliderect(penguin_hb):
                    overlap_left = penguin_hb.right - player_hb.left
                    overlap_right = player_hb.right - penguin_hb.left
                    overlap_top = penguin_hb.bottom - player_hb.top
                    overlap_bottom = player_hb.bottom - penguin_hb.top
                    minimum = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
                    if minimum == overlap_left:
                        player.rect.x += overlap_left
                    elif minimum == overlap_right:
                        player.rect.x -= overlap_right
                    elif minimum == overlap_top:
                        player.rect.y += overlap_top
                    else:
                        player.rect.y -= overlap_bottom
                    player_hb = player.get_hitbox()

    @staticmethod
    def verify_water(entity_list: list) -> bool:
        player = EntityMediator.__get_player(entity_list)
        ice = EntityMediator.__get_ice(entity_list)
        if player is None or ice is None:
            return False
        if not ice.rect.collidepoint(player.rect.center):
            return True
        return False

    @staticmethod
    def verify_out_of_screen(entity_list: list):
        for entity in entity_list[:]:
            if isinstance(entity, Penguin):
                if (entity.rect.x > WIN_WIDTH or entity.rect.right < 0 or
                        entity.rect.y > WIN_HEIGHT or entity.rect.bottom < 0):
                    entity_list.remove(entity)
