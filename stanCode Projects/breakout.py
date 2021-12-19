"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.graphics.gobjects import GLabel
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    life = GLabel('Lives: ' + str(lives))
    life.font = '-20'
    graphics.window.add(life, 0, graphics.window.height)
    brick_number = graphics.brick_number
    # Add animation loop here!
    while lives > 0 and brick_number > 0:
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        # Hits the side walls and bounces
        if graphics.ball.x < 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
            graphics.set_dx(-dx)
        # Hits the ceiling and bounces
        if graphics.ball.y < 0:
            graphics.set_dy(-dy)
        # Loses life
        elif graphics.ball.y + graphics.ball.height > graphics.window.height:
            graphics.restart()
            lives -= 1
            life.text = ('Lives: ' + str(lives))
        else:
            for i in range(2):
                for j in range(2):
                    if graphics.hit_brick(graphics.ball.x + graphics.ball.width * i,
                                          graphics.ball.y + graphics.ball.height * j):
                        object_detected = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width * i,
                                                                        graphics.ball.y + graphics.ball.height * j)
                        if object_detected is not None:
                            # Hits the bricks
                            if object_detected is not graphics.paddle and object_detected is not life:
                                graphics.window.remove(object_detected)
                                brick_number -= 1
                                graphics.set_dy(-dy)
                                break
                            # Hits the paddle
                            elif object_detected is graphics.paddle and dy > 0:
                                graphics.set_dy(-dy)
                                break
        if lives <= 0:
            game_over = GLabel('Game Over.')
            game_over.font = '-40'
            graphics.window.add(game_over, graphics.window.width / 2 - game_over.width / 2,
                                graphics.window.height / 2 + game_over.height)
        pause(FRAME_RATE)
        if brick_number == 0:
            win = GLabel('You Win!')
            win.font = '-40'
            graphics.window.add(win, (graphics.window.width - win.width) / 2, (graphics.window.height + win.height) / 2)
            break


if __name__ == '__main__':
    main()
