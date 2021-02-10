import numpy as np
import colorama as cl
from colorama import Fore, Back, Style
import config as cfg
import os
from time import sleep

cl.init()
idx = 0

# INITIALIZING THE CANVAS
CANVAS = [[' ']*cfg.WIDTH for _ in range(cfg.HEIGHT)]

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

while True:
    os.system('clear')
    
    # PRINTING THE HEADER
    print(cfg.COLORS[idx] + cfg.HEADER + Fore.RESET)
    idx = (idx + 1) % 7

    # PRINTING THE CANVAS
    for i in range(cfg.HEIGHT):
        print(cfg.LEFT_PADDING,end="")
        for j in range(cfg.WIDTH):
            print(CANVAS[i][j],end="")
        print()
    sleep(0.1)