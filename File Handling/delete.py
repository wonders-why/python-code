#How to delete a file
import os

try:
    os.remove("File Handling/deletefile.txt") 
except FileNotFoundError:
    print("The file doesnt exist")

# to delete a folder us rmdir (remove directory)
try:
    os.rmdir("File Handling/deletedir")
except FileNotFoundError:
    print("file doesnt exist") # my compuet deied the access so i got an eror try deleting your os that might help