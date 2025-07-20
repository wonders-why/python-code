# Traversal means displaying all values present in a data structure,
# which can be done using loops.

list = [1, 2, 3, 4, 5]

# For-each loop
for x in list:
    print(x)

# Using range() and len() functions
for x in range(len(list)):
    print(list[x])

# Using while loop
x = 0
while x < len(list):
    print(list[x])
    x += 1

# List comprehension shorthand for printing
[print(x) for x in list]

# Let's do list comprehensions in detail later
