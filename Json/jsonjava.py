import json
#json is the syntax for storing and exchanging data
#json is the text written by javascript object notations

"""So in python we can import json files and convert the data to read it as python data types or we can 
change the json files data and convert them into python data types and sort them out lets try
"""


x =  '{ "name":"John", "age":30, "city":"New York"}' #it is a json data, which are normally passed as strings

#lets print it 
print(x)
print(type(x)) # as it says string

#now lets convert it into python and then print it
y = json.loads(x) # the loads funtion here takes the json data and coverts it into the python data format...
print(y["age"])
print(y)
print(type(y)) 

"""now lets convert python data into json data"""

a_dict = {
    "Name" : "Deepak",
    "Age" : 20,
    "Course" : "bca",
    "list" : [1,2,3,45]
}

z = json.dumps(a_dict) #dumps funtion makes the data into json text
print(z, type(z))


"""We can actually format the data to make it more appealing and readable"""
a_dict = {
    "Name": "Deepak",
    "Age": 20,
    "Course": "bca",
    "list": [1, 2, 3, 45],
    "tuple": list((1, 2, 3, 4, 78)),     # tuple → list
    "set": [list({1,2,3,4}), list({1,2,3,4,5})]  # sets → lists
}


# so what the below fucntion does is gives 4 indents after every object and sorts keys according to the variables
formatteddata = json.dumps(a_dict, indent=4, sort_keys= True )
print(formatteddata)

#that is all for now in json we can explore more later if we feel like it hahahah