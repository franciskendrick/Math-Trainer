from utils import BaseMain
from .title import Title
import pygame

pygame.init()


class Gameover(BaseMain):
    display_size_divider = 2.5

    def __init__(self):
        super().__init__()

        self.title = Title()

    def draw(self, display):
        # Fill background
        self.draw_background()

        # Draw elements
        self.title.draw(self.display)

        # Blit display to original display
        self.blit_to_display(display)
