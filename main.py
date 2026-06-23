import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode((1000, 600))
print('Setup Finish')

print('Loop Start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close window
            quit() #End pygame