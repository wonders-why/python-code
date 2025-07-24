# so there are diffrent ways to loop in dicts for example
# you wanna loop the dicts, or only the values, or maybe just the keys.

"""Here is how you can do it"""

adict = {
    "name" : "Deepak",
    "age" : 20,
    "lastname" : "singh"
}

for x in adict: #loops through the keys
    print(x)

for x in adict:
    print(adict.get(x))# loops through the values

for x in adict.keys():# loops through keys 
    print(x)

for x in adict.values():#print values
    print(x)

for x in adict.items():#prints the whole items, keys and values together
    print(x)