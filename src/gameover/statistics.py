from utils import separate_sets_from_yaxis, clip_set_to_list_on_yaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "gameover"
        )
    )

spritesets = separate_sets_from_yaxis(
    pygame.image.load(f"{resources_path}/titles.png"))


class Statistics:
    def __init__(self):
        # Titles
        self.titles = []
        for i, img in enumerate(clip_set_to_list_on_yaxis(spritesets[2])):
            wd, ht = img.get_size()
            size = (wd * 2, ht * 2)
            
            title = [
                pygame.transform.scale(img, size),  # img
                pygame.Rect((27, 85+(22*i)), size)  # rect
            ]
            self.titles.append(title)

        # Lines 
        self.lines = [((23, i), (232, i)) for i in range(79, 189+1, 22)]

    def draw(self, display):
        for title in self.titles:
            display.blit(*title)

        for (start_pos, end_pos) in self.lines:
            pygame.draw.line(display, (199, 207, 204), start_pos, end_pos, 2)
