import sys
import os
import pickle
from collections import OrderedDict
from random import randrange
from pprint import pprint
import data

found_letters = []

def select_word():
    words_length = len(data.words)
    random_index = randrange(words_length)
    return data.words[random_index]

def display_word(word):
    displayed_word = []
    for letter in word:
        if is_found_letter(letter=letter):
            displayed_char = letter
        else:
            displayed_char = "*"
        displayed_word.append(displayed_char)
    pprint("".join(displayed_word))

def is_found_letter(letter):
    global found_letters
    return True if letter in found_letters else False

def check_endgame(word):
    global found_letters
    for letter in word:
        if letter not in found_letters:
            return False
    return True

def get_user_input():
    new_letter = ''
    while new_letter == '':
        new_letter = input("Please enter a letter : ")
    return new_letter

def check_letter(letter, word):
    global found_letters
    if letter in word:
        found_letters.append(letter)
        unique_list = set(found_letters)
        found_letters = list(unique_list)
        return True
    return False

def check_lives():
    return True if data.lives > 0 else False

def run_game():
    pprint("Welcome to the Hangman game !")
    gamer_name = input("\n What is your name ? ")
    dict_score = init_score(gamer_name=gamer_name)
    word_to_find = select_word()

    while not check_endgame(word_to_find) and check_lives():
        display_word(word=word_to_find)
        letter = get_user_input()
        if not check_letter(letter=letter, word=word_to_find):
            data.lives -= 1
            pprint(f"Letter {letter} not in word")
            pprint(f"Lives remaining : {data.lives}")
    # End game, score
    if not check_lives():
        pprint("You lose ! Retry when you want")
    elif check_endgame(word_to_find):
        pprint("You win !! Congratulations")
        # dict_score[gamer_name] = data.lives
        if save_score(dict_score=dict_score, name=gamer_name, score=data.lives):
            pprint("Score saved !")
            pprint(dict_score)

def init_score(gamer_name):
    '''Initialize score

    Args:
        gamer_name (string): user name

    Returns:
        dict: dictionnary containing score
    '''
    try:
        with open('score', 'rb') as fp:
            score_pickler = pickle.Unpickler(fp)
            score_dict = score_pickler.load()
            return score_dict
    except FileNotFoundError:
        score_dict = {gamer_name: 0}
        with open('score', 'wb') as fp:
            score_pickler = pickle.Pickler(fp)
            score_pickler.dump(score_dict)
            return score_dict

def save_score(dict_score, name, score):
    if dict_score:
        dict_score[name] = score
    try:
        with open('score', 'wb') as fp:
            score_pickler = pickle.Pickler(fp)
            score_pickler.dump(dict_score)
            return True
    except Exception as e:
        pprint(e)

if __name__ == "__main__":
    run_game()

# todo : sort score dict by score desc
