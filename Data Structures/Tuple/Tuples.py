# Let's create tuples
# Ordered, unchangeable (immutable) unlike lists, and allows duplicates
# Represented by curved brackets ( )

touple = (1, 2, 3, 4, 5)
print(type(touple), touple, len(touple))

# Using the tuple constructor to create a tuple
a_touple = tuple((5, 6, 7, 8, 9))

# Indexing is the same as in lists: normal indexing, negative indexing, and slicing work

"""How to check an item in a tuple"""
if 5 in a_touple:
    print("Yes, it is there")
else:
    print(False)

# Tuples are unchangeable, so how do we change values inside them?
# Solution: Convert to list → modify → convert back to tuple

if 6 in touple:
    print(True)
else:
    print(False)

x = list(touple)
x.append(6)
x.remove(3)
touple = tuple(x)

if 6 in touple:
    print(True)
else:
    print(False)

if 3 in touple:
    print(True)
else:
    print(False)

# The del keyword can delete the entire tuple
del touple
