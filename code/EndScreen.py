import pygame

from code.Const import (WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE,
                        COLOR_GREEN, COLOR_RED)


class EndScreen:
    def __init__(self, window: pygame.Surface, won: bool):
        self.window = window
        self.won = won
        self.bg = pygame.image.load('./asset/Water.png').convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (WIN_WIDTH, WIN_HEIGHT))

    def run(self) -> str:
        clock = pygame.time.Clock()
        font_big = pygame.font.SysFont('Arial', 72, bold=True)
        font_hint = pygame.font.SysFont('Arial', 24)

        message = 'GANHOU!' if self.won else 'PERDEU!'
        color = COLOR_GREEN if self.won else COLOR_RED

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 'MENU'
                    if event.key == pygame.K_ESCAPE:
                        return 'QUIT'

            self.window.blit(self.bg, (0, 0))

            surf = font_big.render(message, True, color)
            self.window.blit(surf, (WIN_WIDTH // 2 - surf.get_width() // 2,
                                    WIN_HEIGHT // 2 - 80))

            hint = font_hint.render('Enter: voltar ao menu   |   ESC: sair',
                                    True, COLOR_WHITE)
            self.window.blit(hint, (WIN_WIDTH // 2 - hint.get_width() // 2,
                                    WIN_HEIGHT // 2 + 40))

            pygame.display.flip()
