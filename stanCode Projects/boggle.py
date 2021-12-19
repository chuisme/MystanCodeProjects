"""
File: boggle.py
Name: Elaine Chu
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	d = read_dictionary()
	num_of_rows = 1
	row = []  # To store letters input by the user
	while num_of_rows <= 4:
		word_input = input(str(num_of_rows) + ' row of letters: ').lower().split()
		if len(word_input) != 4:
			# To make sure the user enters four letters in a row
			print('Illegal Input')
			return
		for i in range(0, 3):
			# To make sure the user enters four single letters separated by spaces
			if len(word_input[i]) != 1 or word_input[i].isalpha() is False:
				print('Illegal Input')
				return
		row.append(word_input)
		num_of_rows += 1
	start = time.time()
	# After the user enters four rows of letters, start to search for vocabularies
	if len(row) == 4:
		search_words(row, d)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def search_words(row, d):
	"""
	:param row: lst,  the letters input by the user
	:param d: dict, the dictionary
	"""
	words = []  # To store the words found
	for x in range(len(row[0])):
		for y in range(len(row)):
			word = ''
			row_copy = row
			word += row_copy[x][y]
			search_words_helper(row_copy, word, d, x, y, words)
	print('There are ', str(len(words)), ' words in total.')


def search_words_helper(row, word, d, x, y, words):
	"""
	:param row: lst, the letters input by the user
	:param word: str, the letters to combine into a vocabulary
	:param d: dict, the dictionary
	:param x: int, the index of the row
	:param y: int, the index of row[x]
	:param words: lst, the words found by the function
	:return: None
	"""
	# Search for the words longer than four letters
	if len(word) >= 4 and word in d[word[0]] and word not in words:
		if d[word[0]][d[word[0]].index(word) + 1].startswith(word):  # Words longer than 4 letters
			print(f'Found "{word}"')
			words.append(word)
			search_words_helper(row, word, d, x, y, words)
		else:
			print(f'Found "{word}"')
			words.append(word)
	else:
		for i in range(x - 1, x + 2, 1):  # Adjacent letters from top to bottom
			for j in range(y - 1, y + 2, 1):  # Adjacent letters from left to right side
				if i < 0 or j < 0 or i >= len(row[x]) or j >= len(row):  # The positions out of the searching range
					pass
				elif i == x and j == y:  # Letter repeated
					pass
				elif row[i][j] == '':  # Letter selected
					pass
				else:
					# Choose
					word += row[i][j]
					row[i][j] = ''
					pre_x = x
					pre_y = y
					x = i
					y = j
					# Explore
					if has_prefix(word, d):
						search_words_helper(row, word, d, x, y, words)
					# Un-choose
					row[x][y] = word[-1]
					word = word[:-1]
					x = pre_x
					y = pre_y


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	d = {}
	with open(FILE, 'r') as f:
		for data in f:
			if len(data) >= 4:
				if data[0] in d:
					d[data[0]].append(data.strip())
				else:
					d[data[0]] = [data.strip()]
	return d


def has_prefix(sub_s, d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in d[sub_s[0]]:
		if word.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
