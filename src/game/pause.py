from utils import BaseButton, palette_swap
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "game"
        )
    )


class Pause(BaseButton):
    def __init__(self, enlarge):
        super().__init__()

        # Image
        image = pygame.image.load(f"{resources_path}/buttons.png")
        wd, ht = image.get_size()
        size = (wd * 2, ht * 2)
        image = pygame.transform.scale(image, size)
        
        position = (4, 4)

        # Button
        self.init_button(enlarge, image, position)
