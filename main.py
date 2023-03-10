import pygame
from SnL.constants import WIDTH, HEIGHT

FPS = 30

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("🐍 Snakes and Ladders 🧭")

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    
    pygame.quit()

main()