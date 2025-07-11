#creation and initialisaion of class, object

class myanime:#what values can an anime class hold? 
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating# bad, mid, peak
 
    def output(self):# the self method is required in the funtions inside a class. self here represents the object this function get values from.
        return f"The Anime {self.name} is {self.rating}"
    
anime1 = myanime(name="Solo leveling", rating="Mid") #anime1 is now an object of the class anime
print(anime1.output())
anime2 = myanime("danmachi", "peak")
print(anime2.output())

#using init(), and _str_()
#the init function is used in above example to initialise the values inside the class it is also called a constructor.

class persom:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):#so the function is called when the object is printed as itself like we dont actaully call the values of the object but the object itself.
        return f"The object is {self.name}"
p1 = persom("Deepak", 20)
print(f"My name is{p1.name} and my age is {p1.age}")
print(p1)


#understanding the self parameter
def __init__(self):#self represents the object itself that is being created in obove example p1 and anime1 were both self
    pass#in case you wanna leave a constuctor empty

#Modification and deletion of object 

p1.name = "Amrit"
print(p1.name)
del p1.age
print(p1.age)# this will throw an error as we deleted the varibale age itself.

#there is a lot more then this to learn but dont overdo it as long as you learn something new in a decent amount then thats enouhg. you dont have to cram all the topics in one day just make sure to learn enough.