
#Step 5
import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

from hangman_words import word_list

#TODO-2: - Import the stages from hangman_art.py and make this error go away.
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

from hangman_art import logo, stages
print(logo)

#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
guessed_letters = []

#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

chosen_word = random.choice(word_list)

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = ["_" for letter in chosen_word]

end_game_condition = ""
end_of_game = False

while(not end_of_game):

    guess = input("Guess a letter: ").lower()
    
    if(guess in guessed_letters):
      print("This letter has already been guessed")
    else:
      guessed_letters.append(guess)
      guessed_correctly = False
      
      for idx, letter in enumerate(chosen_word):
          if letter == guess:
              display[idx] = letter
              guessed_correctly = True
      
      if not guessed_correctly:
        lives -= 1
        print("Sorry, this letter doesn't exist in the secret word.")
        
        if lives == 0:
            end_of_game = True
            end_game_condition = "lose"
      
      elif not "_" in display:
          end_of_game = True
          end_game_condition = "win"
    
    print(*display)
    print(stages[lives])

print(f"Game Over, you {end_game_condition.upper()}!")