#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

random_letters = ""
for letter_n in range(1, nr_letters + 1):
    random_letters += letters[random.randint(0, len(letters) - 1)]
    # random_letters += random.choice(letters)

random_numbers = ""
for number_n in range(1, nr_numbers + 1):
    random_numbers += numbers[random.randint(0, len(numbers) - 1)]
    # random_number += random.choice(numbers)

random_symbols = ""
for symbol_n in range(1, nr_symbols + 1):
    random_symbols += symbols[random.randint(0, len(symbols) - 1)]
    # random_symbol += random.choice(symbols)

easy_password = random_letters + random_symbols + random_numbers
print(f"Result of easy password: {easy_password}")
print("\n --------------------------- \n")

#Medium Level - Order of characters randomised, but using a function:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
medium_password = ''.join(random.sample(easy_password, len(easy_password)))
print(f"Result of medium password: {medium_password}")
print("\n --------------------------- \n")


#Hard Level - Order of characters randomised on the fly:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_characters = nr_letters + nr_numbers + nr_symbols
types_of_characters = ["letter", "symbol", "number"]

hard_password = ""
for character in range(1, (total_characters + 1)):
    selected_type = random.choice(types_of_characters)
    selected_character = ""
    match selected_type:
        case "letter":
            selected_character = letters[random.randint(0, len(letters) - 1)]
            nr_letters -= 1
            if nr_letters == 0:
                types_of_characters.remove("letter")
        case "number":
            selected_character = numbers[random.randint(0, len(numbers) - 1)]
            nr_numbers -= 1
            if nr_numbers == 0:
                types_of_characters.remove("number")
        case "symbol":
            selected_character = symbols[random.randint(0, len(symbols) - 1)]
            nr_symbols -= 1
            if nr_symbols == 0:
                types_of_characters.remove("symbol")
    
    print(f"Selected character: {selected_character} | Selected Type: {selected_type}")
    hard_password += selected_character

print(hard_password)
