# Letter Boxed Solver
This is an app that allows the user to input the New York Times Game Letter Boxed and will output the ideal solution. 

The game involves a box with 3 letters on each side. The goal of the game is to connect all 12 letters in as few words as possible, with the conditions that letters from the same side cannot be used consecutively and that the last letter of the prior word must be the first letter of the next word. Typically there exists a two word solution, however in some cases three words are necessary.

Using a cleaned and consolidated list of words, the app uses logic to find the ideal solution to the given problem, initially searching for one word solutions, then two word solutions, and then three word solutions. There is still optimizations that can be made to its run time, however it has been optimized somewhat already by shrinking the list of possible words. This was done in multiple ways: 
1) Remove words with consecutive double letters (ex: letter has two back to back t's)
2) Remove words with the same set of letters and same start and ends letters (ex: 
