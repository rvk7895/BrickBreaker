import colorama as cl
from colorama import Fore
import config as cfg
import os
from brick import Brick1, Brick2, Brick3, Brick4
from paddle import Paddle
from inputter import Input
from ball import Ball
from powerups import Paddle_Grow, Paddle_Shrink, Through_Ball, Fast_Ball
from powerups import Grab_Ball
import random
from time import time

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
start_time = time()
lives = 3
score = 0
space_counter = 0
game_over = False
game_won = False


def reset():
    global lives
    global pd
    global ball
    global attached
    global ACTIVE_POWERUPS

    lives -= 1

    for i in range(pd.length):
        CANVAS[pd.y][pd.x+i] = ' '

    pd = Paddle()
    ball = Ball()
    ACTIVE_POWERUPS = []
    for powerup in POWERUPS:
        powerup.ball = ball

    attached = True


def set_bricks():
    x_co = 1
    y_co = 1
    POWERUPS_AVAILABLE = [Paddle_Grow, Paddle_Shrink,
                          Through_Ball, Fast_Ball, Grab_Ball]

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

        if not (Brick is None):
            powerup = bool(random.getrandbits(1))
            powerup_class = random.choice(POWERUPS_AVAILABLE)
            obj = Brick(x_left=x_co, y=y_co)
            if (char == '1' or char == '2' or char == '3') and powerup:
                puobj = powerup_class(obj, ball)
                POWERUPS.append(puobj)

            BRICKS.append(obj)

        if(char == '\n'):
            x_co = 1
            y_co += 1

        x_co += cfg.BRICK_LENGTH


def check_game_over():
    global game_over
    if lives == 0:
        game_over = True


def check_game_win():
    global game_won
    game_won = True
    for brick in BRICKS:
        if brick.strength == 1 or brick.strength == 2 or brick.strength == 3:
            game_won = False


def set_powerups():
    for powerup in POWERUPS:
        powerup.display(CANVAS)


def print_bricks():
    for brick in BRICKS:
        brick.display(CANVAS)


def check_powerup_bricks():

    for powerup in POWERUPS:
        powerup.move(CANVAS)
        if powerup.picked_up(pd, CANVAS):
            ACTIVE_POWERUPS.append(powerup)
            POWERUPS.remove(powerup)
        if powerup.missed(CANVAS):
            POWERUPS.remove(powerup)

    for powerup in ACTIVE_POWERUPS:
        if powerup.over(pd, CANVAS):
            ACTIVE_POWERUPS.remove(powerup)


def check_ball_grab():
    global attached
    if ball.grab:
        if ball.y == pd.y-1 and ball.x >= pd.x \
                and ball.x < pd.x + pd.length:
            attached = True


def print_canvas():
    # PRINTING THE HEADER
    global idx
    idx = (idx + 1) % 7
    print(cfg.COLORS[idx] + cfg.HEADER + Fore.RESET)

    if not game_won and not game_over:
        print(cfg.LEFT_PADDING+'Score:'+str(score)+' '*40 +
              'Time:'+str(int(time())-int(start_time))
              + ' '*38+'Lives:'+"\u2764\ufe0f  "*lives)

        set_powerups()

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
            print('Press '+Fore.GREEN + 'spacebar' +
                  Fore.WHITE + ' to release ball' + Fore.RESET)

        print(Fore.WHITE + 'Press ' + Fore.GREEN + 'a' + Fore.WHITE + ' and ' +
              Fore.GREEN + 'd' + Fore.WHITE +
              ' to move left or right respectively'
              + Fore.RESET)
    if game_won:
        print(cfg.COLORS[idx] + cfg.GAME_WON + Fore.RESET)

    if game_over:
        print(cfg.COLORS[idx] + cfg.GAME_OVER + Fore.RESET)

    print(Fore.WHITE + 'Press ' + Fore.RED + 'q' +
          Fore.WHITE + ' to quit' + Fore.RESET)


# INITIALIZING THE CANVAS
CANVAS = [[' ']*cfg.WIDTH for _ in range(cfg.HEIGHT)]
BRICKS = []
POWERUPS = []
ACTIVE_POWERUPS = []

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
    score = ball.ball_brick_collision(bricks=BRICKS, canvas=CANVAS,
                                      powerups=POWERUPS, score=score)
    check_powerup_bricks()
    check_ball_grab()
    check_game_over()
    check_game_win()

    if ball.over(CANVAS):
        reset()

    pd.display(CANVAS)
    ball.display(CANVAS)

    print_canvas()

    # TAKING INPUT
    key_press = ip.get_parsed_input(timeout=0.07)
    if key_press == 'd':
        pd.move_paddle(CANVAS, 4)
        if attached:
            ball.move(CANVAS, vel_x=4, attached=True)
    elif key_press == 'a':
        pd.move_paddle(CANVAS, -4)
        if attached:
            ball.move(CANVAS, vel_x=-4, attached=True)
    if not attached:
        ball.move(CANVAS, bricks=BRICKS)
    if space_counter == 0:
        start_time = time()

    if key_press == 'space' and attached is True:
        paddle_middle = pd.x + int(pd.length/2)
        paddle_left_middle = pd.x + int(pd.length/2) - 1
        paddle_right_middle = pd.x + int(pd.length/2) + 1
        if ball.x >= paddle_left_middle or ball.x <= paddle_right_middle:
            vel_x = 0
        if ball.x < paddle_left_middle:
            vel_x = int((ball.x - paddle_middle - 1)/3) * ball.multi
        if ball.x > paddle_right_middle:
            vel_x = int((ball.x - paddle_middle + 1)/3) * ball.multi
        attached = False
        ball.move(CANVAS, vel_x=vel_x, vel_y=-1, attached=True)
        space_counter += 1

os.system("stty echo")
