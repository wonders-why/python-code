"""
When we create a tuple with values, it's called packing
"""

atuple = tuple(("red", "Orange", "purple"))  # Packed tuple with color values

"""
Unpacking: assign tuple values to variables
"""
(Apple, Orange, papaya) = atuple

print(Apple)   # Prints 'red'
print(Orange)
print(papaya)

"""
The number of variables must match the number of values inside the tuple
"""

"""
If the number of variables is less, we can use * to assign leftover values to the last variable
"""

touple = ("Apple", "Orange", "papaya", "kakorot")

(one, two, *three) = touple

print(one, two, three)  # 'three' gets a list of the remaining values
