# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leap_year_msg = "Leap year."
not_leap_year_msg = "Not leap year."


if(not (year % 4 == 0)):
    print(not_leap_year_msg)
else:
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(leap_year_msg)
        else:
            print(not_leap_year_msg)
    else:
        print(leap_year_msg)