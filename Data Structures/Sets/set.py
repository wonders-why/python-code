# A set is a built-in data type in Python
# It is unchangeable (items can't be modified), unordered, and does not allow duplicates
# Curly braces {} are used to create sets
# Note: 1 and True, 0 and False are treated as the same values in a set

a_set = {1, 2, 3, 4, 5, "A", "B", "C"}
b_set = set((9, 8, 7, 6, 5))  # Using set() constructor to create a set

print(a_set)
print(type(b_set), len(b_set))

# To print specific values, we can use a loop
for x in a_set:
    print(x)

# Membership test
if 4 in a_set:
    print(4)
