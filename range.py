# i have done this before but just noticed how naive i was so we can use range in diffrent ways

#there are 3 inputs at most in range funtion{start, end, step}

# where it starts, where it ends and where way does it goes and how many times it skips for ex postive indexing is forwards, negitive is backword. if u wreite 2 it will skip 1 word. like 1 then 1+2 = 3, then 3+2=5


for i in range(0, 6):#(start, end)
    print(i)

print("Second loop")
for i in range(1, 11, 1):#(start,end, step)
    print(i)

print("Third loop")

for i in range(10,0,-1):
    print(i)
