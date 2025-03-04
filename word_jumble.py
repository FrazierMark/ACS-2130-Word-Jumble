import random
from collections import Counter

# Unscrambles 1 word at a time.

dictionary = open("/usr/share/dict/words", "r")
dictionary_list = [word.strip() for word in dictionary.readlines()]
dictionary.close()


def ask_for_jumble():
  jumble = input("Type in you word jumble please.")
  return jumble

def find_possible_len_words(letter_count_dict, scrambled_word_length):
    possible_words = []
    
    for word in dictionary_list:
        if len(word) == scrambled_word_length:  # Compare to actual word length
            possible_answer = dict(Counter(word))  # Letter frequency of dict word
            if possible_answer == letter_count_dict:
                possible_words.append(word)
    
    return possible_words


word_to_descramble = ask_for_jumble()
letter_count_dict = dict(Counter(word_to_descramble))  # Letter count of scrambled word

possible_words = find_possible_len_words(letter_count_dict, len(word_to_descramble))

print("Possible words:", possible_words)

