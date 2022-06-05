#Write your code below this row 👇

for number in range(1, 101):
    sentence = ""
    if number % 3 == 0:
        sentence += "Fizz"
    if number % 5 == 0:
        sentence += "Buzz"
    
    if(sentence == ""):
        sentence = number
    
    print(sentence)