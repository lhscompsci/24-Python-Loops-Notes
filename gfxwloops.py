import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
screen.fill((255,255,255))
img = pygame.image.load("dude.gif")

screen.blit(img,(x,y))

# Updates the display
pygame.display.update()

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            pygame.quit();
            sys.exit();
