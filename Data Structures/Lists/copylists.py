# Let's learn to copy lists

a = ["Deepak", "Daniel", "Ash"]
b = a  # This does NOT copy the list; it creates a reference to the same list
print(b)

a.append("Asta")
print(b)  # b also reflects the change because it's the same list reference

"""How to properly copy a list"""

c = a.copy()    # Using the copy() method
d = list(b)     # Using the list() constructor
e = c[:]        # Using slicing

a.append("HI")
print(a, c)  # 'a' changed but 'c' remains unchanged because it's a copy

# Similar to slicing but manual copying using a loop
thislist = ["apple", "banana", "cherry"]
mylist = []

for item in thislist:
    mylist.append(item)
