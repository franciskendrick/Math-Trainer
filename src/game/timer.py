from utils import NumberFont
import pygame
import time


class Timer(NumberFont):
    def __init__(self):
        super().__init__()

        # Box
        self.box_positions = (
            ((104, 0), (104, 21)), 
            ((104, 20), (153, 20)), 
            ((153, 0), (153, 21))
        )

        # Timer
        self.time_remaining = 300  # seconds (5 mins)
        self.delay = 1000  # milliseconds
        self.time = "5:00"

        self.timer_pos = (110, 4)

        self.last_count = time.perf_counter()

    def draw(self, display):
        for (start_pos, end_pos) in self.box_positions:
            pygame.draw.line(display, (9, 10, 20), start_pos, end_pos, 2)

        self.render_font(display, self.time, self.timer_pos, 2)

    def update_countdown(self):
        dt = time.perf_counter() - self.last_count
        if dt * 1000 >= self.delay and self.time_remaining > 0:
            self.time_remaining -= 1
            self.last_count = time.perf_counter()

            mins, secs = divmod(self.time_remaining, 60)

            self.time = "{:1d}:{:02d}".format(mins, secs)
