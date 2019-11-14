import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass, Brick
from ball import Ball, BigBall

name = "MainState"

boy = None
grass = None
brick = None
balls = []
big_balls = []


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]
    game_world.add_objects(balls,1)

    global brick
    brick = Brick()
    game_world.add_object(brick, 0)


def exit():
    game_world.clear()

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
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


    if collide(brick, boy):
        if boy.x <= brick.x and boy.y <= brick.y + 20:
            boy.x = brick.x - 140
        elif boy.x >= brick.x and boy.y <= brick.y + 20:
            boy.x = brick.x + 140
        else:
            boy.air = False
            boy.x += brick.dir * brick.speed
    else:
        boy.air = True
        if collide(grass, boy):
            boy.air = False



    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)
    for ball in balls:
        if collide(grass, ball):
            ball.stop()

        if collide(brick, ball):
            if ball.size == 0:
                if ball.x <= brick.x and ball.y <= brick.y + 20:
                    ball.x = brick.x - 100
                elif ball.x >= brick.x and ball.y <= brick.y + 20:
                    ball.x = brick.x + 100
                else:
                    ball.stop()
                    ball.x += brick.dir * brick.speed
            elif ball.size == 1:
                if ball.size == 1:
                    if ball.x <= brick.x and ball.y <= brick.y + 20:
                        ball.x = brick.x - 110
                    elif ball.x >= brick.x and ball.y <= brick.y + 20:
                        ball.x = brick.x + 110
                    else:
                        ball.stop()
                        ball.x += brick.dir * brick.speed


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






