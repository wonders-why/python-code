# Removing items or the set entirely

aset = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# remove() removes the specified item; throws an error if the item is not present
aset.remove(8)

# discard() removes the item if present; does nothing if the item is absent
aset.discard(9)

# pop() removes a random item from the set
aset.pop()

# clear() empties the set completely
aset.clear()

# del deletes the set entirely
del aset

print(aset)
