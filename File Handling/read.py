with open("File Handling/wush.txt") as x:# with statment allows us to automatically close the file once we are done with it.
    print(x.read())

#we can also specifiy how many part of the file we want to read

with open("File Handling/hello.txt", "rt") as y:
    print(y.read(3))  # here 3 represents 3 numbers or letters from the file
    print(y.readline())

#we can also read only a line using readline function in print