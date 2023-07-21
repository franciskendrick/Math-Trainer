from utils import separate_sets_from_yaxis, clip_set_to_list_on_yaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "gameover"
        )
    )

spritesets = separate_sets_from_yaxis(
    pygame.image.load(f"{resources_path}/titles.png"))


class Title:
    def __init__(self):
        img = clip_set_to_list_on_yaxis(spritesets[0])
        wd, ht = img.get_size()
        size = (wd * 4, ht * 4)

        self.title = [
            pygame.transform.scale(img, size),  # img
            pygame.Rect((36, 28), size)  # rect
        ]

    def draw(self, display):
        display.blit(*self.title)


class HighScore:
    def __init__(self):
        pass

    def draw(self, display):
        pass
