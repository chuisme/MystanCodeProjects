"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        paddle = GRect(paddle_width, paddle_height)
        paddle.filled = True
        self.paddle = paddle
        self.paddle_height = self.window.height - PADDLE_OFFSET
        self.window.add(paddle, (self.window.width - paddle.width) / 2, self.window.height - paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.original_x = self.window.width / 2 - ball_radius
        self.original_y = self.window.height / 2 - ball_radius
        self.window.add(self.ball, self.original_x, self.original_y)
        self.__dx = 0
        self.__dy = 0
        # Default initial velocity for the ball

        # Initialize our mouse listeners
        onmousemoved(self.paddle_moving)
        onmouseclicked(self.click)

        # Initialize variables
        self.count = 0
        self.brick_number = brick_rows * brick_cols
        color = 'black'

        # Draw bricks
        for i in range(0, brick_cols):
            for j in range(0, brick_rows):
                if j // 2 == 0:
                    color = 'red'
                elif j // 2 == 1:
                    color = 'orange'
                elif j // 2 == 2:
                    color = 'yellow'
                elif j // 2 == 3:
                    color = 'green'
                elif j // 2 == 4:
                    color = 'blue'
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color
                self.window.add(self.brick, x=i * (brick_width + brick_spacing), y=j * (brick_height + brick_spacing) +
                                                                              brick_offset)

    def paddle_moving(self, event):
        """
        This function has the paddle move with its center following the mouse.
        :param event: event
        :return: None
        """
        if self.paddle.width / 2 < event.x < self.window.width - self.paddle.width / 2:
            self.paddle.x = event.x - self.paddle.width / 2
        elif event.x < self.paddle.width / 2:  # To prevent the paddle from out-boarding the left side
            self.paddle.x = 0
        else:  # To prevent the paddle from out-boarding the right side
            self.paddle.x = self.window.width - self.paddle.width

    def click(self, event):
        """
        This function starts the animation.
        :param event: event
        :return: None
        """
        self.count = 1
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def hit_brick(self, x, y):
        """
        :param x: x-coordinate
        :param y: y-coordinate
        :return: Bool, whether there are objects collided.
        """
        maybe_object = self.window.get_object_at(x, y)
        if maybe_object is not None:
            return True
        else:
            return False

    def hit_paddle(self):
        """
        Detects whether the ball hits the paddle.
        :return: Bool, whether the ball hits the paddle.
        """
        maybe_object = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        if maybe_object == self.paddle:
            return True
        maybe_object = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if maybe_object is self.paddle:
            return True
        else:
            return False

    def restart(self):
        """
        This function resets the ball to its original position.
        :return: None
        """
        self.count = 0
        self.ball.x = self.original_x
        self.ball.y = self.original_y
        self.__dx = 0
        self.__dy = 0

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy


