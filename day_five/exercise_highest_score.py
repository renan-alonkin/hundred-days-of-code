# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_score = max(student_scores) # This is considered cheating for this exercise

# We presume the first one is the highest, in case there is only 1
max_score = student_scores[0]
for score in student_scores:
    if(max_score < score):
        max_score = score
        
print(f"The highest score in the class is: {max_score}")