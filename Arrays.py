#arrays are lists in python, however to work with arrays we need to use numpy libraries

Animes =["Danmachi", "Apothcary Dairies", "Frieren"]

for x in Animes:
    print(x)
else:
    print("The list is printed")

# Append and insert are used to insert values but both have diffrent usage
Animes.append("Summertime Rendering")# it will simply add summtime rendering to the end of list/array
Animes.insert(2, "Oregairu") #2 here represents the index oregairu will be added at

for x in Animes:
    print(x)

print("Now lets remove some elements")
# we can use remove or pop for removal in the same way as append and insert
Animes.remove("Danmachi")#this  will simply remove the anime mentioned
Animes.pop(2)# it removes the element on index no 2 which is frieren in the list

for x in Animes:
    print(x)

#merging a list can be done using using extend() funtion and len() for length of the array/list, count() for counting a specific element in the list
#copy is used to copy one array/list another

"""Note"""
# as you learn and see problems new solutions that are already there will come to you. You just to find them...
#so dont learn all at once, build using what you know and once you know enough u will see thats not enough...
# and eventually u will seek things to sort problems ad develop things to solve other's problem
