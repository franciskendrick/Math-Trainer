from utils.font import NumberFont
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "..", "resources", "game"
        )
    )


class BaseProblem(NumberFont):
    def draw_div(self, display, _, question):  # draw division
        x, y = question
        x_pos, y_pos, symbol_pos, ans_pos = self.positions

        # Draw
        self.render_font(display, str(x), x_pos, 3)  # x
        self.render_font(display, str(y), y_pos, 3)  # y
        display.blit(self.symbol_img, symbol_pos)  # symbol

    def draw_exp(self, display, _, question):  # draw exponentiation
        x, y = question

        if len(x) >= 2:  # x is 2 digit
            x_pos, y_pos, symbol_pos, ans_pos = self.positions["2"]
            self.render_font(display, self.format_num(x, 2), x_pos, 4)  # x
        else:  # x is 1 digit
            x_pos, y_pos, symbol_pos, ans_pos = self.positions["1"]
            self.render_font(display, self.format_num(x, 1), x_pos, 4)  # x

        self.render_font(display, str(y), y_pos, 2)  # y
        display.blit(self.symbol_img, symbol_pos)  # symbol

    def draw_sqr(self):  # Draw square root
        pass
