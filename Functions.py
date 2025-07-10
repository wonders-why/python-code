# funtions, calling and creating functions

def greet(Name, Greeting):
    print(f"Hellow,{Greeting}, my name is {Name}")

greet(Greeting="Konichiwa", Name="Deepak")
greet("Amrit", "Good morning")

#Arguments and parameters
#parameters are the initialized variables present in the parenthses in function defination.
#Arguments are the values we pass to the funtion variables.

def person(Name, age = 20):  #20 is a default value 
    print(f"Hello, I'm {Name}, My age is {age}")


person("Deepak", 20)

#args keyword is used when u dont know how many arguments u will have to pass.

#Arbitory argument
def intro(*Name):
    print(f"My name is {Name[0]} and this is my friend {Name[1]}")
    # yes make sure to rememeber the indexing starts from 0 "i fcked up here lol"

intro("Deepak", "Amrit")

#Arbitory keyword argument
def intro(**food):
    print(f"There are diffrent types of food catogories like vegitables {food["vegies"]}, fruits{food["fruti"]}, meat {food["meat"]} and etc ")
    #the variables indexing is string so we have to use quotations
intro(vegies ="cucumber", fruti = "Mangoes", meat ="Chicken")


#things like /, * are used to define positional and non postianl only argument 

#a fucntion with nothing to do uses pass as its body 

# a fucntion can also pass a list as arguments

# and remeber use Return when returning values to variables for storing and further alterations...
