#Write your code below this row 👇
sum_of_evens = 0
# Using step
for even in range(2, 101, 2):
    sum_of_evens += even
    
print(sum_of_evens)

# Using if
another_sum_of_evens = 0
for number in range(1, 101):
    another_sum_of_evens += number if number % 2 == 0 else 0

# print(another_sum_of_evens)