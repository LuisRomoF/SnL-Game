import pygame
from .constants import GREEN,ROWS, WHITE,SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.current_player = None

    def draw_squares(self,win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2,ROWS,2):
                pygame.draw.rect(win,GREEN,(row * SQUARE_SIZE, col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))