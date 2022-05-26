state1 = "Delaware"
state2 = "Pennsylvania"

# Storing it as lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]

# Lists keep order
print(states_of_america[0])
print(states_of_america[1])

# Counting from the end of the list
print(states_of_america[-1])

# Changing element's values
states_of_america[1] = "Pencil-vania"
print(states_of_america)

# Adding elements
states_of_america.append("Georgia")
print(states_of_america)

states_of_america.extend(["Virginia", "New York"])
print(states_of_america)

# IndexErrors
# print(states_of_america[23])

# Nested lists
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries",  "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)