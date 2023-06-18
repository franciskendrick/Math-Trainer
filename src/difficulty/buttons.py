from utils import clip_set_to_list_on_yaxis, separate_sets_from_yaxis, palette_swap
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "difficulty"
        )
    )

spritesets = separate_sets_from_yaxis(
    pygame.image.load(f"{resources_path}/buttons.png"))


class LevelButtons:
    # Initialize
    def __init__(self, enlarge):
        # Images
        order = ["1", "2", "3"]
        images = clip_set_to_list_on_yaxis(spritesets[0])

        # Palette
        hover_palette = {
            (9, 10, 20): (9, 10, 20),
            (199, 207, 204): (168, 181, 178)
        }

        # Positions
        positions = {
            "1": (43, 53),
            "2": (43, 65),
            "3": (43, 77)
        }

        # Buttons
        self.buttons = {}
        for name, img in zip(order, images):
            # Initialize
            hover_img = palette_swap(img.convert(), hover_palette)
            rect = pygame.Rect(positions[name], img.get_rect().size)
            hitbox = pygame.Rect(
                rect.x * enlarge, rect.y * enlarge,
                rect.width * enlarge, rect.height * enlarge)

            # Append
            button = [
                False,  # is hovered
                img,  # original image
                hover_img,  # hover image
                rect,  # image rectangle
                hitbox  # hitbox
            ]
            self.buttons[name] = button

    # Draw
    def draw(self, display):
        for button in self.buttons.values():
            is_hovered, orig_img, hover_img, rect, _ = button
            img = hover_img if is_hovered else orig_img

            display.blit(img, rect)
