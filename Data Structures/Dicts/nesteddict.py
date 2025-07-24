#so a dict can contain muliple dicts inside it and its called a nested dict

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

#how do we access the specific value

print(myfamily["child2"]["year"])

#loops can be used in a similar way as before but we have to use double loops

for x in myfamily.keys():
    print(x)  # prints the outer key, like 'child1'
    for y in myfamily[x]:  # y will be 'name' or 'year'
        print(y + ": " + str(myfamily[x][y]))  # safe string formatting

