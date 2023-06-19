from utils import BaseButtons, clip_set_to_list_on_yaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "menu"
        )
    )


class Buttons(BaseButtons):
    def __init__(self, enlarge):
        super().__init__()

        # Images
        order = ["addition", "subtraction", "multiplication", "division", "exponentiation", "square_root"]
        images = clip_set_to_list_on_yaxis(
            pygame.image.load(f"{resources_path}/buttons.png"))

        # Positions
        positions = {
            "addition": (41, 46),
            "subtraction": (31, 58),
            "multiplication": (23, 70),
            "division": (41, 82),
            "exponentiation": (23, 94),
            "square_root": (31, 106)
        }

        # Buttons
        self.init_buttons(enlarge, order, images, positions)
