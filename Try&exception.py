# what is try exception
"""so basically when u make a mistake like syntax error the program usually throws error thats why
we need to use try and exveption methods to avoid errors. the try block holds the code that might have
an eroor and exception basically stands for " a problem has occured" instead throwing errors.
"""

#for example

try:
    print(x) # remeber there is no x variable so it should throw an erro
except:
    print("An error occured")

    """the try block gets ignored as it will throw an error"""

#there are diffrent types of errors and so are their name

print("Second")
try:
    print(y)
except NameError:
    print("Its a name error")
except:
    print("Some other error")

#in case there was no error the block will execute
try:
    print("hello")
except:
    print("An error occured")
else:
    print("no error occured") # the else block is there for except. if the except condition doesnt prints the else will


"""There is also a finally keyword that can be used to do anything either way if the condition is right or wrong"""

try:
    print("hello")
except:
    print("An error occured")
finally:
    print("The block is finished")


    """There is also a way to raise errors ourselves"""
age = int(input("Enter your age"))
if age <  18:
    raise TypeError("You are a minor")