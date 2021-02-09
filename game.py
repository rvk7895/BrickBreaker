import numpy as np
import colorama as cl
from colorama import Fore, Back, Style
import config as cfg
from art import tprint
import os
from time import sleep

cl.init()

# tprint(cfg.LEFT_PADDING + ' '*40 + 'Brick Breaker')
# # PRINTING THE FRAME
# print(cfg.LEFT_PADDING + '_'*cfg.WIDTH)
# for x in range(cfg.HEIGHT):
#     print(cfg.LEFT_PADDING+'|'+' '*(cfg.WIDTH-2)+'|')
# print(cfg.LEFT_PADDING+'_'*cfg.WIDTH)

while True:
    os.system('clear')
    tprint(cfg.LEFT_PADDING + ' '*40 + 'Brick Breaker')
    # PRINTING THE FRAME
    print(cfg.LEFT_PADDING + '_'*cfg.WIDTH)
    for x in range(cfg.HEIGHT):
        print(cfg.LEFT_PADDING+'|'+' '*(cfg.WIDTH-2)+'|')
    print(cfg.LEFT_PADDING+'_'*cfg.WIDTH)
    sleep(1)