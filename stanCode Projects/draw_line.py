"""
File: draw_line.py
Name: Elaine Chu
-------------------------
User can draw lines between mouseclicks.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

# Global Variables
window = GWindow(500, 500, title = 'Draw Line')
click = 0
dot_x = 0
dot_y = 0
dot = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global click, dot_x, dot_y, dot
    click += 1
    if click % 2 == 1:
        dot = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        dot.filled = False
        dot.color = 'black'
        dot_x = mouse.x - SIZE / 2
        dot_y = mouse.y - SIZE / 2
        window.add(dot)
    else:
        line = GLine(dot_x + SIZE / 2, dot_y + SIZE / 2, mouse.x, mouse.y)
        window.add(line)
        window.remove(dot)


if __name__ == "__main__":
    main()
