import random
x = int(input("Enter the Start numbers :"))
y = int(input("Enter the End number :"))
z = range(x, y)

print(f"The random number is : {random.choice(z)}")
