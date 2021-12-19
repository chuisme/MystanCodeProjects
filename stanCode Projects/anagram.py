"""
File: anagram.py
Name: Elaine Chu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variables
dict_list = []  # A list to store words in the dictionary file
word = ''
anagram_list = []  # A list to store anagrams
count = 0


def main():
    """
    The user input a word, and this function helps finding its anagrams and counts how much time does the whole
    process take.
    """
    global anagram_list, count
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    start = time.time()
    read_dictionary()
    while True:
        input_word = input('Find anagrams for: ')
        if input_word == EXIT:
            break
        else:
            print('Searching ...')
            find_anagrams(input_word)
            print(count, 'anagrams', anagram_list)
    print('----------------------------------')
    end = time.time()
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global dict_list
    with open(FILE, 'r') as f:
        for data in f:
            dict_list += data.split()


def find_anagrams(s):
    """
    :param s: str, the string to find anagrams
    :return: None
    """
    global word, anagram_list, count
    if len(s) == 0:
        if word in dict_list and word not in anagram_list:
            print('Found: ', word)
            print('Searching ...')
            count += 1
            anagram_list.append(word)
    else:
        for i in range(len(s)):
            if has_prefix(word) is True:
                word += s[i]
                s_new = s[:i] + s[i + 1:]
                find_anagrams(s_new)
                word = word[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: str, a string to check if there are words start with sub_s
    :return: bool, whether there are words with prefix
    """
    for word in dict_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
