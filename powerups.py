from config import HEIGHT
from time import perf_counter, time


class Powerups:
    def __init__(self, brick, ball):
        self.x = int((brick.x_left + brick.x_right)/2)
        self.y = brick.y
        self.brick = brick
        self.activated = False
        self.ball = ball
        self.start_time = time()
        self.time_limit = 10

    def move(self, canvas):
        if self.activated:
            canvas[self.y][self.x] = ' '
            self.y += 1

    def missed(self, canvas):
        if self.y == HEIGHT-2:
            canvas[self.y][self.y] = ' '
            return True
        return False
        # def check_brick(self, bricks):
        #     present = False
        #     for brick in bricks:
        #         if brick is self.brick:
        #             present = True

        #     if not present:
        #         self.activated = True


class Paddle_Grow(Powerups):
    def __init__(self, brick, ball):
        super().__init__(brick, ball)
        self.char = 'G'

    def display(self, canvas):
        if self.activated:
            canvas[self.y][self.x] = self.char

    def picked_up(self, paddle, canvas):
        if self.y == paddle.y-1 and \
                (self.x >= paddle.x and self.x < paddle.x + paddle.length):
            paddle.length += 2
            self.activated = False
            self.start_time = time()
            return True
        return False

    def over(self, paddle, canvas):
        if time() - self.start_time > self.time_limit:
            for i in range(paddle.length):
                canvas[paddle.y][paddle.x + i] = ' '
            paddle.length -= 2
            return True
        return False


class Paddle_Shrink(Powerups):
    def __init__(self, brick, ball):
        super().__init__(brick, ball)
        self.char = 'S'

    def display(self, canvas):
        if self.activated:
            canvas[self.y][self.x] = self.char

    def picked_up(self, paddle, canvas):
        if self.y == paddle.y-1 and \
                (self.x >= paddle.x and self.x < paddle.x + paddle.length):
            for i in range(paddle.length):
                canvas[paddle.y][paddle.x + i] = ' '
                paddle.length -= 2
            self.activated = False
            return True
        return False

    def over(self, paddle, canvas):
        if time() - self.start_time > self.time_limit:
            for i in range(paddle.length):
                canvas[paddle.y][paddle.x + i] = ' '
            paddle.length += 2
            return True
        return False


class Through_Ball(Powerups):
    def __init__(self, brick, ball):
        super().__init__(brick, ball)
        self.char = 'T'

    def display(self, canvas):
        if self.activated:
            canvas[self.y][self.x] = self.char

    def picked_up(self, paddle, canvas):
        if self.y == paddle.y-1 and \
                (self.x >= paddle.x and self.x < paddle.x + paddle.length):
            self.ball.through_ball = True
            self.activated = False
            return True
        return False

    def over(self, paddle, canvas):
        if time() - self.start_time > self.time_limit:
            self.ball.through_ball = False
            return True
        return False


class Fast_Ball(Powerups):
    def __init__(self, brick, ball):
        super().__init__(brick, ball)
        self.char = 'F'

    def display(self, canvas):
        if self.activated:
            canvas[self.y][self.x] = self.char

    def picked_up(self, paddle, canvas):
        if self.y == paddle.y-1 and \
                (self.x >= paddle.x and self.x < paddle.x + paddle.length):
            self.ball.multi += 1
            self.activated = False
            return True
        return False

    def over(self, paddle, canvas):
        if time() - self.start_time > self.time_limit:
            self.ball.multi -= 1
            return True
        return False


class Grab_Ball(Powerups):
    def __init__(self, brick, ball):
        super().__init__(brick, ball)
        self.char = 'G'

    def display(self, canvas):
        if self.activated:
            canvas[self.y][self.x] = self.char

    def picked_up(self, paddle, canvas):
        if self.y == paddle.y-1 and \
                (self.x >= paddle.x and self.x < paddle.x + paddle.length):
            self.ball.grab = True
            self.ball.vel_y = 0
            self.activated = False
            return True
        return False

    def over(self, paddle, canvas):
        if time() - self.start_time > self.time_limit:
            self.ball.grab = False
            return True
        return False
