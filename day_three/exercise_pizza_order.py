# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

# Standardizing inputs.
size = size.lower()
add_pepperoni = add_pepperoni.lower()
extra_cheese = extra_cheese.lower()

# If it has extra cheese, +1 to bill
bill += 1 if extra_cheese == "y" else 0

# If add_peperoni is true, add bill accordingly to the size.
if(add_pepperoni == "y"):
    bill += 2 if size == "s" else 3

# Then add to bill the base price of each size.
if(size == "s"):
    bill += 15
if(size == "m"):
    bill += 20
if(size == "l"):
    bill += 25

print(f"Your final bill is: ${bill}")