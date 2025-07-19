#lets learn to copy lists

a = ["Deepak", "Daniel", "Ash"]
b = a# this doesnt copies the list but makes a reference to it like it happens in funtion. if the value of a changes it will reflect on b aswell
print(b)

a.append("Asta")
print(b)

"""So how can we copy it? we can use a function called copy"""

c = a.copy() # other things we can use is
d = list(b)# using list funtion
e = c[:]#using slicing
a.append("HI")
print(a, c)

#this is similiar to slicing lissts but easier
thislist = ["apple", "banana", "cherry"]
mylist = []

for item in thislist:
    mylist.append(item)
