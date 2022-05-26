import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

#Write your code below this line 👇
users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
opponents_choice = random.randint(0, 2)

win_condition = "You lose"

if(users_choice == 0 and opponents_choice == 2):
    win_condition = "Rock wins against Sissors, you win!"

if(users_choice == 1 and opponents_choice == 0):
    win_condition = "Paper wins against Rock, you win!"

if(users_choice == 2 and opponents_choice == 1):
    win_condition = "Scissors wins against Paper, you win!"

if(users_choice == opponents_choice):
    win_condition = "It is a tie!"

print("You chose:\n")
print(choices[users_choice])

print("\nComputer chose:\n")
print(choices[opponents_choice])

print(f"\n{win_condition}\n--")