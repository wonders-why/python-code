#to write on files we need to use write and append parameters 

# a parameter only adds the text to the end of existing text
# w parameter replaces the existing text with new one
with open("File Handling/wush.txt", "a") as x:
    x.write(" 2 Nobara tokisaki")

with open("File Handling/hello.txt", "w") as f:
    f.write("The existing texts are deleted...")

with open("File Handling/wush.txt", "r") as x:
    print(x.read())