import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "resources"
        )
    )


class Window:
    # Window
    rect = pygame.Rect(0, 0, 640, 640)

    def __init__(self):
        # Game information
        with open(f"{resources_path}/gameinfo.json") as json_file:
            self.gameinfo_data = json.load(json_file)

    def update_gameinfo(self, highscore_value):
        # Get handle information
        handle_gameinfo = self.gameinfo_data.copy()

        # Edit highscore value
        handle_gameinfo["highscore"] = highscore_value

        # Append
        with open(f"{resources_path}/gameinfo.json", "w") as json_file:
            json.dump(handle_gameinfo, json_file)


window = Window()
