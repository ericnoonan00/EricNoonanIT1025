class Shark():
    def __init__(self, name, species):         #__init__ is short for initialize and it defines a constructor function
      self.name = name
      self.species = species
    def swim(self):
      print(self.name + " who is a " + self.species + " is swimming")

sharkGabe = Shark("Gabe", "Whale Shark")
sharkGabe.swim()
