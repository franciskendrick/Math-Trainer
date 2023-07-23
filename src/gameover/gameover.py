from utils import BaseMain
from game import GameTypeTitle
from .titles import Title, HighScore
from .statistics import Statistics
from .buttons import Buttons
import pygame

pygame.init()
gt_positions = {
    "type": (4, 4),
    "level": (8, 11)
}


class Gameover(BaseMain):
    display_size_divider = 2.5

    def __init__(self):
        super().__init__()

        self.title = Title()
        self.highscore = HighScore()
        self.statistics = Statistics()
        self.buttons = Buttons(self.display_size_divider)

    def init(self, game_type, difficulty):
        self.gt_subtitle = GameTypeTitle(game_type, difficulty)

    def draw(self, display):
        # Fill background
        self.draw_background()

        # Draw elements
        self.gt_subtitle.draw(self.display, gt_positions)
        self.highscore.draw(self.display)
        self.title.draw(self.display)
        self.statistics.draw(self.display)
        self.buttons.draw(self.display)

        # Blit display to original display
        self.blit_to_display(display)
