from utils import BaseButtons, BaseButton
from utils import clip_set_to_list_on_yaxis, separate_sets_from_yaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "difficulty"
        )
    )

spritesets = separate_sets_from_yaxis(
    pygame.image.load(f"{resources_path}/buttons.png"))


class LevelButtons(BaseButtons):
    def __init__(self, enlarge):
        super().__init__()

        # Images
        order = ["1", "2", "3"]
        images = clip_set_to_list_on_yaxis(spritesets[0])

        # Positions
        positions = {
            "1": (43, 53),
            "2": (43, 65),
            "3": (43, 77)
        }

        # Buttons
        self.init_buttons(enlarge, order, images, positions)


class BackButton(BaseButton):
    def __init__(self, enlarge):
        super().__init__()

        # Image
        image = clip_set_to_list_on_yaxis(spritesets[1])
        position = (51, 108)

        # Button
        self.init_button(enlarge, image, position)

    def draw(self, display):
        is_hovered, orig_img, hover_img, rect, _ = self.button
        img = hover_img if is_hovered else orig_img

        display.blit(img, rect)
