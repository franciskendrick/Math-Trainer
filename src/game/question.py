from utils import BaseProblem
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
    def __init__(self, game_type, difficulty):
        # Game type
        gametype_switchcase = {
            "addition": Addition,
            "subtraction": Subtraction,
            "multiplication": Multiplication,
            "division": Division,
            "exponentiation": Exponentiation,
            "square_root": SquareRoot 
        }

        self.game_type = gametype_switchcase[game_type]()

        # Difficulty
        self.level = difficulty
        if game_type not in ["exponentiation", "square_root"]:
            self.level_switchcase = {
                "1": self.game_type.level_1,
                "2": self.game_type.level_2,
                "3": self.game_type.level_3
            }
        else:
            self.level_switchcase = {
                "1": self.game_type.level_1,
                "2": self.game_type.level_2,
            }

    def draw(self, display):
        self.game_type.draw(display, self.level, self.question)

    def get_question(self):
        self.question = self.level_switchcase[self.level]()


# Problem Generators
class Addition(BaseProblem):
    def __init__(self):
        super().__init__()

        # Symbol
        self.init_symbol(0)

        # Positions
        self.positions = {  # x, y, symbol, line, answer
            "1": ((66, 30), (66, 54), (51, 60), ((42, 76), (86, 76)), (48, 81)),
            "2": ((57, 30), (57, 54), (42, 60), ((33, 76), (95, 76)), (39, 81)),
            "3": ((48, 30), (48, 54), (30, 60), ((24, 76), (104, 76)), (30, 81))
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
    

class Subtraction(BaseProblem):
    def __init__(self):
        super().__init__()

        # Symbol
        self.init_symbol(1)

        # Positions
        self.positions = {  # x, y, symbol, line, answer
            "1": ((48, 30), (66, 54), (51, 60), ((42, 76), (86, 76)), (48, 81)),
            "2": ((57, 30), (57, 54), (42, 60), ((33, 76), (95, 76)), (39, 81)),
            "3": ((48, 30), (48, 54), (30, 60), ((24, 76), (104, 76)), (30, 81))
        }

        # Maximum digits
        self.max_digits = {
            "1": (2, 1),
            "2": (2, 2),
            "3": (3, 3)
        }

    # Question generator
    def level_1(self):
        x = random.randint(0, 18)
        y = random.randint(0, 9)
        return x, y

    def level_2(self):
        x = random.randint(10, 99)
        y = random.randint(10, x)
        return x, y

    def level_3(self):
        x = random.randint(100, 999)
        y = random.randint(100, x)
        return x, y
    

class Multiplication(BaseProblem):
    def __init__(self):
        super().__init__()

        # Symbol
        self.init_symbol(2)

        # Positions
        self.positions = {  # x, y, symbol, line, answer
            "1": ((66, 30), (66, 54), (51, 60), ((42, 76), (86, 76)), (48, 81)),
            "2": ((57, 30), (75, 54), (42, 60), ((33, 76), (95, 76)), (39, 81)),
            "3": ((48, 30), (84, 54), (30, 60), ((24, 76), (104, 76)), (30, 81))
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
        y = random.randint(0, 9)
        return x, y

    def level_3(self):
        x = random.randint(100, 999)
        y = random.randint(0, 9)
        return x, y
    

class Division(BaseProblem):
    def __init__(self):
        # Symbol
        self.init_symbol(3)

        # Positions (x, y, symbol, answer)
        self.positions = ((49, 67), (19, 67), (40, 61), (46, 40))

        # Maximum digits
        self.max_digits = {
            "1": (2, 1),
            "2": (3, 1),
            "3": (3, 1)
        }

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

        self.render_font(display, str(x), x_pos, 3)  # x
        self.render_font(display, str(y), y_pos, 3)  # y
        display.blit(self.symbol_img, symbol_pos)  # symbol


class Exponentiation:
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


class SquareRoot:
    # Question generator
    def level_1(self):
        squares = [i ** 2 for i in range(1, 10)]
        return random.choice(squares)

    def level_2(self):
        squares = [i ** 2 for i in range(10, 100)]
        return random.choice(squares)
