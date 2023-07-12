from utils import NumberFont
import pygame

pygame.init()


class Input(NumberFont):
    def __init__(self, game_type, difficulty):
        super().__init__()

        self.game_type = game_type
        self.difficulty = f"lvl_{difficulty}"

        # Position
        positions = {
            "lvl_1": (96, 162),
            "lvl_2": (78, 162),
            "lvl_3": (60, 162),
            "division": (92, 80),
            "exponentiation": (82, 158),
            "square_root": (82, 152)
        }
        if self.game_type in ["division", "exponentiation", "square_root"]:
            self.position = positions[self.game_type]
        else:
            self.position = positions[self.difficulty]

        # Enlarge
        self.enlarge = 4 if self.game_type in ["exponentiation", "square_root"] else 6

        # Append location
        self.on_left = True if self.game_type in ["addition", "subtraction", "multiplication"] else False

        # Text
        self.text = []

        # Maximum digits
        self.max_digits = {
            "lvl_1": 2,
            "lvl_2": 3,
            "lvl_3": 4,
        }

    def draw(self, display):
        text = "".join(self.text)
        if self.game_type in ["addition", "subtraction", "multiplication"]:
            text = self.format_text(text)
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

    def format_text(self, num):
        max_digit = self.max_digits[self.difficulty]
        x = [" " for _ in range(max_digit - len(num))] + [num]
        x = "".join(x)

        return x
