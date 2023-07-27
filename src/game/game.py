from utils import BaseMain
from .question import Question
from .titles import GameTypeTitle, InputAppendTitle
from .timer import Timer
from .input import Input
import pygame
import time

pygame.init()


class Game(BaseMain):
    display_size_divider = 2.5
    bg_colors = {
        "correct": (208, 218, 145),
        "wrong": (187, 108, 107),
        "default": (235, 237, 233)
    }

    def __init__(self):
        super().__init__()

        # Background
        self.bg_color = self.bg_colors["default"]
        self.time_remaining = 1  # seconds
        self.delay = 1000  # milliseconds
        self.bg_changed = False
        self.last_count = time.perf_counter()

        self.inputappend_title = InputAppendTitle()

    def init(self, game_type, difficulty):
        self.question = Question(game_type, difficulty)
        self.gametype_title = GameTypeTitle(game_type, difficulty)
        self.timer = Timer()
        self.input = Input(game_type, difficulty)
        self.inputappend_title.on_left = self.input.on_left
        
    def draw(self, display):
        # Fill background
        self.draw_background(bgcolor=self.bg_color)

        # Draw elements
        self.question.draw(self.display)
        self.gametype_title.draw(self.display)
        self.inputappend_title.draw(self.display)
        self.timer.draw(self.display)
        self.input.draw(self.display)

        # Blit display to original display
        self.blit_to_display(display)

    def update_background(self):
        dt = time.perf_counter() - self.last_count
        if self.bg_changed and dt * 1000 >= self.delay and self.time_remaining > 0:
            self.time_remaining -= 1
            self.last_count = time.perf_counter()
        elif self.time_remaining == 0:
            self.bg_color = self.bg_colors["default"]

            self.time_remaining = 1  # seconds
            self.bg_changed = False
