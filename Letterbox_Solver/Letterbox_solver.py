'''
Samuel Baldwin
Letter Boxed Solver
'''

import pandas as pd
from itertools import permutations, combinations

CLEANED_WORDS = 'merged.txt'

def load_text_file(file):
    """Read words from a given text file into a list of strings"""
    words = pd.read_csv(file, header=None, dtype=str).squeeze('columns').astype(str).tolist()
    return words

def has_adjacent_letters_from_same_side(word, sides):
    for i in range(len(word) - 1):
        # Find the side each letter comes from
        letter1, letter2 = word[i], word[i+1]
        side1 = None
        side2 = None

        for idx, side in enumerate(sides):
            if letter1 in side.lower():
                side1 = idx
            if letter2 in side.lower():
                side2 = idx

        # If both letters are from the same side, return True (i.e., invalid)
        if side1 == side2:
            return True

    return False

def filter_words(word_list, sides):
    letters = ''.join(sides).lower()

    # First filter: Only keep words that are subsets of the letters
    filtered_words = [word for word in word_list if set(word).issubset(set(letters))]

    # Second filter: Ensure no adjacent letters come from the same side
    final_filtered_words = [word for word in filtered_words if not has_adjacent_letters_from_same_side(word, sides)]
    
    return final_filtered_words


# ONE WORD SOLUTIONS
def find_one_word_solutions(letters, word_list):
    filtered_list = [word for word in word_list if len(set(word)) == len(letters)]
    if len(filtered_list) == 0:
        return None
    else:
        return filtered_list 
    
# TWO WORD SOLUTIONS    
def filter_words_by_combinations(sides, letters, word_list):
    '''
    
    '''
    possible_combinations = []
    for side in sides:
        side = side.lower()
        possible_combinations.extend([''.join(combination)
                             for combination in permutations(side, 2)])
        for letter in side:
            possible_combinations.append(letter + letter)
    
    filtered_words = [word for word in word_list                   
                      if all(char in letters for char in word)]
    
    filtered_words = [word for word in filtered_words if not 
                    any(string in word for string in possible_combinations)]

    return filtered_words

def find_matching_word_pairs(letters, word_list):
    completion_words = []
    for word1, word2 in permutations(word_list, 2):
        combined_word = word1 + word2
        if set(letters) == set(combined_word):
            completion_words.append(word1 + " " + word2)
    
    return completion_words

def filter_pairs_by_letter_match(word_pairs):
    filtered_pairs = []
    for pair in word_pairs:
        first_word, second_word = pair.split()
        if first_word[0] == second_word[-1]:
            filtered_pairs.append(pair)
    
    cleaned_filtered_pairs = []
    for pair in word_pairs:
        first_word, second_word = pair.split()
        if first_word[0] == second_word[-1]:
            cleaned_filtered_pairs.append(second_word + " " + first_word)
    
    return cleaned_filtered_pairs     

def find_two_word_solutions(sides, letters, word_list):
    filtered_words = filter_words_by_combinations(sides, letters, word_list)
    word_pairs = find_matching_word_pairs(letters, filtered_words)
    arranged_pairs = filter_pairs_by_letter_match(word_pairs)
    two_word_solutions = sorted(arranged_pairs, key=lambda x: min(len(word) for word in x))
    if len(two_word_solutions) == 0:
        return None
    else:
        return two_word_solutions 

# THREE WORD SOLUTIONS
def find_connectable_word_triplets(word1, word2, word3):
    permutations_list = permutations([word1, word2, word3])
    for perm in permutations_list:
        if perm[0][-1] == perm[1][0] and perm[1][-1] == perm[2][0]:
            return perm[0] + ' ' + perm[1] + ' ' + perm[2]
    return None

def find_three_word_solutions(letters, possible_words):
    solutions = []
    for word1, word2, word3 in combinations(possible_words, 3):
        if len(solutions) > 20:
            break
        combined_word = word1 + word2 + word3
        if set(letters) == set(combined_word):
            connectable_permutation = find_connectable_word_triplets(word1, word2, word3)
            if connectable_permutation:
                print(connectable_permutation)
                solutions.append(connectable_permutation)
    return solutions


# Call functions from flask

def one_two_word_solutions(sides):
    cleaned_words = filter_words(load_text_file('merged.txt'), sides)
    letters = ''.join(sides).lower()

    one_word_solution = find_one_word_solutions(letters, cleaned_words)
    if one_word_solution:
        return one_word_solution

    two_word_solution = find_two_word_solutions(sides, letters, cleaned_words)
    if two_word_solution:
        return two_word_solution

    return []

def three_word_solutions(sides):
    cleaned_words = filter_words(load_text_file('merged.txt'), sides)
    print(len(cleaned_words))
    print("Done cleaning")
    letters = ''.join(sides).lower()

    three_word_solution = find_three_word_solutions(letters, cleaned_words)
    if three_word_solution:
        return three_word_solution

    return []
