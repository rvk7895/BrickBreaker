# Brick Breaker Game
By :\
Ritvik Aryan Kalra\
2019115002

## Objective
Objective of the game is to break all the breakable bricks. There are 4 types of bricks in the game:
* Red which require 1 collision to break
* Blue which require 2 collisions to break
* Yellow which require 3 collision to break
* Black which are unbreakable

The player has 3 lives. A life is lost when the paddle misses the ball and ball goes below the paddle. 

There are different powerups present, which are randomly placed in random bricks. Each powerup appears when a brick has been completely destroyed. After it appears it starts dropping and needs to fall over the paddle to activate the powerup. The powerups are as follows:
* G - Grows the paddle by 2 characters.
* S - Shrinks the paddle by 2 characters, minimum length is 3 characters.
* T - Through ball, passes through the bricks destroying them in the process. Can even break unbreakable bricks.
* F - Increases the speed multiplier of the ball by 1. Initially the ball multiplier is 1
* G - Gives the paddle ability to grab the ball. To launch the ball one has to press the `spacebar`.

Each powerup lasts for 10 seconds.

## Instructions
1. To launch the ball press `spacebar`
2. To move left and right press `a` or `d` respectively
3. To quit press `q`

## Additional Functionalities
User can create their own levels by editing the [Level_1.txt](Levels/Level_1.txt) file.
* 0 reprents a space
* 1 represetns a red brick
* 2 represents a blue brick
* 3 represents a yellow brick
* 4 represents a black brick

User can edit the width and height of the playing area by changing the values of `WIDTH` and `HEIGHT` in [`config.py`](config.py) respectively.