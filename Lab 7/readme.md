# Executive Summary
Lab 7 has everything to do with the insanely powerful tool that is Object Oriented Programming. First, we'll look at File compression. I'm interested to see how and why we compress files. Next, we will explore OOP in python. I'm most excited to do this one, because I just learned OOP in C# and want to know how to do it in Python too. Finally we will look at some of the concepts of OOP.
___
# File/Folder Compression
### File Compression
A *zipped* (compressed) file will take up much less storage and can be transferred to other machines way quicker. This is the purpose of file compression.  A vector graphics file contains mathematical calculations that are then rendered in the colors the user chooses. A regular image file contains the plotted points for each pixel and whatever color is assigned to. This is why the svg file is much smaller than a rendered image file. Also, this means that the svg file has some sort of natural compression, with it just being some math.
___
# Python OOP
There is a method in the shark class for the shark swimming and the shark being awesome. The property (parameter) of each of the methods is "self". I believe that self, in Python, is similar to this.Method in C# or JavaScript. "Self" doesn't need to be named "self", you can use another parameter name instead, however it is convention to use the word "self."

A constructor is a method that predefines variables in a class. For instance,say I wanted every employee at a firm to have a starting wage. First, I would have a salary variable, and a constructor function declared. Then, within the constructor, I would set that variable equal to the desired starting wage. In the example given, they use a constructor to name the shark.

A class is the blueprint to an object. You can have many objects of the same class, they will juct follow the same "blueprint". For instance, i can have many many sharks, but they would all be a part of the shark class and follow the same blueprint and guidelines that I set in place for a shark. To instantiate an object from a class is to create an object that accesses the variables and functions in that class. This is done in python like this (this example will also be included in the repository):

```python
  class Shark():
    def __init__(self, name, species):         #__init__ is short for initialize and it defines a constructor function
      self.name = name
      self.species = species
    def swim(self):
      print(self.name + " who is a " + self.species + " is swimming")
  
  sharkGabe = Shark("Gabe", "Whale Shark")
  sharkGabe.swim()
```
___
# OOP Concepts
If I was to go through a drive-through at a Culvers, I would have: a class that represents any order and a variable for burgers, a variable for sides, and a variable for drinks. Then, in that class I would have a constructor with boolean parameters (such as BoolBurger, BoolSide, BoolDrink, etc.) and if statements that take the parameter data to decide whether or not to display an item on my order. Finally, I would have an object that represents my specific order, with the parameters for burger and drink set to true and everything else to false. 

* Object - Gabe, Sammy, and Stevie were Objects of the shark class. They were instantiated from the shark class.
* Class - Shark would be the class as it is the name of the class and provides the instructions for shark objects.
* Abstraction - the definition of a shark is an abraction. An abstraction is 
* Encapsulation - swim(self) is an encapsulation. It is a method that can be called upon by different objects.
* Inheritance - A specific type of shark would be an inheritance.
___
# Conclusion
In Lab 7 has we coveredFile Conpression and Object Oriented Programming. First, we looked at some of the aspects of file compression. Files are compressed for ease of sharing and minimizing your storage used. Next, we looked at python's way of doing OOP. The syntax was bafflingly simple, however, more practice is needed for me to fully understand how python computes OOP. Finally we looked at some of OOP concepts. These concepts included, but were not limited to: Abstraction, Encapsulation and Inheritance. These are important to understand because they are some of the more important concepts of OOP. 
