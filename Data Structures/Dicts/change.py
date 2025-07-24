# changing the values of keys 

a_dict = {
    "name": "deepak",
    "lastname" : "Singh"
}
a_dict["name"]  = "Daniel"
print(a_dict)

#another way to change the values is

a_dict.update({"lastname":"Walker"})
print(a_dict)

#del, clear, pop, popitems use

a_dict.pop("name")#removes the specified element
a_dict.popitem()#removes the last element
a_dict.clear()#Empties the dict


"""Del is used to delete the whole list or a specified item"""

del a_dict["lastname"]
del a_dict

