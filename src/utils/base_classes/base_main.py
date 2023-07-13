from window import window
import pygame

pygame.init()


class BaseMain:
    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)

    def draw_background(self, bgcolor=(235, 237, 233)):
        self.display.fill(bgcolor)

    def blit_to_display(self, display):
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))
