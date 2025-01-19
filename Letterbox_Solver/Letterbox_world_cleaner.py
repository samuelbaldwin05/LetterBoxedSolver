"""
Samuel Baldwin
Clean words file for letter boxed
"""
import pandas as pd

WORDS = 'uncleaned_words.txt'

def load_text_file(file):
    '''
    From a given text file, open the file
    read the words in the file into a list
    '''
    words = pd.read_csv(file, header=None, dtype=str).squeeze('columns').astype(str).tolist()
    return words

def process_word_list(words):
    '''
    From a list of all words, edit the list to only
    contain words that work with the letterboxed game,
    contain at least one vowel, are not 1 or 2 letters long,
    and do not have unwanted characters or consecutive duplicates.
    Also, words with the same set of letters, starting and ending with the same letters, 
    will only keep the shorter word.
    '''
    specific_characters = "0123456789-.&///-+-"
    vowels = "aeiou"
    
    filtered_words = []
    seen_words = {}  # Dictionary to track words by their letter set and start/end characters
    
    for word in words:
        word = word.lower()  # Convert to lowercase
        
        # Check for unwanted characters
        if any(char in word for char in specific_characters):
            continue
        
        # Remove apostrophes
        word = word.replace("'", "")
        
        # Check for consecutive duplicates
        if any(word[i] == word[i - 1] for i in range(1, len(word))):
            continue
        
        # Check for vowels and length of word
        if len(word) > 2 and any(vowel in word for vowel in vowels):
            # Create a signature: set of letters, first letter, and last letter
            letter_set = frozenset(word)  # Use frozenset to ignore order of letters
            start_end_tuple = (word[0], word[-1])
            
            # Check if this word's set of letters and start/end match another word
            if letter_set not in seen_words:
                seen_words[letter_set] = (word, start_end_tuple)
                filtered_words.append(word)
            else:
                existing_word, existing_start_end = seen_words[letter_set]
                # If both words have the same start and end, keep the shorter one
                if existing_start_end == start_end_tuple:
                    if len(word) < len(existing_word):
                        # Replace the longer word with the shorter one
                        filtered_words.remove(existing_word)
                        filtered_words.append(word)
                        seen_words[letter_set] = (word, start_end_tuple)
                else:
                    filtered_words.append(word)
                    seen_words[letter_set] = (word, start_end_tuple)
    
    return filtered_words

def create_file(words_list, file_name):
        with open(file_name, "w") as file:
            for word in words_list:
                file.write(word + "\n")

def main():
    words1 = load_text_file('output.txt')
    words2 = load_text_file('output2.txt')
    merged = list(set(words1) & set(words2))
    create_file(merged, "merged.txt")

if __name__ == "__main__":
    main()
