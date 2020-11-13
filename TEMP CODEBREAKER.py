from random import random
from random_word import RandomWords

def diff_gen(level):
    r = RandomWords()
    if level in range(0, 4):
        return e_diff
    elif level in range(5, 9):
        return m_diff
    elif level in range(10, 13):
        return h_diff


def player_input(diff_lev):
    mess = input("Enter a ",diff_level, "word.")
    return mess

def level_gen():
    return 3
