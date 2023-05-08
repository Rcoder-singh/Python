# Write your code below this row 👇
print("Method 1 using modulus \n")
total1= 0
for i in range(1,101):
    if i%2==0:
        total1+=i
print("Sum of all even numbers upto 100 =",total1)

print("Method 2 using stepping by 2\n")

total2 =0
for i in range(2,101,2):
    total2 +=i
print(f"Sum of all even numbers upto 100 = {total2}")

