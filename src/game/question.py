from utils import NumberFont, clip_set_to_list_on_xaxis
from math import sqrt
import pygame
import random
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "game"
        )
    )


class Question:
    add = lambda _, q: q[0] + q[1] 
    subtract = lambda _, q: q[0] - q[1]
    multiply = lambda _, q: q[0] * q[1]
    divide = lambda _, q: q[0] // q[1]
    exponentiate = lambda _, q: q[0] ** q[1]
    square_root = lambda _, q: int(sqrt(q))

    def __init__(self, game_type, difficulty):
        # Solve
        self.solve = {
            "addition": self.add,
            "subtraction": self.subtract,
            "multiplication": self.multiply,
            "division": self.divide,
            "exponentiation": self.exponentiate,
            "square_root": self.square_root
        }

        # Game type
        gametype_switchcase = {
            "addition": Addition,
            "subtraction": Subtraction,
            "multiplication": Multiplication,
            "division": Division,
            "exponentiation": Exponentiation,
            "square_root": SquareRoot 
        }

        self.game_type = game_type
        self.generator = gametype_switchcase[game_type]()

        # Difficulty
        self.level = difficulty
        if game_type not in ["exponentiation", "square_root"]:
            self.level_switchcase = {
                "1": self.generator.level_1,
                "2": self.generator.level_2,
                "3": self.generator.level_3
            }
        else:
            self.level_switchcase = {
                "1": self.generator.level_1,
                "2": self.generator.level_2,
            }

    def draw(self, display):
        self.generator.draw(display, self.level, self.question)

    def get_question(self):
        self.question = self.level_switchcase[self.level]()
        self.answer = self.solve[self.game_type](self.question)


# Problem Generators
attachments = clip_set_to_list_on_xaxis(
    pygame.image.load(f"{resources_path}/attachments.png"))


def get_symbol(idx):
    # Symbol image
    image = attachments[idx]
    wd, ht = image.get_size()
    symbol_img = pygame.transform.scale(image, (wd * 6, ht * 6))

    return symbol_img


def format_num(num, max_digit):
    x = [" " for _ in range(max_digit - len(str(num)))] + [str(num)]
    x = "".join(x)

    return x


class Draw(NumberFont):
    def draw(self, display, level, question):  # draws addition, subtraction, multiplication
        x, y = question
        x_pos, y_pos, symbol_pos, line_pos, ans_pos = self.positions[level]

        # Get x and y's string format
        x_str = format_num(x, self.max_digits[level][0])
        y_str = format_num(y, self.max_digits[level][1])

        # Draw
        self.render_font(display, x_str, x_pos, 6)  # x
        self.render_font(display, y_str, y_pos, 6)  # y
        display.blit(self.symbol_img, symbol_pos)  # symbol
        pygame.draw.line(display, (9, 10, 20), *line_pos, 6)  # line


class Addition(Draw):
    def __init__(self):
        super().__init__()

        # Symbol
        self.symbol_img = get_symbol(0)

        # Positions
        self.positions = {  # x, y, symbol, line, answer
            "1": ((132, 60), (132, 108), (102, 120), ((84, 152), (172, 152)), (96, 162)),  # level 1
            "2": ((114, 60), (114, 108), (84, 120), ((66, 152), (190, 152)), (78, 162)),  # level 2
            "3": ((96, 60), (96, 108), (60, 120), ((48, 152), (208, 152)), (60, 162))  # level 3
        }

        # Maximum digits
        self.max_digits = {
            "1": (1, 1),
            "2": (2, 2),
            "3": (3, 3)
        }

    # Question generator
    def level_1(self):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y

    def level_2(self):
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y

    def level_3(self):
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y
    

class Subtraction(Draw):
    def __init__(self):
        super().__init__()

        # Symbol
        self.symbol_img = get_symbol(1)

        # Positions
        self.positions = {  # x, y, symbol, line, answer
            "1": ((96, 60), (132, 108), (102, 120), ((84, 152), (172, 152)), (96, 162)),  # level 1
            "2": ((114, 60), (114, 108), (84, 120), ((66, 152), (190, 152)), (78, 162)),  # level 2
            "3": ((96, 60), (96, 108), (60, 120), ((48, 152), (208, 152)), (60, 162))  # level 3
        }

        # Maximum digits
        self.max_digits = {
            "1": (2, 1),
            "2": (2, 2),
            "3": (3, 3)
        }

    # Question generator
    def level_1(self):
        x = random.randint(1, 18)
        limit = 9 if x > 9 else x-1
        y = random.randint(0, limit)
        return x, y

    def level_2(self):
        x = random.randint(10, 99)
        y = random.randint(10, x)
        return x, y

    def level_3(self):
        x = random.randint(100, 999)
        y = random.randint(100, x)
        return x, y
    

