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
    def __init__(self):
        self.addition = Addition()
        self.subtraction = Subtraction()
        self.multiplication = Multiplication()
        self.division = Division()
        self.exponentiation = Exponentiation()
        self.square_root = SquareRoot()


# Problem Generators
class Addition:
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


class Subtraction:
    def level_1(self):
        x = random.randint(0, 18)
        y = random.randint(0, x)
        return x, y

    def level_2(self):
        x = random.randint(10, 99)
        y = random.randint(10, x)
        return x, y

    def level_3(self):
        x = random.randint(100, 999)
        y = random.randint(100, x)
        return x, y


class Multiplication:
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


class Division:
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
        
        return divisors

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


class Exponentiation:
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
    def level_1(self):
        squares = [i ** 2 for i in range(1, 10)]
        return random.choice(squares)

    def level_2(self):
        squares = [i ** 2 for i in range(10, 100)]
        return random.choice(squares)
