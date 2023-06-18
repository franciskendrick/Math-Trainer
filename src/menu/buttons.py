from utils import clip_set_to_list_on_yaxis, palette_swap
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "menu"
        )
    )


class Buttons:
    # Initialize
    def __init__(self, enlarge):
        # Images
        order = ["addition", "subtraction", "multiplication", "division", "exponentiation", "square_root"]
        images = clip_set_to_list_on_yaxis(
            pygame.image.load(f"{resources_path}/buttons.png"))

        # Palette
        hover_palette = {
            (9, 10, 20): (9, 10, 20),
            (199, 207, 204): (168, 181, 178)
        }
        
        # Positions
        positions = {
            "addition": (41, 46),
            "subtraction": (31, 58),
            "multiplication": (23, 70),
            "division": (41, 82),
            "exponentiation": (23, 94),
            "square_root": (31, 106)
        }

        # Buttons
        self.buttons = {}
        for name, img in zip(order, images):
            # Inititalize
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

    # Action detection
    def button_down_detection(self):
        for (name, button) in self.buttons.items():
            *_, hitbox = button

            mouse_pos = pygame.mouse.get_pos()
            if hitbox.collidepoint(mouse_pos):
                return name

    def button_over_detection(self):
        for button in self.buttons.values():
            *_, hitbox = button
            
            mouse_pos = pygame.mouse.get_pos()
            button[0] = True if hitbox.collidepoint(mouse_pos) else False

    # Functions
    def reset_overdetection(self):
        for button in self.buttons.values():
            button[0] = False
