# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_as_int = int(age)

if age_as_int <= 90:
 years_remaining =  90-age_as_int
 days_remaining =  years_remaining *365
 weeks_remaining= years_remaining *52
 months_remaining= years_remaining *12

 message = f"You have {days_remaining} days, {weeks_remaining} weeks,{months_remaining} months, {years_remaining} years to make yourself best,better than the rest."
 print(message)

else:

    print( "You have outlived many people of your year of birth.")
