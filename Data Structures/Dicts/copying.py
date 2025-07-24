#copying a dict is easier and similar to other data types

a_dict = {
    "Name" : "Deepak",
    "Age" : 20,
    "Course" : "bca",
    "list" : [1,2,3,45]
}

#simple copying
b_dict = a_dict.copy()

#copying using constructor
c_dict = dict(a_dict)

#to the wonderers
a_dict = b_dict # wont work because in python this automatically means that a_dict and b_dict share the same location, which means b_   dict is just a reference to the a_dict,
