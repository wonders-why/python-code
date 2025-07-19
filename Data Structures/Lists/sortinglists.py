#sorting

List = [3, 2, 3, 4, 5, 1]

List.sort() # the sort function is used to sort out the data
print(List)

List.sort(reverse=True)
print(List) # to sort in a reverse order

list2 = ['a', 'b', 'c', 'D', 'd', 'A']

list2.sort()
print(list2)

list2.sort(key=str.upper)
print(list2)