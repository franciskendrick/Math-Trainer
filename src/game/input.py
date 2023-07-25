from utils import NumberFont
import pygame

pygame.init()


class Input(NumberFont):
    def __init__(self, game_type, difficulty):
        super().__init__()

        difficulty = f"lvl_{difficulty}"

        # Position & maximum digit
        positions = {
            "lvl_1": (96, 162),
            "lvl_2": (78, 162),
            "lvl_3": (60, 162),
            "division": (92, 80),
            "exponentiation": (82, 158),
            "square_root": (82, 152)
        }
        max_digits = {
            "lvl_1": 2,
            "lvl_2": 3,
            "lvl_3": 4,
            "division": 3,
            "exponentiation": 4,
            "square_root": 4
        }
        if game_type in ["division", "exponentiation", "square_root"]:
            self.position = positions[game_type]
            self.max_digit = max_digits[game_type]
        else:
            self.position = positions[difficulty]
            self.max_digit = max_digits[difficulty]

        # Text
        self.text = []
        self.enlarge = 4 if game_type in ["exponentiation", "square_root"] else 6
        if game_type in ["addition", "subtraction", "multiplication"]:
            self.on_left = True
            self.will_format = True
        else:
            self.on_left = False
            self.will_format = False

    # Draw
    def draw(self, display):
        text = "".join(self.text)
        if self.will_format:
            text = self.format_text(text)
        self.render_font(display, text, self.position, self.enlarge)

    # Update
    def update_text(self, num):
        if self.on_left:
            if num == "BS" and len(self.text) > 0:
                self.text.pop(0)
                return True
            elif num != "BS" and len(self.text) < self.max_digit:
                self.text.insert(0, num)
                return True
        else:
            if num == "BS" and len(self.text) > 0:
                self.text.pop(-1)
                return True
            elif num != "BS" and len(self.text) < self.max_digit: 
                self.text.append(num)
                return True
            
        return False
                
    def get_intinput(self):
        return int("".join(self.text))

    # Format
    def format_text(self, num):
        x = [" " for _ in range(self.max_digit - len(num))] + [num]
        x = "".join(x)
        return x
