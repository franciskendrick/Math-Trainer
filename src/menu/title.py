import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "menu"
        )
    )


class Title:
    def __init__(self):
        img = pygame.image.load(
            f"{resources_path}/title.png")
        wd, ht = img.get_size()
        size = (wd * 2, ht * 2)

        self.img = pygame.transform.scale(img, size)
        self.rect = pygame.Rect((26, 12), self.img.get_size())

    def draw(self, display):
        display.blit(self.img, self.rect)
