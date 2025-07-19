# lets create touples
#ordered, unchangeable unlike lists, allows duplicacy
#reperesented by cruved bracket ( )

touple = (1,2,3,4,5)
print(type(touple), touple, len(touple))

a_touple = tuple((5,6,7,8,9)) #the tuple constructor to create a tuple

#the indexing is same as lists, the simple one the negitive indexing and also the slicing / range indexing

"""how to check an item in a tuple"""

if 5 in a_touple:
    print("yes it is there")
else:
    print(False)

#the tuples are unchangeable so what we can do to change the items inside of it? 

#converting a tuple to list and changing values and then returning it back to tuples is the solution here is how we do it
if 6 in touple:
    print(True)
else:
    print(False)

x = list(touple)
x.append(6)
x.remove(3)
touple = tuple(x)

if 6 in touple:
    print(True)
else:
    print(False)

if 3 in touple:
    print(True)
else:
    print(False)

#also del keyword can help to delte the tuple

del touple