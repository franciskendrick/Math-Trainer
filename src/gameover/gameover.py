from utils import BaseMain
from .title import Title
from .statistics import Statistics
from .buttons import Buttons
import pygame

pygame.init()


class Gameover(BaseMain):
    display_size_divider = 2.5

    def __init__(self):
        super().__init__()

        self.title = Title()
        self.statistics = Statistics()
        self.buttons = Buttons(self.display_size_divider)

    def draw(self, display):
        # Fill background
        self.draw_background()

        # Draw elements
        self.title.draw(self.display)
        self.statistics.draw(self.display)
        self.buttons.draw(self.display)

        # Blit display to original display
        self.blit_to_display(display)
