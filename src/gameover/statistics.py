from utils import NumberFont, separate_sets_from_yaxis, clip_set_to_list_on_yaxis
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


class Statistics(NumberFont):
    def __init__(self):
        super().__init__()

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

        # Statistics
        self.stats_positions = {
            "ans_acc": (113, 85),
            "key_acc": (113, 107),
            "score": (95, 129),
            "wrg_ans": (115, 151),
            "mistakes": (129, 173)
        }
        self.stats_colors = {
            "ans_acc": "green",
            "key_acc": "green",
            "score": "green",
            "wrg_ans": "red",
            "mistakes": "red"
        }

    def init_stats(self, stats):
        self.stats = {}

        self.stats["ans_acc"] = self.get_accuracy(stats["score"], stats["wrg_ans"])
        self.stats["key_acc"] = self.get_accuracy(stats["key_presses"], stats["mistakes"])
        self.stats["score"] = str(stats["score"])
        self.stats["wrg_ans"] = str(stats["wrg_ans"])
        self.stats["mistakes"] = str(stats["mistakes"])

    def draw(self, display):
        for title in self.titles:
            display.blit(*title)

        for (start_pos, end_pos) in self.lines:
            pygame.draw.line(display, (199, 207, 204), start_pos, end_pos, 2)

        for (text, pos, color) in zip(self.stats.values(), self.stats_positions.values(), self.stats_colors.values()):
            self.render_font(display, text, pos, enlarge=2, color=color)

    def get_accuracy(self, observed_value, mistakes):
        true_value = observed_value - mistakes
        accuracy = (100 - ((observed_value - true_value) / true_value * 100))
        return f"{round(accuracy, 2)}%"
