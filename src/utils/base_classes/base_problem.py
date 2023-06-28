from utils.font import NumberFont
from utils.image_editors import clip_set_to_list_on_xaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "..", "resources", "game"
        )
    )

# Problem Generators
attachments = clip_set_to_list_on_xaxis(
    pygame.image.load(f"{resources_path}/attachments.png"))


class BaseProblem(NumberFont):
    def init_symbol(self, idx):
        super().__init__()

        # Symbol image
        image = attachments[idx]
        wd, ht = image.get_size()
        self.symbol_img = pygame.transform.scale(image, (wd * 3, ht * 3))

    # Draw
    def draw(self, display, level, question):
        x, y = question
        x_pos, y_pos, symbol_pos, line_pos, ans_pos = self.positions[level]

        self.render_font(display, self.format_num(x, level, 0), x_pos, 3)  # x
        self.render_font(display, self.format_num(y, level, 1), y_pos, 3)  # y
        display.blit(self.symbol_img, symbol_pos)  # symbol
        pygame.draw.line(display, (9, 10, 20), *line_pos, 3)  # line

    # Functions
    def format_num(self, num, level, idx):
        max_digit = self.max_digits[level][idx]
        x = [" " for _ in range(max_digit - len(str(num)))] + [str(num)]
        x = "".join(x)

        return x
