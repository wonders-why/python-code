#if 

x = int(input("Enter x : "))
y = int(input("Enter y : "))

# a simple if statement with 3 blocks consisting of if, elif and else.
if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equals")
else:
    print("x is smaller then y")

#shorthand for if 
if x < y: print(" y is greater")

#shorthand for if-else
print ("is greater") if x > y else  print("is smaller")

#match statement, it is similar to switch statement in other languages.

x = int(input("Enter the month : "))

match x:
    case 1  :
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4 | 5 : # to put multiple cases n one block
        print("its wed or thursday")
    case _: #used as default value 
        print("No vales")
 
 #while loop


x = 1
while 5 > x:
    print(x)
    x += 1
    if x == 5:
        break
    else:
        print("The loop is over")

# There is no do while loop python but we hvae while else where else pushesh once the while is finsihed 
x = 1
while 5 > x:
    print(x)
    x += 1
else:
    print("The loop is finally over")


# for each loop

x = ["y","x","z"]
for alp in x:
    print(alp)


# these are all the looping statements for each loop and break and continue have similar use to other langauges lik break breaks the loop and continue skips the current itiration of loops.