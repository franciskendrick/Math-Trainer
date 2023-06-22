from utils import BaseMain
from .title import Title
from .buttons import Buttons
import pygame

pygame.init()


class Menu(BaseMain):
    def __init__(self):
        super().__init__()
    
        self.title = Title()
        self.buttons = Buttons(self.display_size_divider)

    def draw(self, display):
        # Fill background
        self.draw_background()

        # Draw elements
        self.title.draw(self.display)
        self.buttons.draw(self.display)

        # Blit menu's display to original display
        self.blit_to_display(display)
