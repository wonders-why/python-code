#before 3.6 of python we had to use format()
# but now we can use f string 
age = 17
txt = f"My name is deepak, I'm {age} years old"
print(txt)

txt =  f"My name is deepak, I'm {age:.3f} years old" #.3f represents 3 floating points
print(txt)

"""We can also perform mathmatical operationusig f string"""
txt = f"Im  2x10 years old so that makes me {2*10}"
print(txt)
price = 1000
fruit = 'apple'

txt = f"This {fruit} is {"expensive" if price>100 else "cheap"}"
print(txt)
txt = f"This {fruit.capitalize()} is very delicious"
print(txt)

"""format function can still be used but f string is better and faster. I know the basics of it and how to use thats enough as im not going to use it"""