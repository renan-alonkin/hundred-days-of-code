# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

days_in_year = 365
weeks_in_year = 52
months_in_year = 12

aimed_age = 90

aimed_age_in_days = aimed_age * days_in_year
aimed_age_in_weeks = aimed_age * weeks_in_year
aimed_age_in_months = aimed_age * months_in_year

days_left = aimed_age_in_days - (age * days_in_year)
weeks_left = aimed_age_in_weeks - (age * weeks_in_year)
months_left = aimed_age_in_months - (age * months_in_year)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")


