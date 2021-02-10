from colorama import Fore, Back
import config as cfg

class Brick0:
    def __init__ (self):
        self.strength = 0

    def display(self, canvas, x, y):
        for i in range(cfg.BRICK_LENGTH):
            canvas[y][x+i] = ' '

class Brick1:
    def __init__ (self):
        self.strength = 1
        self.fore_color = Fore.WHITE
        self.back_color = Back.RED

    def display(self, canvas, x, y):
        canvas[y][x] = self.fore_color + self.back_color + '╔' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y][x+i] = self.back_color + self.fore_color + '═' + Back.RESET + Fore.RESET
        canvas[y][x+cfg.BRICK_LENGTH-1] = self.back_color + self.fore_color + '╗' + Back.RESET + Fore.RESET
        
        canvas[y+1][x] = self.fore_color + self.back_color + '║' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y+1][x+i] = self.back_color + self.fore_color + ' ' + Back.RESET + Fore.RESET
        canvas[y+1][x+cfg.BRICK_LENGTH-1] = self.fore_color + self.back_color + '║' + Back.RESET + Fore.RESET

        canvas[y+2][x] = self.fore_color + self.back_color + '╚' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y+2][x+i] = self.back_color + self.fore_color + '═' + Back.RESET + Fore.RESET
        canvas[y+2][x+cfg.BRICK_LENGTH-1] = self.back_color + self.fore_color + '╝' + Back.RESET + Fore.RESET


class Brick2:
    def __init__(self):
        self.strength = 2
        self.fore_color = Fore.WHITE
        self.back_color = Back.BLUE

    def display(self, canvas, x, y):
        canvas[y][x] = self.fore_color + self.back_color + '╔' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y][x+i] = self.back_color + self.fore_color + '═' + Back.RESET + Fore.RESET
        canvas[y][x+cfg.BRICK_LENGTH-1] = self.back_color + self.fore_color + '╗' + Back.RESET + Fore.RESET
        
        canvas[y+1][x] = self.fore_color + self.back_color + '║' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y+1][x+i] = self.back_color + self.fore_color + ' ' + Back.RESET + Fore.RESET
        canvas[y+1][x+cfg.BRICK_LENGTH-1] = self.fore_color + self.back_color + '║' + Back.RESET + Fore.RESET

        canvas[y+2][x] = self.fore_color + self.back_color + '╚' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y+2][x+i] = self.back_color + self.fore_color + '═' + Back.RESET + Fore.RESET
        canvas[y+2][x+cfg.BRICK_LENGTH-1] = self.back_color + self.fore_color + '╝' + Back.RESET + Fore.RESET

class Brick3:
    def __init__(self):
        self.strength = 3
        self.fore_color = Fore.WHITE
        self.back_color = Back.YELLOW

    def display(self, canvas, x, y):
        canvas[y][x] = self.fore_color + self.back_color + '╔' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y][x+i] = self.back_color + self.fore_color + '═' + Back.RESET + Fore.RESET
        canvas[y][x+cfg.BRICK_LENGTH-1] = self.back_color + self.fore_color + '╗' + Back.RESET + Fore.RESET
        
        canvas[y+1][x] = self.fore_color + self.back_color + '║' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y+1][x+i] = self.back_color + self.fore_color + ' ' + Back.RESET + Fore.RESET
        canvas[y+1][x+cfg.BRICK_LENGTH-1] = self.fore_color + self.back_color + '║' + Back.RESET + Fore.RESET

        canvas[y+2][x] = self.fore_color + self.back_color + '╚' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y+2][x+i] = self.back_color + self.fore_color + '═' + Back.RESET + Fore.RESET
        canvas[y+2][x+cfg.BRICK_LENGTH-1] = self.back_color + self.fore_color + '╝' + Back.RESET + Fore.RESET

class Brick4:
    def __init__(self):
        self.strength = 9999
        self.fore_color = Fore.WHITE
        self.back_color = Back.BLACK

    def display(self, canvas, x, y):
        canvas[y][x] = self.fore_color + self.back_color + '╔' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y][x+i] = self.back_color + self.fore_color + '═' + Back.RESET + Fore.RESET
        canvas[y][x+cfg.BRICK_LENGTH-1] = self.back_color + self.fore_color + '╗' + Back.RESET + Fore.RESET
        
        canvas[y+1][x] = self.fore_color + self.back_color + '║' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y+1][x+i] = self.back_color + self.fore_color + ' ' + Back.RESET + Fore.RESET
        canvas[y+1][x+cfg.BRICK_LENGTH-1] = self.fore_color + self.back_color + '║' + Back.RESET + Fore.RESET

        canvas[y+2][x] = self.fore_color + self.back_color + '╚' + Back.RESET + Fore.RESET
        for i in range(1,cfg.BRICK_LENGTH-1):
            canvas[y+2][x+i] = self.back_color + self.fore_color + '═' + Back.RESET + Fore.RESET
        canvas[y+2][x+cfg.BRICK_LENGTH-1] = self.back_color + self.fore_color + '╝' + Back.RESET + Fore.RESET