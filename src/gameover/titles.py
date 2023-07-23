from utils import NumberFont, separate_sets_from_yaxis, clip_set_to_list_on_yaxis
from window import window
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


class HighScore(NumberFont):
    def __init__(self):
        super().__init__()

        self.title_img = clip_set_to_list_on_yaxis(spritesets[1])
        self.title_size = (55, 6)

        self.center_pos = (127, 55)

        self.highscore = str(window.gameinfo_data["highscore"])

    def draw(self, display):
        # Title
        score_size = self.get_size(self.highscore)
        full_wd = self.title_size[0] + score_size[0]
        pos = (self.center_pos[0] - (full_wd / 2), self.center_pos[1])

        display.blit(self.title_img, pos)

        # Score
        pos = (pos[0] + 55 + 2, pos[1])
        self.render_font(display, self.highscore, pos)
