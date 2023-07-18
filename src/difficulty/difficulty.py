from utils import BaseMain
from .title import Title
from .buttons import LevelButtons, BackButton
import pygame

pygame.init()


class Difficulty(BaseMain):
    display_size_divider = 5

    def __init__(self):
        super().__init__()

        self.title = Title()
        self.lvl_buttons = LevelButtons(self.display_size_divider)
        self.back_button = BackButton(self.display_size_divider)
        
    def draw(self, display):
        # Fill background
        self.draw_background()

        # Draw elements
        self.title.draw(self.display)
        self.lvl_buttons.draw(self.display)
        self.back_button.draw(self.display)

        # Blit display to original display
        self.blit_to_display(display)
