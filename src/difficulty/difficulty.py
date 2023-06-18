from window import window
from .title import Title
from .buttons import LevelButtons, BackButton
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "menu"
        )
    )


class Difficulty:
    display_size_divider = 5
    
    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)
        
        self.title = Title()
        self.lvl_buttons = LevelButtons(self.display_size_divider)
        self.back_button = BackButton(self.display_size_divider)
        
    def draw(self, display):
        # Fill background
        self.display.fill((235, 237, 233))

        # Draw elements
        self.title.draw(self.display)
        self.lvl_buttons.draw(self.display)
        self.back_button.draw(self.display)

        # Blit menu's display to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))
 