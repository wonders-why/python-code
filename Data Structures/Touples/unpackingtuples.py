# so as we create a tuple we put values inside it and its called packing it with data

#similarly we can unpack the data and assign it to variables.

atuple = tuple(("red", "Orange", "purple")) #this is a pakced tuple with color values

(Apple,Orange, papaya )  = atuple

print(Apple)# It will print the corresponding value which is red 
print(Orange)
print(papaya)

"""The number of varianbles must match the number of values inside tuple"""

"""Now, if we dont assign the same number of variables we can use astrik sign in the end to assign all the left out values to the last variable"""

touple = ("Apple","Orange", "papaya", "kakorot")

(one, two, *three) = touple

print(one, two, three)