class Animal:
    def __init__(self, name): #This initializes the attributes once a class is made.
        self.__name = name #This is attribute 1.

    def eat(self):
        print(self.__name, "eats")

    def make_sound(self):
        print(self.__name, )



class Lion(Animal):
     
    def eat(self):
        print(self.__name, "fresh meat.")

    def make_sound(self):
        print(self.__name, "roars loudly!")



class Elephant(Animal):
    def eat(self):
        print(self.__name, "grass and fruits.")

    def make_sound(self):
        print(self.__name, "trumpets!")


class Monkey(Animal):
    def eat(self):
        print(self.__name, "bananas.")

    def make_sound(self):
        print(self.__name, "chatters!")






#These are the created objects.
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound())
print(elephant.eat())
print("-----")

print(monkey.make_sound())
print(monkey.eat())
print("-----")