#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters 
# in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

display = ["_" for letter in chosen_word]

while("_" in display):

    guess = input("Guess a letter: ").lower()

    for idx, letter in enumerate(chosen_word):
        if letter == guess:
            display[idx] = letter

    print(*display)
    
print("You Won!")