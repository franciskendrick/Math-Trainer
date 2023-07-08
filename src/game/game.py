from utils import BaseMain
from .question import Question
from .titles import Titles
from .timer import Timer
from .pause import Pause
import pygame

pygame.init()


class Game(BaseMain):
    display_size_divider = 2.5

    def __init__(self):
        super().__init__()

        self.pause = Pause(self.display_size_divider)

    def init(self, game_type, difficulty):
        self.question = Question(game_type, difficulty)
        self.titles = Titles(game_type, difficulty)
        self.timer = Timer()
        
    def draw(self, display):
        # Fill background
        self.draw_background()

        # Draw elements
        self.question.draw(self.display)
        self.titles.draw(self.display)
        self.timer.draw(self.display)
        self.pause.draw(self.display)

        # Blit menu's display to original display
        self.blit_to_display(display)
