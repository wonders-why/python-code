class Characters:
    def __init__(self, name, character):
        self.name = name
        self.character = character

    def show(self):
        print("Base characters show method.")

class JJK(Characters):
    def __init__(self, name, character):
        super().__init__(name, character)

    def show(self):
        print(f" Anime: {self.name}, strongest: {self.character}")

class TG(Characters):
    def __init__(self, name, character):
        super().__init__(name, character)

    def show(self):
        print(f" Dark anime: {self.name}, main: {self.character}")

# List of different objects (parent type reference)
animes = [JJK("Jujutsu Kaisen", "Gojo"), TG("Tokyo Ghoul", "Kaneki")]

for anime in animes:
    anime.show()

#Advanced topics to study
"""
Method overriding	
Abstract methods	
Duck typing	
Operator overloading	
Runtime polymorphism	
Polymorphic functions	
"""