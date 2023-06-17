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
    pygame.image.load(f"{resources_path}/title.png"))


class Title:
    def __init__(self):
        self.init_title()

    def init_title(self):
        img = clip_set_to_list_on_yaxis(spritesets[0])
        wd, ht = img.get_size()
        size = (wd * 2, ht * 2)

        self.title = [
            pygame.transform.scale(img, size),  # img
            pygame.Rect((10, 20), img.get_size())  # rect
        ]

    def init_subtitle(self, game_type):
        order = ["addition", "subtraction", "multiplication", "division", "exponentiation", "square_root"]
        images = clip_set_to_list_on_yaxis(spritesets[1])

        img = images[order.index(game_type)]
        rect = pygame.Rect((12, 12), img.get_rect().size)
        self.subtitle = [img, rect]

    def draw(self, display):
        display.blit(*self.title)  # draw title
        display.blit(*self.subtitle)  # draw subtitle
