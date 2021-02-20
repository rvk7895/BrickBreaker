from config import PADDLE_Y, PADDLE_X, PADDLE_LENGTH, WIDTH, BRICK_LENGTH
from brick import Brick1, Brick2, Brick3, Brick4


class Ball:
    def __init__(self):
        self.x = PADDLE_X + int(PADDLE_LENGTH/2)
        self.y = PADDLE_Y - 1
        self.vel_x = 0
        self.vel_y = 0
        self.through_ball = False
        self.grab = False
        self.multi = 1

    def display(self, canvas):
        canvas[self.y][self.x] = 'o'

    def move(self, canvas, vel_x=0, vel_y=0, attached=False, bricks=[]):
        canvas[self.y][self.x] = ' '
        self.vel_x = vel_x if attached else self.vel_x
        self.vel_y = vel_y if attached else self.vel_y
        if self.x + self.vel_x < 1:
            self.x = 1 - self.vel_x
        if self.x + self.vel_x > WIDTH - 2:
            self.x = WIDTH - 2 - self.vel_x
        if self.y + self.vel_y < 1:
            self.y = 1
        if self.y > PADDLE_Y and self.x >= PADDLE_X and self.x <= PADDLE_Y-1:
            self.y = PADDLE_Y-1
        for brick in bricks:
            if self.vel_y < 0 and\
               (brick.y < self.y and brick.y >= self.y + self.vel_y) and \
                    (self.x >= brick.x_left and self.x <= brick.x_right):
                self.y = brick.y + 1 - self.vel_y
            if self.vel_y > 0 and\
                (brick.y > self.y and brick.y <= self.y + self.vel_y) and \
                    (self.x >= brick.x_left and self.x <= brick.x_right):
                self.y = brick.y-1 - self.vel_y
            if self.vel_x > 0 and\
                (self.y <= brick.y + 1 and self.y >= brick.y - 1) and \
                    (self.x < brick.x_left and
                     self.x + self.vel_x >= brick.x_left):
                self.x = brick.x_left - 1 - self.vel_x
            if self.vel_x < 0 and\
                (self.y <= brick.y + 1 and self.y    >= brick.y - 1) and \
                    (self.x > brick.x_right and
                     self.x + self.vel_x <= brick.x_right):
                self.x = brick.x_right + 1 - self.vel_x

        self.x += self.vel_x
        self.y += self.vel_y

    def ball_paddle_collision(self, paddle):
        paddle_middle = paddle.x + int(paddle.length/2)
        paddle_left_middle = paddle.x + int(paddle.length/2) - 1
        paddle_right_middle = paddle.x + int(paddle.length/2) + 1
        if self.y == PADDLE_Y-1 and self.vel_y > 0 and self.x >= paddle.x \
                and self.x < paddle.x + paddle.length:
            if self.x >= paddle_left_middle or self.x <= paddle_right_middle:
                self.vel_x = 0
            if self.x < paddle_left_middle:
                self.vel_x = int((self.x - paddle_middle - 1)/4) * self.multi
            if self.x > paddle_right_middle:
                self.vel_x = int((self.x - paddle_middle + 1)/4) * self.multi
            self.vel_y = -self.vel_y
        if self.y == PADDLE_Y:
            if (self.vel_x > 0 and self.x == paddle.x - 1) or\
                    (self.vel_x < 0 and self.x == paddle.x + PADDLE_LENGTH):
                self.vel_x = -self.vel_x

    def ball_wall_collision(self):
        if self.x == 1 or self.x == WIDTH - 2:
            self.vel_x = -self.vel_x
        if self.y == 1:
            self.vel_y = -self.vel_y

    def ball_brick_collision(self, bricks=[], canvas=[], powerups=[]):
        the_brick = None
        collision = False
        for idx, brick in enumerate(bricks):
            if (self.y == brick.y + 1 or self.y == brick.y - 1) and \
                    (self.x >= brick.x_left and self.x <= brick.x_right):
                if not self.through_ball:
                    self.vel_y = -self.vel_y
                collision = True

            if(self.x == brick.x_left - 1 or self.x == brick.x_right + 1) and \
                    (self.y <= brick.y + 1 and self.y >= brick.y - 1):
                if not self.through_ball:
                    self.vel_x = -self.vel_x
                collision = True

            if collision:
                the_brick = brick
                break

        obj = None
        if collision:
            bricks.remove(the_brick)
            if self.through_ball:
                for i in range(BRICK_LENGTH):
                    canvas[the_brick.y][the_brick.x_left + i] = ' '
            else:
                if the_brick.strength == 1:
                    for i in range(BRICK_LENGTH):
                        canvas[the_brick.y][the_brick.x_left + i] = ' '
                    for powerup in powerups:
                        if powerup.brick is the_brick:
                            powerup.activated = True
                if the_brick.strength == 2:
                    obj = Brick1(the_brick.x_left, the_brick.y)
                    for powerup in powerups:
                        if powerup.brick is the_brick:
                            powerup.brick = obj
                if the_brick.strength == 3:
                    obj = Brick2(the_brick.x_left, the_brick.y)
                    for powerup in powerups:
                        if powerup.brick is the_brick:
                            powerup.brick = obj
                if the_brick.strength > 3:
                    obj = Brick4(the_brick.x_left, the_brick.y)

            if not (obj is None):
                bricks.append(obj)
