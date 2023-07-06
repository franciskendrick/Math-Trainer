from utils import separate_sets_from_yaxis, clip_set_to_list_on_yaxis
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


class Titles:
    def __init__(self, game_type, difficulty):
        # Images
        spritesets = separate_sets_from_yaxis(
            pygame.image.load(f"{resources_path}/titles.png"))
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
