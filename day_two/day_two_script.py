# Data Types

# String
# Subscripting (getting the element)
print("Hello"[0])
print("Hello"[-1:])

print("123" + "345")

# Integer
print(123 + 345)
# Using "commas" (better visualization)
print(123_456_789)

#Float
3.14159

#Boolean
True
False

# Errors
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")

# Mathematical operations
3 + 5
7 - 4
3 * 2
# Divisions always return in float
6 / 3
2 ** 2

# PEMDAS LR (Left to Right)
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

# Number manipulation and F Strings
print(round(8 / 3))
print(round(8 / 3, 2))

# Integer division / Floor division 
print (8 // 2) 

result = 4 / 2 
result /= 2
print (result)

score = 0
# User scores a point
score = score + 1
score += 1 # Alternatively

# F Strings
height = 1.8
is_winning = True
print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")