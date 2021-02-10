import numpy as np
import colorama as cl
from colorama import Fore, Back, Style
import config as cfg
import os
from time import sleep
from brick import Brick0, Brick1, Brick2, Brick3, Brick4

cl.init()
idx = 0
level = 1

def set_bricks():
    x_co = 1
    y_co = 1
    Brick = None
    bricks_array_row = 0
    bricks_array_col = 0

    for char in level_string:
        # print(char)
        if(char=='0'): Brick = Brick0
        if(char=='1'): Brick = Brick1
        if(char=='2'): Brick = Brick2
        if(char=='3'): Brick = Brick3
        if(char=='4'): Brick = Brick4

        if(Brick != None): 
            obj = Brick(x_top = x_co, y_top = y_co)
            obj.display(canvas = CANVAS, x = x_co, y = y_co)
            BRICKS[bricks_array_row][bricks_array_col] = obj
            bricks_array_col += 1
        
        if(char == '\n'): 
            x_co = 1
            y_co += 3
            bricks_array_col = 0
            bricks_array_row += 1

        x_co += cfg.BRICK_LENGTH

# INITIALIZING THE CANVAS
CANVAS = [[' ']*cfg.WIDTH for _ in range(cfg.HEIGHT)]
BRICKS = [[None]*35 for _ in range(9)]

# INITIALIZING THE FRAME IN CANVAS
CANVAS[0][0] = '╔'
CANVAS[0][cfg.WIDTH-1] = '╗'
CANVAS[cfg.HEIGHT-1][0] = '╚'
CANVAS[cfg.HEIGHT-1][cfg.WIDTH-1] = '╝'
for x in range(1,cfg.WIDTH-1):
    CANVAS[0][x] = '═'
    CANVAS[cfg.HEIGHT-1][x] = '═'
for x in range(1,cfg.HEIGHT-1):
    CANVAS[x][0] = '║'
    CANVAS[x][cfg.WIDTH-1] = '║'

# READ LEVEL
file = None
if (level == 1): file = open(r'./Levels/Level_1.txt', 'r')
if (level == 2): file = open(r'./Levels/Level_2.txt', 'r')
if (level == 3): file = open(r'./Levels/Level_3.txt', 'r') 
level_string = file.read();

while True:
    os.system('clear')

    set_bricks()
    
    # PRINTING THE HEADER
    print(cfg.COLORS[idx] + cfg.HEADER + Fore.RESET)
    idx = (idx + 1) % 7

    # PRINTING THE CANVAS
    for i in range(cfg.HEIGHT):
        print(cfg.LEFT_PADDING,end="")
        for j in range(cfg.WIDTH):
            print(CANVAS[i][j],end="")
        print()
    # print(level_string)
    # for i in range(9):
    #     for j in range(34):
    #         print(BRICKS[i][j])
    sleep(0.1)