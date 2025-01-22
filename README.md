# Letter Boxed Solver
This is an app that allows the user to input the New York Times Game Letter Boxed and will output the ideal solution. 

The game involves a box with 3 letters on each side. The goal of the game is to connect all 12 letters in as few words as possible, with the conditions that letters from the same side cannot be used consecutively and that the last letter of the prior word must be the first letter of the next word. Typically there exists a two word solution, however in some cases three words are necessary.

Files:
Letterboxed_word_cleaner
Cleans and consolidates a list of words. Additionally deletes excess words that serve no purpose in the context of letter boxed to optimize the solving time using mulitple methods:
1) Remove words with consecutive double letters (ex: letter has two back to back t's)
2) Remove words with the same set of letters and same start and ends letters (ex: for lead and leaded, leaded is removed)

Letterboxed_solver
Takes the in the input and the cleaned words list and uses logic to find the answer. Initially searches for one word solution simply searching for words with the correct set of letters, that also meet the condition of no consecutive letters from the same side. 
Then searches for two word solutions by finding words are a subset of the set of letters and finds two words that add up to the set that have the same end and start letter.
If two word solution is not possible, does the same for three words, however this is avoided at all costs as it is slower.

App
Front end that takes in input letters and shows results.




