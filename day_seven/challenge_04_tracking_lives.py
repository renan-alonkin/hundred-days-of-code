
#Step 4
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = ["_" for letter in chosen_word]

end_of_game = False
while(not end_of_game):

    guess = input("Guess a letter: ").lower()
    guessed_correctly = False
    for idx, letter in enumerate(chosen_word):
        if letter == guess:
            display[idx] = letter
            guessed_correctly = True
    
    if not guessed_correctly:
            lives -= 1
            if lives == 0:
                end_of_game = True
    
    elif not "_" in display:
        end_of_game = True
    
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(*display)
    print(stages[lives])

print("Game Over")