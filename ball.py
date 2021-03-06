from config import PADDLE_Y, PADDLE_X, PADDLE_LENGTH, WIDTH, BRICK_LENGTH, HEIGHT
from brick import Brick1, Brick2, Brick3, Brick4
import os


class Ball:
    def __init__(self):
        self.x = PADDLE_X + int(PADDLE_LENGTH / 2)
        self.y = PADDLE_Y - 1
        self.vel_x = 0
        self.vel_y = 0
        self.through_ball = False
        self.grab = False
        self.multi = 1

    def display(self, canvas):
        canvas[self.y][self.x] = "o"

    def move(self, canvas, vel_x=0, vel_y=0, attached=False, bricks=[]):
        canvas[self.y][self.x] = " "
        self.vel_x = vel_x if attached else self.vel_x
        self.vel_y = vel_y if attached else self.vel_y
        if self.x + self.vel_x < 1:
            self.x = 1 - self.vel_x
        if self.x + self.vel_x > WIDTH - 2:
            self.x = WIDTH - 2 - self.vel_x
        if self.y + self.vel_y < 1:
            self.y = 1
        if self.y > PADDLE_Y and self.x >= PADDLE_X and self.x <= PADDLE_Y - 1:
            self.y = PADDLE_Y - 1
        for brick in bricks:
            if (
                self.vel_y < 0
                and (brick.y < self.y and brick.y >= self.y + self.vel_y)
                and (self.x >= brick.x_left and self.x <= brick.x_right)
            ):
                self.y = brick.y + 1 - self.vel_y
            if (
                self.vel_y > 0
                and (brick.y > self.y and brick.y <= self.y + self.vel_y)
                and (self.x >= brick.x_left and self.x <= brick.x_right)
            ):
                self.y = brick.y - 1 - self.vel_y
            if (
                self.vel_x > 0
                and (self.y <= brick.y + 1 and self.y >= brick.y - 1)
                and (self.x < brick.x_left and self.x + self.vel_x >= brick.x_left)
            ):
                self.x = brick.x_left - 1 - self.vel_x
            if (
                self.vel_x < 0
                and (self.y <= brick.y + 1 and self.y >= brick.y - 1)
                and (self.x > brick.x_right and self.x + self.vel_x <= brick.x_right)
            ):
                self.x = brick.x_right + 1 - self.vel_x

        self.x += self.vel_x
        self.y += self.vel_y

    def ball_paddle_collision(self, paddle):
        paddle_middle = paddle.x + int(paddle.length / 2)
        paddle_left_middle = paddle.x + int(paddle.length / 2) - 1
        paddle_right_middle = paddle.x + int(paddle.length / 2) + 1

        if (
            self.y == PADDLE_Y - 1
            and self.vel_y > 0
            and self.x >= paddle.x
            and self.x < paddle.x + paddle.length
        ):
            if self.x >= paddle_left_middle or self.x <= paddle_right_middle:
                self.vel_x = 0
            if self.x < paddle_left_middle:
                self.vel_x = int((self.x - paddle_middle - 1) / 3) * self.multi
            if self.x > paddle_right_middle:
                self.vel_x = int((self.x - paddle_middle + 1) / 3) * self.multi
            self.vel_y = -self.vel_y
            os.system("aplay -q ./Sound_Assets/Metal\\ Hit\\ 1.wav -d 1 &")
            return True
        if self.y == PADDLE_Y:
            if (self.vel_x > 0 and self.x == paddle.x - 1) or (
                self.vel_x < 0 and self.x == paddle.x + PADDLE_LENGTH
            ):
                self.vel_x = -self.vel_x
                os.system("aplay -q ./Sound_Assets/Metal\\ Hit\\ 1.wav -d 1 &")
                return True

    def ball_wall_collision(self):
        if self.x == 1 or self.x == WIDTH - 2:
            self.vel_x = -self.vel_x
            os.system("aplay -q ./Sound_Assets/Metal\\ Hit\\ 2.wav -d 1 &")

        if self.y == 1:
            self.vel_y = -self.vel_y
            os.system("aplay -q ./Sound_Assets/Metal\\ Hit\\ 2.wav -d 1 &")

    def ball_brick_collision(self, bricks=[], canvas=[], powerups=[], score=0):
        the_brick = None
        collision = False
        for idx, brick in enumerate(bricks):
            if (
                (self.y == brick.y + 1 and self.vel_y < 0)
                or (self.y == brick.y - 1 and self.vel_y > 0)
            ) and (self.x >= brick.x_left and self.x <= brick.x_right):
                if not self.through_ball:
                    self.vel_y = -self.vel_y
                collision = True

            if (
                (self.x == brick.x_left - 1 and self.vel_x > 0)
                or (self.x == brick.x_right + 1 and self.vel_x < 0)
            ) and (self.y <= brick.y + 1 and self.y >= brick.y - 1):
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
                score += 10 * the_brick.strength
                for i in range(BRICK_LENGTH):
                    canvas[the_brick.y][the_brick.x_left + i] = " "
            else:
                if the_brick.strength == 1:
                    os.system("aplay -q ./Sound_Assets/Metal\\ Hit\\ 3.wav -d 1 &")
                    score += 10
                    for i in range(BRICK_LENGTH):
                        canvas[the_brick.y][the_brick.x_left + i] = " "
                    for powerup in powerups:
                        if powerup.brick is the_brick:
                            powerup.activated = True
                            powerup.x_vel = self.vel_x
                if the_brick.strength == 2:
                    os.system("aplay -q ./Sound_Assets/Metal\\ Hit\\ 4.wav -d 1 &")
                    score += 10
                    obj = Brick1(the_brick.x_left, the_brick.y)
                    for powerup in powerups:
                        if powerup.brick is the_brick:
                            powerup.brick = obj
                if the_brick.strength == 3:
                    os.system("aplay -q ./Sound_Assets/Metal\\ Hit\\ 5.wav -d 1 &")
                    score += 10
                    obj = Brick2(the_brick.x_left, the_brick.y)
                    for powerup in powerups:
                        if powerup.brick is the_brick:
                            powerup.brick = obj
                if the_brick.strength > 3:
                    obj = Brick4(the_brick.x_left, the_brick.y)

            if not (obj is None):
                bricks.append(obj)
        return score

    def over(self, canvas):
        if self.y == HEIGHT - 2:
            canvas[self.y][self.x] = " "
            return True
        return False
