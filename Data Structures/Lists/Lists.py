#Lists are commonly used as a replacement of array in python.
#unlike array a list is more dynamic and can store diffrent types of data types.
#A list is represented by Square brackets.
#it is changeable and ordered in nature, it also allows duplicacy

A_list = [1, 2, 3, "This", "Is", "A", "List", 1]
#it can also be initialised by list() constructor fucntion
This_list = list((1, 2, 3,"A", "list", "is", "A", "list"))

print(len(This_list), type(This_list), This_list[4])

if "list" in This_list:
    print(True)
else:
    print(False)


"""Now lets perform some of the common operations on lists"""

"""Lets add some items"""

#Inset - it is funtion that can insert items without replacing the already present items. it adds the item to the specific index of list and moves the other items forwards.

A_list.insert(3, 4)# index and the value
print(A_list)

#append - Used to add an item at the end of list

A_list.append("Im the added element") 

#Extend - to merge two lists

A_list.extend(This_list)#The extend keyword can add any type of structure like tuples, dicts and also sets.

print(A_list)

"""Lets delete some of it lol"""
b_list = [1, 2, 3, "This", "Is", "A", "List", 1]

#Remove - to remove specific element by name

b_list.remove(3)
print(b_list)

#pop - used to pop specific or last item in the list
b_list.pop(5)#Pops the 5th index item
b_list.pop() #In case you dont mention the index it will pop the last item.

#del and clear - both are used to delete the element or list, as for clear it empties the list ratehre then delteing its existence.

del b_list[0]
b_list.clear()
del b_list

