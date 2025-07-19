#traversal in simple words

tople = (1,2,3,4,5)

print("Its a for each loop")
for x in tople:
    print(x)

print("its a range fucntion")
for x in range(1, len(tople)+1): # or for x in range(len(tople))
    print(x)


print("Its a while loop")
x = 0
while x < len(tople):
    print(tople[x])
    x += 1