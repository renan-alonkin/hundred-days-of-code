fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    print(fruits) # Will be run 3 times

print(fruits) # Will be printed only once

# For Loop with Range
for number in range(1, 11): # The last number is where it will stop
    print(number)
    
# Summing from 1 to 100
result = 0  
for number in range (1, 101):
    result += number

print(result)