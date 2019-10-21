import game_framework
import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state


name = "MainState"
time = 0.0

boy = None
grass = None
pause = None
font = None


class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.frame = 0
    def draw(self):
        self.image.clip_draw(200,200,500,500,400,300,300,300)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = main_state.boy.x, 90
        self.frame = main_state.boy.frame
        self.image = load_image('run_animation.png')
        self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global boy, grass, pause
    boy = Boy()
    grass = Grass()
    pause = Pause()


def exit():
    global boy, grass, pause
    del(boy)
    del(grass)
    del(pause)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def update():
    global time
    time =(time + 1) % 300

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    if (time >150):
        pause.draw()
    update_canvas()





