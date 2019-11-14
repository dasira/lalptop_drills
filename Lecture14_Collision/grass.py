from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        draw_rectangle(*self.get_bb())

    # fill here
    def get_bb(self):
        return 0, 0, 800 - 1, 50

class Brick:
    def __init__(self):
        self.x, self.y = 180 , 200
        self.speed = 1
        self.dir = 1
        self.image = load_image('brick180x40.png')

    def update(self):
        if self.x >= 800 - 90:
            self.dir = -1
        elif self.x <= 0 + 90:
            self.dir = 1
        self.x += self.dir * self.speed
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20