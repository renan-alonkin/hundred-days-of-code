import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names_len = len(names)
selected_name_index = random.randint(0, names_len - 1) # -1 Because the size is different from the last index

chosen_person = names[selected_name_index]

print(f"{chosen_person} is going to buy the meal today!")