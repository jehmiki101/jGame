import pygame

from code.Const import (WIN_WIDTH, WIN_HEIGHT, WIN_TITLE, MENU_OPTION,
                        COLOR_WHITE, COLOR_YELLOW, COLOR_WATER)


class Menu:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.bg = pygame.image.load('./asset/Water.png').convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (WIN_WIDTH, WIN_HEIGHT))

    def run(self) -> str:
        clock = pygame.time.Clock()
        selected = 0
        font_title = pygame.font.SysFont('Arial', 56, bold=True)
        font_opt = pygame.font.SysFont('Arial', 36, bold=True)
        font_hint = pygame.font.SysFont('Arial', 20)

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_DOWN):
                        selected = (selected + 1) % len(MENU_OPTION)
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[selected]

            self.window.blit(self.bg, (0, 0))

            title = font_title.render(WIN_TITLE, True, COLOR_WHITE)
            self.window.blit(title, (WIN_WIDTH // 2 - title.get_width() // 2, 120))

            for i, option in enumerate(MENU_OPTION):
                color = COLOR_YELLOW if i == selected else COLOR_WHITE
                prefix = '> ' if i == selected else '  '
                surf = font_opt.render(prefix + option, True, color)
                self.window.blit(surf, (WIN_WIDTH // 2 - surf.get_width() // 2, 300 + i * 60))

            hint = font_hint.render('Use as setas e Enter. Sobreviva 10s sem cair na agua!',
                                    True, COLOR_WHITE)
            self.window.blit(hint, (WIN_WIDTH // 2 - hint.get_width() // 2, WIN_HEIGHT - 60))

            pygame.display.flip()
