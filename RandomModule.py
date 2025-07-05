# Random Module helps you pick a random number from the range you give it.
import random

print(random.randrange(0, 99)) #picks from the randome range of 0 to 99

x = range(1,999)
print(random.choice(x)) #picks fromt he range you hvae given it the range acts as sequence

print(random.random()) #picks a random float from 0.234, 0.897

print(random.randint(1, 10)) #picks a random integer between the sequence

fruits = ['apple', 'banana', 'cherry']
print(random.choice(fruits)) #similar to range, picks a value out of list

nums = [1, 2, 3]
print(random.choices(nums, k=5))# same as above but this one actually gives 5 random values beacuase of 'k'

nums = [1, 2, 3, 4]
print(random.sample(nums, 2))# picks unique elements unlike above one

nums = [1, 2, 3, 4]
random.shuffle(nums)#used to shuffle the list
print(nums)
