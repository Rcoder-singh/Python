import random

# Split string method
names_string = input("Give me everybody's names, seperated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Get the total number of items in list.
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")

# This can be also be written in place of above code but above code is to understand the concept.
# person_who_will_pay = random.choice(names)
