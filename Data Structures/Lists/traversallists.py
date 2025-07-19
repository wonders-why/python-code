#traversal is the fucntion to display all the values present in the data structure which can be done using loops

list = [1,2,3,4,5]

#for each loop
for x in list:
    print(x)

#while using the range and len funtion
for x in range(len(list)):
    print(list[x])

#using while loop
x = 0
while x < len(list):
    print(list[x])
    x += 1
    
[print (x) for x in list]