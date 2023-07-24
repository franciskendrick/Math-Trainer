from utils import palette_swap
from .font_to_dict import clip_font_to_dict
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..", "..", "..", "resources", "font"
    )
)


class NumberFont:
    order = [
        "0", "1", "2", "3", "4",
        "5", "6", "7", "8", "9",
        ":", ",", ".", "%"
    ]
    colors = {
        "black": (9, 10, 20),
        "green": (70, 130, 50),
        "red": (165, 48, 48)
    }
    character_spacing = 1

    def __init__(self):
        # Font spriteset
        font_set = pygame.image.load(
            f"{resources_path}/number_font.png")

        self.characters = {}
        for (name, color) in self.colors.items():
            # Get font set in different colors
            # if name != "black":
            palette = {
                self.colors["black"]: color
            }
            font_set_ = palette_swap(font_set.convert(), palette)

            # Get characters in a dictionary form
            self.characters[name] = clip_font_to_dict(
                font_set_, self.order)
        
        # Space
        self.space = 5

    def render_font(self, display, text, pos, enlarge=1, color="black"):
        handle_display = pygame.Surface(
            display.get_size(), pygame.SRCALPHA)
        x, y = pos
        x_offset = 0

        # Pick color
        characters = self.characters[color]

        # Loop over every character in text
        for char in text:
            if char != " ":  # a number
                # Get character image
                character = characters[char]

                # Resize
                wd, ht = character.get_size()
                character = pygame.transform.scale(
                    character, (wd * enlarge, ht * enlarge))

                spacing = self.character_spacing * enlarge

                # Blit to handle display
                handle_display.blit(character, (x + x_offset, y))

                # Add to offset the width of resized character and spacing
                x_offset += character.get_width() + spacing
            else:  # a space
                # spacing = (self.character_spacing * enlarge) if enlarge != 1 else self.character_spacing
                x_offset += (self.space + self.character_spacing) * enlarge

        # Blit to display
        display.blit(handle_display, (0, 0))

    def get_size(self, text, enlarge=1):
        characters = self.characters["black"]
        wd = 0
        for i, char in enumerate(text, 1):
            if char != " ":  # a number
                # Get character image
                character = characters[char]

                # Resize
                character_wd, _ = character.get_size()
                character_wd = character_wd * enlarge
                spacing = (self.character_spacing * enlarge) if len(text) > i else 0
                    
                # Add to width
                wd += character_wd + spacing
            else:  # a space
                # Add to width
                wd += (self.space + self.character_spacing) * enlarge

        return (wd, 6 * enlarge)
