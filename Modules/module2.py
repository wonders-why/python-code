#so this is a another module with diffrent fucntions

def add(a, b):
    return a + b

# Example:
print(add(3, 5))  # Output: 8

def greet(name):
    print(f"Hello, {name}!")

# Example:
greet("Deepak")  # Output: Hello, Deepak!

def is_palindrome(word):
   if type(word) == int:
       word = str(word)
   if word == word[-1::-1]:
       return print("it is a palindrome")
   else :
       return print("its not a palindrome")
