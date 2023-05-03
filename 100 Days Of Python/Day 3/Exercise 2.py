#Calculate BMI

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = float(float(weight)/float(height)**2)
print(round(BMI,2))
if(BMI<18.5):
  print("You are underweight!")
elif(18.5>BMI<25):
  print("Hurry you have normal weight.")
elif(25>BMI<30):
  print("You are overweight go on a diet please.")
elif(30>BMI<35):
  print("Oh!no you are obese.")
elif(BMI>35):
  print("You are clinically obese.")
  
