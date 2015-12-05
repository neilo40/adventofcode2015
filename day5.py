from collections import deque
from itertools import izip


with open("inputs/day5.txt", 'r') as fh:
    words = fh.readlines()


def is_nice_part1(word):
    return has_three_vowels(word) and has_double_letter(word) and has_no_forbidden_strings(word)


def has_three_vowels(word):
    vowels = "aeiou"
    vowels_in_word = [l for l in word if l in vowels]
    return len(vowels_in_word) >= 3


def has_double_letter(word):
    letters = deque(word)
    while(letters):
        try:
            if letters[0] == letters[1]:
                return True
        except IndexError:
            return False  # End of Deque
        letters.popleft()


def has_no_forbidden_strings(word):
    forbidden_strings = ["ab", "cd", "pq", "xy"]
    for forbidden_string in forbidden_strings:
        if forbidden_string in word:
            return False
    return True


def is_nice_part2(word):
    return has_two_unique_pairs(word) and has_repeating_letter(word)


def has_two_unique_pairs(word):
    pairs = [p[0] + p[1] for p in izip(word, word[1:])]
    for pair in pairs:
        if word.count(pair) >= 2:
            return True
    return False


def has_repeating_letter(word):
    letters = deque(word)
    while(letters):
        try:
            if letters[0] == letters[2]:
                return True
        except IndexError:
            return False  # End of Deque
        letters.popleft()


nice_words = 0 
for word in words:
    if is_nice_part2(word):
        nice_words += 1


print nice_words
