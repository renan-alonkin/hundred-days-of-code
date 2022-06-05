# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum_of_heights = sum(student_heights) / len(student_heights) # this is illegal for this exercise

sum_of_heights = 0
total_amount_of_students = 0

for student_height in student_heights:
    sum_of_heights += student_height
    total_amount_of_students += 1
    
average_height = round(sum_of_heights / total_amount_of_students)

print(average_height)