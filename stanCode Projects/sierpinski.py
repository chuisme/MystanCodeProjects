"""
File: sierpinski.py
Name: Elaine Chu
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This function draws a sierpinski triangle.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, the order to draw the sierpinski triangle
	:param length: int, the length of the sierpinski triangle
	:param upper_left_x: int, the x coordinate of the upper-left corner of the sierpinski triangle
	:param upper_left_y: int, the y coordinate of the upper-left corner of the sierpinski triangle
	:return: None
	"""
	if order == 1:
		line_a = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		line_b = GLine(upper_left_x, upper_left_y, upper_left_x + 0.5 * length, upper_left_y + 0.866 * length)
		line_c = GLine(upper_left_x + length, upper_left_y, upper_left_x + 0.5 * length, upper_left_y + 0.866 * length)
		window.add(line_a)
		window.add(line_b)
		window.add(line_c)
	else:
		sierpinski_triangle(order - 1, 0.5 * length, upper_left_x, upper_left_y)
		sierpinski_triangle(order - 1, 0.5 * length, upper_left_x + 0.5 * length, upper_left_y)
		sierpinski_triangle(order - 1, 0.5 * length, upper_left_x + 0.5 * 0.5 * length, upper_left_y + 0.866 * 0.5 * length)


if __name__ == '__main__':
	main()