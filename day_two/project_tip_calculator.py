from math import ceil

print("Welcome to the tip calculatopr.")

total_bill = float(input("What was the total bill? $"))

percentage = int(input("What percentage would you like to give? 10, 12, or 15? "))

amount_people = int(input("How many people to split the bill? "))

to_be_paid_by_each_person = round((total_bill * (1 + percentage / 100)) / amount_people, 2)

formatted_to_be_paid_by_each_person = "{:.2f}".format(to_be_paid_by_each_person)

print(f"Each person should pay: ${formatted_to_be_paid_by_each_person}")