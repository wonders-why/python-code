# The sets are unchangeable, yet we can still update and add values inside them

set1 = {1, 2, 3, 4, False}

# Use add() to add values to the set
set1.add(10)
print(set1)

# We can also extend one set with another
set2 = {"a", "b", "c"}
set1.update(set2)  # We can also pass a list or tuple to update()
print(set1)

""" Union """
# This method is used to combine two sets and join them together
set3 = set1.union(set2), set1 | set2  # Both return the same values
print(set3)

""" Intersection """
# This method returns the values that are present in both sets (duplicate values)
a = {1, 2, 3, 5, 6, 8}
b = {1, 2, 4, 6, 9}

# Using intersection() or & operator
c = a.intersection(b) or a & b
print(c)

# intersection_update() modifies the original set
a.intersection_update(b)
print(a)  # It will return the same values as c

""" Difference """
# This method returns the unique values from aa that are not in bb
aa = {1, 2, 3, 4, 5, 6, 7}
bb = {1, 4, 6, 9, 7, 0}

# Using difference() or - operator
d = aa.difference(bb) or aa - bb  # 2, 3, and 5 are unique to aa
print(d)

# difference_update() modifies the original set
aa.difference_update(bb)

""" Symmetric Difference """
# Returns all the values from both sets that are non-duplicate
c = aa.symmetric_difference(bb) or aa ^ bb  # Both work the same
print(c)

# symmetric_difference_update() modifies the original set
aa.symmetric_difference_update(bb)
