from colorama import Fore
from config import WIDTH
from config import PADDLE_Y, PADDLE_X, PADDLE_LENGTH


class Paddle:
    def __init__(self):
        self.length = PADDLE_LENGTH
        self.color = Fore.WHITE
        self.x = PADDLE_X
        self.y = PADDLE_Y

    def display(self, canvas):
        for i in range(self.length):
            canvas[self.y][self.x+i] = self.color + '█' + Fore.RESET

    def move_paddle(self, canvas, dir):
        for i in range(self.length):
            canvas[self.y][self.x+i] = ' '

        if dir == -3 and self.x <= 4 :
            self.x = 1
        elif dir == 3 and self.x + self.length >= WIDTH - 5 :
            self.x = WIDTH - 1 - self.length
        else:
            self.x += dir
