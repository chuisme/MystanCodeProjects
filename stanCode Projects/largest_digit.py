"""
File: largest_digit.py
Name: Elaine Chu
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the number to find the largest digit
	:return: int, the largest digit
	"""
	if n > 0:
		return find_largest_helper(n, 0)
	else:
		return find_largest_helper(-n, 0)


def find_largest_helper(n, maximum):
	"""
	:param n: int, the number to find the largest digit
	:param maximum: int, the largest digit
	:return: int, the largest digit
	"""
	if n % 10 > maximum:
		maximum = n % 10
	if n / 10 == 0:
		return maximum
	else:
		return find_largest_helper(n // 10, maximum)


if __name__ == '__main__':
	main()