class Multiplication(Draw):
    def __init__(self):
        super().__init__()

        # Symbol
        self.symbol_img = get_symbol(2)

        # Positions
        self.positions = {  # x, y, symbol, line, answer
            '1': [(132, 60), (132, 108), (102, 120), [(84, 152), (172, 152)], (96, 162)],  # level 1
            '2': [(114, 60), (150, 108), (84, 120), [(66, 152), (190, 152)], (78, 162)],  # level 2
            '3': [(96, 60), (168, 108), (60, 120), [(48, 152), (208, 152)], (60, 162)]  # level 3
        }

        # Maximum digits
        self.max_digits = {
            "1": (1, 1),
            "2": (2, 1),
            "3": (3, 1)
        }

    # Question generator
    def level_1(self):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y

    def level_2(self):
        x = random.randint(10, 99)
        y = random.randint(1, 9)
        return x, y

    def level_3(self):
        x = random.randint(100, 999)
        y = random.randint(2, 9)
        return x, y
    

class Division(NumberFont):
    def __init__(self):
        super().__init__()

        # Symbol
        self.symbol_img = get_symbol(3)

        # Positions (x, y, symbol, answer)
        self.positions = ((98, 134), (38, 134), (80, 122), (92, 80))

    # Question generator
    def level_1(self):
        x = random.randint(0, 99)
        divisors = self.get_divisors(x)
        weights = self.get_weights(divisors)
        [y] = random.choices(divisors, weights=weights)
        return x, y

    def level_2(self):
        x = random.randint(10, 999)
        divisors = self.get_divisors(x)
        weights = self.get_weights(divisors)
        [y] = random.choices(divisors, weights=weights)
        return x, y

    def level_3(self):
        x = random.randint(100, 999)
        divisors = self.get_divisors(x)
        weights = self.get_weights(divisors)
        [y] = random.choices(divisors, weights=weights)
        return x, y

    # Functions
    def get_divisors(self, x):
        divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        new_divisors = []
        for divisor in divisors:
            if x % divisor == 0:  # divisible by divisor
                new_divisors.append(divisor)
        
        return new_divisors

    def get_weights(self, divisors):
        num_divisors = len(divisors)
        if num_divisors > 1:
            normal_weight = 100 / num_divisors
            ones_weight = normal_weight / 10  # 1's weight
            others_weight = normal_weight + ((ones_weight * 9) / (num_divisors-1))  # every other number's weight

            weights = [ones_weight] + [others_weight for _ in range(num_divisors - 1)]
        else:
            weights = [100]

        return weights
    
    # Draw
    def draw(self, display, _, question):
        x, y = question
        x_pos, y_pos, symbol_pos, ans_pos = self.positions

        # Draw
        self.render_font(display, str(x), x_pos, 6)  # x
        self.render_font(display, str(y), y_pos, 6)  # y
        display.blit(self.symbol_img, symbol_pos)  # symbol


class Exponentiation(NumberFont):
    def __init__(self):
        super().__init__()

        # Positions
        self.positions = {  # x, y, answer
            1: ((96, 94), (140, 78), (82, 158)),  # x is 1 digit
            2: ((72, 94), (164, 78), (82, 158))  # x is 2 digit
        }

    # Question generator
    def level_1(self):
        x = random.randint(0, 9)
        [y] = random.choices([0, 1, 2, 3], [10, 10, 40, 40])  # discourage 0 and 1
        return x, y

    def level_2(self):
        x = random.randint(0, 99)
        if x >= 10:  # x is a double digit
            # if x is less than or equal than 21, y = 2 or 3; if x is greater than 21, y = 2
            y = random.randint(2, 3) if x <= 21 else 2
        else:  # x is a single digit
            y = random.randint(3, 5)

        return x, y

    # Draw
    def draw(self, display, _, question):
        x, y = question

        # Get x and y's string format
        x_str = str(x)
        y_str = str(y)

        # Draw
        x_pos, y_pos, ans_pos = self.positions[len(x_str)]
        self.render_font(display, format_num(x, len(x_str)), x_pos, 8)  # x
        self.render_font(display, y_str, y_pos, 4)  # y


class SquareRoot(NumberFont):
    def __init__(self):
        super().__init__()

        # Symbol
        self.symbol_img = get_symbol(4)

        # Positions
        self.positions = {  # x, symbol, line, answer
            1: ((126, 92), (90, 80), ((114, 82), (166, 82)), (82, 152)),  # digit 1
            2: ((108, 92), (72, 80), ((96, 82), (184, 82)), (82, 152)),  # digit 2
            3: ((90, 92), (54, 80), ((78, 82), (202, 82)), (82, 152)),  # digit 3
            4: ((72, 92), (36, 80), ((60, 82), (220, 82)), (82, 152))  # digit 4
        }

        self.used_questions = []

    # Question generator
    def level_1(self):
        squares = [i ** 2 for i in range(1, 10)]
        x = random.choice(squares)

        if x in self.used_questions:
            self.level_1()
        else:
            if len(self.used_questions) >= 5:
                self.used_questions.pop(-1)
            self.used_questions.insert(0, x)

        return x

    def level_2(self):
        squares = [i ** 2 for i in range(10, 100)]
        return random.choice(squares)
    
    # Draw
    def draw(self, display, _, question):
        x_str = str(question)
        x_pos, symbol_pos, line_pos, ans_pos = self.positions[len(x_str)]

        # Draw
        self.render_font(display, x_str, x_pos, 6)  # x
        display.blit(self.symbol_img, symbol_pos)  # symbol
        pygame.draw.line(display, (9, 10, 20), *line_pos, 6)  # line
