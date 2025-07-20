# Sorting lists

List = [3, 2, 3, 4, 5, 1]

# Sort in ascending order (default)
List.sort()
print(List)

# Sort in descending order
List.sort(reverse=True)
print(List)

list2 = ['a', 'b', 'c', 'D', 'd', 'A']

# Sort with case sensitivity (uppercase letters come before lowercase)
list2.sort()
print(list2)

# Sort ignoring case by converting all to uppercase during comparison
list2.sort(key=str.upper)
print(list2)
