from colorama import Fore
from pyfiglet import figlet_format

LEFT_PADDING = ' '*50
WIDTH = 107
HEIGHT = 30
COLORS = [Fore.RED,
          Fore.GREEN,
          Fore.YELLOW,
          Fore.BLUE,
          Fore.MAGENTA,
          Fore.CYAN,
          Fore.WHITE]

BRICK_LENGTH = 5

HEADER_TEXT = figlet_format("Brick Breaker")
GAME_OVER_TEXT = figlet_format("Game Over")
GAME_WON_TEXT = figlet_format("Game Won")

SPACES = ' '*72
HEADER = SPACES
for idx in range(len(HEADER_TEXT)):
    HEADER += HEADER_TEXT[idx]
    if(HEADER_TEXT[idx] == '\n'):
        HEADER += SPACES

GAME_OVER = SPACES + ' '*4
for idx in range(len(GAME_OVER_TEXT)):
    GAME_OVER += GAME_OVER_TEXT[idx]
    if(GAME_OVER_TEXT[idx] == '\n'):
        GAME_OVER += SPACES + ' '*4

GAME_WON = SPACES + ' '*4
for idx in range(len(GAME_WON_TEXT)):
    GAME_WON += GAME_WON_TEXT[idx]
    if(GAME_WON_TEXT[idx] == '\n'):
        GAME_WON += SPACES + ' '*4


PADDLE_Y = 25
PADDLE_X = 45
PADDLE_LENGTH = 9
