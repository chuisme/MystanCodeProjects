"""
File: bouncing_ball.py
Name: Elaine Chu
-------------------------
Let the ball bounces for 3 times without being interrupted by mouseclicks during movements.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 20
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py')
remaining_times = 3
ball = GOval(SIZE, SIZE)
moving = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global ball
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(start)


def start(mouse):
    global ball, remaining_times, moving
    vy = 0
    if remaining_times > 0:
        if not moving:
            moving = True
            while True:
                ball.move(VX, vy)
                vy += GRAVITY
                if ball.y + ball.height >= window.height:
                    vy = -vy
                    vy *= REDUCE
                if ball.x + ball.width >= window.width:
                    ball.x = START_X
                    ball.y = START_Y
                    break
                pause(DELAY)
            remaining_times -= 1
            moving = False


if __name__ == "__main__":
    main()
