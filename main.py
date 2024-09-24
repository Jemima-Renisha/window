import pygame
pygame.init()
screeen = pygame.display.set_mode((500,500))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screeen.fill("pink")
    pygame.display.flip()