# Lists are commonly used as a replacement for arrays in Python.
# Unlike arrays, a list is more dynamic and can store different types of data.
# A list is represented by square brackets [].
# It is changeable (mutable), ordered, and allows duplicates.

A_list = [1, 2, 3, "This", "Is", "A", "List", 1]

# It can also be initialized by the list() constructor function
This_list = list((1, 2, 3, "A", "list", "is", "A", "list"))

print(len(This_list), type(This_list), This_list[4])

if "list" in This_list:
    print(True)
else:
    print(False)

"""Now let's perform some common operations on lists"""

"""Let's add some items"""

# insert() - Inserts an item at a specific index without replacing existing items,
# shifting subsequent items forward.
A_list.insert(3, 4)  # index and the value
print(A_list)

# append() - Adds an item at the end of the list
A_list.append("I'm the added element")

# extend() - Merges another iterable (list, tuple, set, dict keys, etc.) to the list
A_list.extend(This_list)
print(A_list)

"""Let's delete some items"""

b_list = [1, 2, 3, "This", "Is", "A", "List", 1]

# remove() - Removes the first occurrence of the specified element by value
b_list.remove(3)
print(b_list)

# pop() - Removes and returns item at the given index (last if index not specified)
b_list.pop(5)  # Pops the element at index 5
b_list.pop()   # Pops the last element

# del and clear() - del deletes element or list entirely; clear empties the list
del b_list[0]  # Delete element at index 0
b_list.clear()  # Empties the list
del b_list      # Deletes the list entirely
