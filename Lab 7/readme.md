# Executive Summary
___
# File/Folder Compression
### File Compression
A *zipped* (compressed) file will take up much less storage and can be transferred to other machines way quicker. This is the purpose of file compression.  A vector graphics file contains mathematical calculations that are then rendered in the colors the user chooses. A regular image file contains the plotted points for each pixel and whatever color is assigned to. This is why the svg file is much smaller than a rendered image file. Also, this means that the svg file has some sort of natural compression, with it just being some math.
___
# Python OOP
There is a method in the shark class for the shark swimming and the shark being awesome. The property (parameter) of each of the methods is "self". I believe that self, in Python, is similar to this.Method in C# or JavaScript. "Self" doesn't need to be named "self", you can use another parameter name instead, however it is convention to use the word "self."

A constructor is a method that predefines variables in a class. For instance,say I wanted every employee at a firm to have a starting wage. First, I would have a salary variable, and a constructor function declared. Then, within the constructor, I would set that variable equal to the desired starting wage. In the example given, they use a constructor to name the shark.

A class is the blueprint to an object. You can have many objects of the same class, they will juct follow the same "blueprint". For instance, i can have many many sharks, but they would all be a part of the shark class and follow the same blueprint and guidelines that I set in place for a shark. To instantiate an object from a class is to create an object that accesses the variables and functions in that class. This is done in python like this

<code>
  class Shark():
    def __init__(self, name, species):         #__init__ is short for initialize and it defines a constructor function<br>
      self.name = name<br>
      self.species = species<br>
    def swim(self):<br>
      print(self.name + " who is a " + self.species + " is swimming")<br>
  
  sharkGabe = Shark("Gabe", "Whale Shark")<br>
  sharkGabe.swim()<br>
</code>
___
# OOP Concepts
___
# Conclusion
