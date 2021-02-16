import numpy as np
import colorama as cl
from colorama import Fore, Back, Style
import config as cfg
import os
from time import sleep
from brick import Brick1, Brick2, Brick3, Brick4
from paddle import Paddle
from inputter import Input
from ball import Ball


cl.init()
pd = Paddle()
ball = Ball()
ip = Input()
dir = 0
key_press = ''
idx = 0
level = 1
attached = True
speed = 0


def set_bricks():
    x_co = 1
    y_co = 1

    for char in level_string:
        # print(char)
        Brick = None
        if(char == '1'):
            Brick = Brick1
        if(char == '2'):
            Brick = Brick2
        if(char == '3'):
            Brick = Brick3
        if(char == '4'):
            Brick = Brick4

        if(Brick != None):
            obj = Brick(x_left=x_co, y=y_co)
            BRICKS.append(obj)

        if(char == '\n'):
            x_co = 1
            y_co += 1

        x_co += cfg.BRICK_LENGTH


def print_bricks():
    for brick in BRICKS:
        brick.display(CANVAS)


# INITIALIZING THE CANVAS
CANVAS = [[' ']*cfg.WIDTH for _ in range(cfg.HEIGHT)]
BRICKS = []

# INITIALIZING THE FRAME IN CANVAS
CANVAS[0][0] = '╔'
CANVAS[0][cfg.WIDTH-1] = '╗'
CANVAS[cfg.HEIGHT-1][0] = '╚'
CANVAS[cfg.HEIGHT-1][cfg.WIDTH-1] = '╝'
for x in range(1, cfg.WIDTH-1):
    CANVAS[0][x] = '═'
    CANVAS[cfg.HEIGHT-1][x] = '═'
for x in range(1, cfg.HEIGHT-1):
    CANVAS[x][0] = '║'
    CANVAS[x][cfg.WIDTH-1] = '║'

# READ LEVEL
file = None
if (level == 1):
    file = open(r'./Levels/Level_1.txt', 'r')
if (level == 2):
    file = open(r'./Levels/Level_2.txt', 'r')
if (level == 3):
    file = open(r'./Levels/Level_3.txt', 'r')
level_string = file.read()


os.system("stty -echo")
set_bricks()

while key_press != 'q':
    os.system('clear')

    print_bricks()
    ball.ball_paddle_collision(pd)
    ball.ball_wall_collision()
    # print(level_string)
    ball.ball_brick_collision(bricks=BRICKS, canvas=CANVAS)
    # print(level_string)
    # input()

    pd.display(CANVAS)
    ball.display(CANVAS)

    # PRINTING THE HEADER
    print(cfg.COLORS[idx] + cfg.HEADER + Fore.RESET)
    idx = (idx + 1) % 7

    CANVAS[0][0] = '╔'
    CANVAS[0][cfg.WIDTH-1] = '╗'
    CANVAS[cfg.HEIGHT-1][0] = '╚'
    CANVAS[cfg.HEIGHT-1][cfg.WIDTH-1] = '╝'
    for x in range(1, cfg.WIDTH-1):
        CANVAS[0][x] = '═'
        CANVAS[cfg.HEIGHT-1][x] = '═'
    for x in range(1, cfg.HEIGHT-1):
        CANVAS[x][0] = '║'
        CANVAS[x][cfg.WIDTH-1] = '║'

    # PRINTING THE CANVAS
    for i in range(cfg.HEIGHT):
        print(cfg.LEFT_PADDING, end="")
        for j in range(cfg.WIDTH):
            print(CANVAS[i][j], end="")
        print()

    if attached:
        print(Fore.WHITE + 'Press ' + Fore.GREEN + 'spacebar' +
              Fore.WHITE + ' to release ball' + Fore.RESET)

    print(Fore.WHITE + 'Press ' + Fore.GREEN + 'a' + Fore.WHITE + ' and ' +
          Fore.GREEN + 'd' + Fore.WHITE + ' to move left or right respectively'
          + Fore.RESET)

    print(Fore.WHITE + 'Press ' + Fore.RED + 'q' +
          Fore.WHITE + ' to quit' + Fore.RESET)

    # TAKING INPUT
    key_press = ip.get_parsed_input(timeout=0.07)
    if key_press == 'd':
        pd.move_paddle(CANVAS, 3)
        if attached:
            ball.move(CANVAS, vel_x=3, attached=True)
    elif key_press == 'a':
        pd.move_paddle(CANVAS, -3)
        if attached:
            ball.move(CANVAS, vel_x=-3, attached=True)
    if not attached:
        ball.move(CANVAS, bricks=BRICKS)
    if key_press == 'space' and attached is True:
        attached = False
        ball.move(CANVAS, vel_x=0, vel_y=-1, attached=True)

os.system("stty echo")
