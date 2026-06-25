import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, WIN_TITLE
from code.EndScreen import EndScreen
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption(WIN_TITLE)
        # Música de fundo geral: toca em loop por todas as telas.
        pygame.mixer.music.load('./asset/musicaFundo.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def run(self):
        while True:
            menu = Menu(self.window)
            option = menu.run()

            if option == 'SAIR':
                pygame.quit()
                quit()

            if option == 'JOGAR':
                level = Level(self.window)
                won = level.run()

                end = EndScreen(self.window, won)
                result = end.run()

                if result == 'QUIT':
                    pygame.quit()
                    quit()
