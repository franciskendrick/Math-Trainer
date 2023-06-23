from utils import BaseMain
from .question import Question
import pygame

pygame.init()


class Game(BaseMain):
    def __init__(self):
        super().__init__()

    def init_question(self, game_type, difficulty):
        self.question = Question(game_type, difficulty)
        
    def draw(self, display):
        # Fill background
        self.draw_background()

        # Draw elements
        self.question.draw(self.display)

        # Blit menu's display to original display
        self.blit_to_display(display)
