from utils import BaseMain
from game import GameTypeTitle
from .titles import Title
from .statistics import Statistics
from .buttons import Buttons
import pygame

pygame.init()


class Gameover(BaseMain):
    display_size_divider = 2.5

    def __init__(self):
        super().__init__()

        self.title = Title()
        self.statistics = Statistics()
        self.buttons = Buttons(self.display_size_divider)

    def init(self, game_type, difficulty):
        self.gt_subtitle = GameTypeTitle(game_type, difficulty)

        center_pos = (127, 55)
        type_size, lvl_size = self.gt_subtitle.get_img_sizes()

        full_wd = type_size[0] + 6 + lvl_size[0]
        
        type_pos = (center_pos[0] - (full_wd / 2), center_pos[1])
        dot_pos = (type_pos[0] + type_size[0] + 2, center_pos[1] + 2)
        level_pos = (dot_pos[0] + 2 + 2, center_pos[1])

        self.gt_positions = {
            "type": type_pos,
            "level": level_pos,
            "dot": dot_pos
        }

    def draw(self, display):
        # Fill background
        self.draw_background()

        # Draw elements
        self.title.draw(self.display)

        self.gt_subtitle.draw(self.display, self.gt_positions)
        rect = pygame.Rect(*self.gt_positions["dot"], 2, 2)
        pygame.draw.rect(self.display, (9, 10, 20), rect)

        self.statistics.draw(self.display)
        self.buttons.draw(self.display)

        # Blit display to original display
        self.blit_to_display(display)
