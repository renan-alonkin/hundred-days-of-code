from audioop import cross


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇

cross_road = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" ")
cross_road = cross_road.lower()

if(cross_road == "left"):
    lake = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to " + \
                 "wait for the boat. Type \"swim\" to swim across. ")
    lake = lake.lower()
    if(lake == "wait"):
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and " + \
            "one blue. Which colour do you choose? ")
        door = door.lower()
        if(door == "yellow" or door == "blue"):
            print("Ohhhh no, you've choose the only door full of monsters! unfortunately, that is a Game Over.")
        else:
            print("You choose the communist door. your treasure is sharing your life with others! You win!")
    else:
        print("It is the middle ages for god sake, you are using a full plate armor! you DEFINITELY can't float. You drawned, Game Over.")
else:
    print("You've been hit by a charette and now you are limping, you can't continue this jorney. I hope you have " + \
        "health ensurance man. Anyways. That is a Game Over for you :c")