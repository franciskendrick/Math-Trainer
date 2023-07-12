from utils import BaseMain
from .question import Question
from .titles import GameTypeTitle, InputAppendTitle
from .timer import Timer
from .pause import Pause
from .input import Input
import pygame

pygame.init()


class Game(BaseMain):
    display_size_divider = 2.5

    def __init__(self):
        super().__init__()

        self.pause = Pause(self.display_size_divider)
        self.inputappend_title = InputAppendTitle()

    def init(self, game_type, difficulty):
        self.question = Question(game_type, difficulty)
        self.gametype_title = GameTypeTitle(game_type, difficulty)
        self.timer = Timer()
        self.input = Input(game_type, difficulty)
        self.inputappend_title.on_left = self.input.on_left
        
    def draw(self, display):
        # Fill background
        self.draw_background()

        # Draw elements
        self.question.draw(self.display)
        self.gametype_title.draw(self.display)
        self.inputappend_title.draw(self.display)
        self.timer.draw(self.display)
        self.pause.draw(self.display)
        self.input.draw(self.display)

        # Blit menu's display to original display
        self.blit_to_display(display)
