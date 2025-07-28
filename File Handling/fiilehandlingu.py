
f = open("File Handling/hello.txt", "rt") # this is how to create a file using open and f read function
print(f.read())
f.close() # after opening a file, its a good practice to close it
#f = open("File Handling/wush.txt", "x") #x is used to create a file  a is for append, w is for write and t is for text and b is for binary


with open("File Handling/wush.txt") as x:# with statment allows us to automatically close the file once we are done with it.
    print(x.read())

#we can also specifiy how many part of the file we want to see

with open("File Handling/hello.txt", "rt") as y:
    #print(y.read(3))  # here 3 represents 3 numbers or letters from the file
    print(y.readline())

#we can also read only a line using radline futnion in print