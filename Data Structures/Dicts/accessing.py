"""To access dict items we can use its key to get the specific value"""
adict = {
     "Name" : "Deepak",
    "Age" : 20,
    "Course" : "bca",
    "list" : [1,2,3,45]
}
print(adict["list"])

"""There is a method that does the same work"""

a = adict.get("Course") # it gets the value from adict and copies it to a
print(a)

"""there is also a method to get keys that are in the dictionaries and as it share the same values u can expect it to update 
   automatically and change values.
"""
b = adict.keys()
print(b)
#now if we update it and print it agian the keys will be updated too

adict["Nation"] = "india"
print(b)

"""So there is another method that returns only values instead of keys"""

c = adict.values()
print(c)

"""There is also a mthod for returning the whole values but it will be in tuples"""
d = adict.items()
print(d)