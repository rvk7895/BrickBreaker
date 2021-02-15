from colorama import Fore
from config import WIDTH

class Paddle:
    def __init__(self):
        self.length = 8
        self.color = Fore.WHITE
        self.x = 85
        self.y = 40

    def display(self, canvas):
        for i in range(self.length):
            canvas[self.y][self.x+i] = self.color + '█' + Fore.RESET

    def move_paddle(self, canvas, dir):
        if(dir == -1 and self.x == 1): 
            pass
        elif(dir == 1 and self.x + self.length == WIDTH-2): 
            pass
        else: 
            for i in range(self.length):
                canvas[self.y][self.x+i] = ' '
            self.x += dir