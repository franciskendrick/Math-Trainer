from utils import BaseMain
import pygame

pygame.init()


class Game(BaseMain):
    def __init__(self):
        super().__init__()
        
    def draw(self, display):
        # Fill background
        self.draw_background()

        # Draw elements

        # Blit menu's display to original display
        self.blit_to_display(display)
