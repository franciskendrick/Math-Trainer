from utils import separate_sets_from_yaxis, clip_set_to_list_on_xaxis, clip_set_to_list_on_yaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "game"
        )
    )

type_switchcase = {
    "addition": 0,
    "subtraction": 1,
    "multiplication": 2,
    "division": 3,
    "exponentiation": 4,
    "square_root": 5
}
level_switchcase = {
    "1": 0,
    "2": 1,
    "3": 2
}

spritesets = separate_sets_from_yaxis(
    pygame.image.load(f"{resources_path}/titles.png"))


class GameTypeTitle:
    def __init__(self, game_type, difficulty):
        # Images
        self.type_imgs = clip_set_to_list_on_yaxis(spritesets[0])
        self.lvl_imgs = clip_set_to_list_on_yaxis(spritesets[1])

        # Index
        self.type_idx = type_switchcase[game_type]
        self.lvl_idx = level_switchcase[difficulty]
        
        # Positions
        self.positions = {
            "type": (158, 4),
            "level": (162, 11)
        }

    def draw(self, display):
        display.blit(self.type_imgs[self.type_idx], self.positions["type"])
        display.blit(self.lvl_imgs[self.lvl_idx], self.positions["level"])


class InputAppendTitle:
    def __init__(self):
        # Images
        order = ["left", "right"]
        self.images = {}
        for image, name in zip(clip_set_to_list_on_xaxis(spritesets[2]), order):
            wd, ht = image.get_size()
            self.images[name] = pygame.transform.scale(image, (wd * 2, ht * 2))

        # Positions
        self.positions = {
            "left": (55, 5),
            "right": (47, 5)
        }

        # Type
        self.on_left = None

    def draw(self, display):
        key = "left" if self.on_left else "right"
        display.blit(self.images[key], self.positions[key])
