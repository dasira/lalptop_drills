import game_framework
from pico2d import *

import game_world
import random
import main_state

#1280 , 1024
class Ball:
    image = None
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(50, 1800 - 10), random.randint(200, 1100 - 10)

    def get_bb(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        return cx - 10, cy - 10, cx + 10, cy + 10

    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(cx, cy)
        draw_rectangle(*self.get_bb())

    def set_background(self, bg):
        self.bg = bg
        self.x = self.x
        self.y = self.y

    def update(self):
        pass

    def stop(self):
        pass