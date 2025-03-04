import random

dictionary = open("/usr/share/dict/words", "r")
dictionary_list = [word.strip() for word in dictionary.readlines()]
dictionary.close()


def word_to_dict(word_to_descramble):
  letters_to_num_letters = {}
  
  # create the dict: letter (key) to quantity (value): {'t': 3, 'r': 1}
  for letter in word_to_descramble:
    letter_count = letters_to_num_letters.get(letter, 0)
    letter_count += 1
    letters_to_num_letters[letter] = letter_count
    
  return letters_to_num_letters

def ask_for_jumble():
  jumble = input("Type in you word jumble please: \n")
  return jumble

def find_possible_len_words(letter_count_dict, scrambled_word_length):
    possible_words = []
    
    for word in dictionary_list:
        if len(word) == scrambled_word_length:
            possible_answer = dict(word_to_dict(word))
            if possible_answer == letter_count_dict:
                possible_words.append(word)
    
    return possible_words

def ask_for_number_of_words():
    num_words = int(input("How many words would you like to descramble? "))
    return num_words

num_words = ask_for_number_of_words()
all_possible_words = []  # List to store possible words for all scrambled inputs

for _ in range(num_words):
    word_to_descramble = ask_for_jumble()
    letter_count_dict = dict(word_to_dict(word_to_descramble))
    possible_words = find_possible_len_words(letter_count_dict, len(word_to_descramble))  # Find possible words
    all_possible_words.append(possible_words)

print("Possible words for each input:", all_possible_words)


