from colorama import Fore, Back
import config as cfg


class Brick:
    def __init__(self, x_left, y):
        self.x_left = x_left
        self.y = y
        self.x_right = x_left + cfg.BRICK_LENGTH-1

class Brick1(Brick):
    def __init__(self, x_left, y):
        super().__init__(x_left, y)
        self.strength = 1
        self.fore_color = Fore.RED

    def display(self, canvas):
        for i in range(cfg.BRICK_LENGTH):
            canvas[self.y][self.x_left+i] = self.fore_color + '█' + Fore.RESET


class Brick2(Brick):
    def __init__(self, x_left, y):
        super().__init__(x_left, y)
        self.strength = 2
        self.fore_color = Fore.BLUE

    def display(self, canvas):
        for i in range(cfg.BRICK_LENGTH):
            canvas[self.y][self.x_left+i] = self.fore_color + '█' + Fore.RESET


class Brick3(Brick):
    def __init__(self, x_left, y):
        super().__init__(x_left, y)
        self.strength = 3
        self.fore_color = Fore.YELLOW

    def display(self, canvas):
        for i in range(cfg.BRICK_LENGTH):
            canvas[self.y][self.x_left+i] = self.fore_color + '█' + Fore.RESET


class Brick4(Brick):
    def __init__(self, x_left, y):
        super().__init__(x_left, y)
        self.strength = 9999
        self.fore_color = Fore.BLACK

    def display(self, canvas):
        for i in range(cfg.BRICK_LENGTH):
            canvas[self.y][self.x_left+i] = self.fore_color + '█' + Fore.RESET
