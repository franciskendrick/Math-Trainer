from utils.image_editors import palette_swap
import pygame

pygame.init()

hover_palette = {
    (9, 10, 20): (9, 10, 20),
    (199, 207, 204): (168, 181, 178)
}


class BaseButtons:
    # Initialize
    def init_buttons(self, enlarge, order, images, positions):
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


class BaseButton:
    # Initialize
    def init_button(self, enlarge, image, position):
        # Initialize
        hover_img =  palette_swap(image.convert(), hover_palette)
        rect = pygame.Rect(position, image.get_rect().size)
        hitbox = pygame.Rect(
            rect.x * enlarge, rect.y * enlarge,
            rect.width * enlarge, rect.height * enlarge)

        # Append
        self.button = [
            False,  # is hovered
            image,  # original image
            hover_img,  # hover image
            rect,  # image rectangle
            hitbox  # hitbox
        ]

    # Draw
    def draw(self, display):
        is_hovered, orig_img, hover_img, rect, _ = self.button
        img = hover_img if is_hovered else orig_img

        display.blit(img, rect)

    # Action detection
    def button_down_detection(self):
        *_, hitbox = self.button

        mouse_pos = pygame.mouse.get_pos()
        if hitbox.collidepoint(mouse_pos):
            return True

    def button_over_detection(self):
        *_, hitbox = self.button
            
        mouse_pos = pygame.mouse.get_pos()
        self.button[0] = True if hitbox.collidepoint(mouse_pos) else False

    # Functions
    def reset_overdetection(self):
        self.button[0] = False
