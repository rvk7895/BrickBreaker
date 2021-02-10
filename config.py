from colorama import Fore
from pyfiglet import figlet_format

LEFT_PADDING = ' '*15
WIDTH = 182
HEIGHT = 45
COLORS = [Fore.RED, 
        Fore.GREEN, 
        Fore.YELLOW, 
        Fore.BLUE, 
        Fore.MAGENTA, 
        Fore.CYAN, 
        Fore.WHITE]

BRICK_LENGTH = 5

HEADER_TEXT = figlet_format("Brick Breaker")
SPACES = ' '*77
HEADER = SPACES
for idx in range(len(HEADER_TEXT)):
    HEADER += HEADER_TEXT[idx]
    if(HEADER_TEXT[idx] == '\n'):
        HEADER += SPACES
