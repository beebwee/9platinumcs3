# Parent Class

class Animal:
    def __init__(self, name): #This initializes the attributes once a class is made.
      self._name = name #This is attribute 1.
      
    def eat(self):
        print(self._name, "eats.") #This is the method of the objects.


class Lion(Animal): #Child class #1
    def eat(self):
        print(self._name, "eats fresh meat.")

    def make_sound(self): #This is method overriding.
        print(self._name, "roars loudly!")


class Elephant(Animal): #Child class #2
    def eat(self):
        print(self._name, "eats grass and fruits.")

    def make_sound(self): #This is method overriding.
        print(self._name, "trumpets!")

class Monkey(Animal): #Child class #3
    def eat(self):
        print(self._name, "eats bananas.")

    def make_sound(self): #This is method overriding.
        print(self._name, "chatters!")

#These are the created objects.
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

lion.make_sound()
lion.eat()
print("-----")

elephant.make_sound()
elephant.eat()
print("-----")

monkey.make_sound()
monkey.eat()
print("-----")