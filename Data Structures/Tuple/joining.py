# To extend or join a tuple with another, there is no built-in function — we use the + operator

x = (1, 2, 3, 4, 5)
y = (6, 7, 8, 9, 0)

print(x + y)  # Concatenates both tuples

# We can also multiply a tuple to repeat its contents
z = x * 3  # Creates a new tuple z, which repeats x three times
print(z)
