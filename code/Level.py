import pygame

from code.Const import (WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_BLACK,
                        TIMEOUT_LEVEL, TIMEOUT_STEP, SPAWN_TIME)
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.entity_list = []
        self.entity_list.append(EntityFactory.get_entity('IceFloor'))
        self.entity_list.append(EntityFactory.get_entity('Player'))

    def run(self) -> bool:
        clock = pygame.time.Clock()

        SPAWN_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(SPAWN_EVENT, SPAWN_TIME)
        TIMER_EVENT = pygame.USEREVENT + 2
        pygame.time.set_timer(TIMER_EVENT, TIMEOUT_STEP)

        time_left = TIMEOUT_LEVEL
        font = pygame.font.SysFont('Arial', 24, bold=True)
        font_info = pygame.font.SysFont('Arial', 18)

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.time.set_timer(SPAWN_EVENT, 0)
                    pygame.time.set_timer(TIMER_EVENT, 0)
                    pygame.quit()
                    quit()
                if event.type == SPAWN_EVENT:
                    self.entity_list.append(EntityFactory.get_entity('Penguin'))
                if event.type == TIMER_EVENT:
                    time_left -= TIMEOUT_STEP
                    if time_left <= 0:
                        pygame.time.set_timer(SPAWN_EVENT, 0)
                        pygame.time.set_timer(TIMER_EVENT, 0)
                        return True

            self.entity_list[0].draw(self.window)

            for entity in self.entity_list:
                entity.move()
                if entity.get_name() != 'IceFloor':
                    self.window.blit(entity.get_surf(), entity.get_rect())

            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_out_of_screen(self.entity_list)
            if EntityMediator.verify_water(self.entity_list):
                pygame.time.set_timer(SPAWN_EVENT, 0)
                pygame.time.set_timer(TIMER_EVENT, 0)
                return False

            seconds = max(0, time_left) / 1000
            hud = font.render(f'Tempo: {seconds:.1f}s', True, COLOR_WHITE)
            self.window.blit(hud, (10, 10))

            objetivo = font_info.render('Objetivo: sobreviva 10s sem cair na agua',
                                        True, COLOR_WHITE)
            self.window.blit(objetivo, (WIN_WIDTH - objetivo.get_width() - 10, 10))
            comandos = font_info.render('Comandos: setas para mover  |  ESC para sair',
                                        True, COLOR_WHITE)
            self.window.blit(comandos, (WIN_WIDTH - comandos.get_width() - 10, 32))

            pygame.display.flip()
