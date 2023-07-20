from utils import BaseButtons, clip_set_to_list_on_xaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "gameover"
        )
    )


class Buttons(BaseButtons):
    def __init__(self, enlarge):
        super().__init__()

        # Images
        order = ["restart", "menu"]
        images_ = clip_set_to_list_on_xaxis(
            pygame.image.load(f"{resources_path}/buttons.png"))
        
        images = []
        for img in images_:
            wd, ht = img.get_size()
            size = (wd * 2, ht * 2)
            images.append(pygame.transform.scale(img, size))
        
        # Positions
        positions = {
            "restart": (92, 208),
            "menu": (132, 208)
        }

        # Buttons
        self.init_buttons(enlarge, order, images, positions)
