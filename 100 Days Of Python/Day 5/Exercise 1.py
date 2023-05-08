# 🚨 Don't change the code below 👇
Student_heights = input("Input a list of student heights ").split()
for n in range(0, len(Student_heights)):
    Student_heights[n] = int(Student_heights[n])
print(Student_heights)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
for height in Student_heights:
    total_height += height
# print(total_height)


number_of_students = 0
for student in Student_heights:
    number_of_students +=1
# print(number_of_students)

average_height = round(total_height/number_of_students)
print(f"The average height of students is {average_height}")