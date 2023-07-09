from utils import NumberFont
import pygame

pygame.init()


class Input(NumberFont):
    def __init__(self, game_type, difficulty):
        super().__init__()

        # Position
        positions = {
            "lvl_1": (96, 162),
            "lvl_2": (78, 162),
            "lvl_3": (60, 162),
            "division": (92, 80),
            "exponentiation": (82, 158),
            "square_root": (82, 152)
        }
        if game_type in ["division", "exponentiation", "square_root"]:
            self.position = positions[game_type]
        else:
            self.position = positions[f"lvl_{difficulty}"]

        # Enlarge
        self.enlarge = 4 if game_type in ["exponentiation", "square_root"] else 6

        # Append location
        self.on_left = True if game_type in ["addition", "subtraction", "multiplication"] else False

        # Text
        self.text = []

    def draw(self, display):
        text = "".join(self.text)
        self.render_font(display, text, self.position, self.enlarge)

    def update_text(self, num):
        if self.on_left:
            if num == "BS":  # backspace
                self.text.pop(0)
            else:  # append
                self.text.insert(0, num)
        else:
            if num == "BS":  # backspace
                self.text.pop(-1)
            else:  # append
                self.text.append(num)
