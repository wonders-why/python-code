# There are only 2 methods in tuple

a = (1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5)

# index() returns the index of the first occurrence of the given value
b = a.index(3)
print(b)

# count() returns how many times the given value appears in the tuple
c = a.count(5)
print(c)
