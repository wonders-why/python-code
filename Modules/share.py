#now we will access module file here
import module as mvp# importin the whole file , mvp here is a varible we assigned for our convinience
from module import person1
from module2 import is_palindrome #importing a funtion from it

mvp.greet("fuck yourself!") # to use the function we have to use the assigned varible or the module name which is module here

print(mvp.person1["name"])

x = dir(mvp) #this funtion tells the name of all functions in the file u you imported
print(x)

is_palindrome(92829)
is_palindrome("helleh")