from utils import BaseMain
import pygame

pygame.init()


class Menu(BaseMain):
    display_size_divider = 5

    def __init__(self):
        super().__init__()

    def draw(self, display):
        # Fill background
        self.draw_background()

        # Draw elements

        # Blit display to original display
        self.blit_to_display(display)
