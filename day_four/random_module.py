import random
import my_module

print("\n----Using a personal module----")
print(my_module.pi)


print("\n----Random Module----")
random_integer = random.randint(1, 10)
print(random_integer)

# Random acts as -> 0.0000000 - 0.99999999
random_float = random.random() 
print(random_float)

# Random will act as -> 0.0000000 - 4.9999999
random_float *= 5

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")