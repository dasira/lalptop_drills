import game_framework
from pico2d import *

import game_world
import random

#1280 , 1024
class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(10, 1280 - 10), random.randint(10, 1024 - 10)
        self.size = 0
    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def stop(self):
        pass