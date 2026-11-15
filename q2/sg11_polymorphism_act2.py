
1. Answer the following questions:
    
    a. What is duck typing, as explained in the video?

    b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?


2. Create the Python code that:
    
    a. Creates three classes: Car, Boat, and Drone with a method move().
        
        move() in the Car class prints "The car drives on the road."
    
        move() in the Boat class prints "The boat sails on water."
    
        move() in the Drone class prints "The drone flies in the sky."
    
    b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the move() method: vehicle.move().
    
    c. Creates one object of each class.
    
    d. Calls the start_trip() method for each object.

-----------------------------------------------------------------------------------------

a.

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

vehicles = [Car(), Boat(), Drone()]
for vehicle in vehicles:
    vehicle.move()

b.

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()  

vehicles = [Car(), Boat(), Drone()]
for vehicle in vehicles:
    start_trip(vehicle)

c. 

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()  

#Objects
car1 = Car()
boat1 = Boat()
drone1 = Drone()

vehicles = [car1, boat1, drone1]
for vehicle in vehicles:
    start_trip(vehicle)

3. How does the code in 2.2 demonstrate polymorphism?
The three classes used above (Car, Boat, and Drone) are unrelated and not subclasses of one another. However, they are all defined by the method move(). The function start_trip() doesn't care about the type of vehicle (car, boat or drone) as long as it has the move() method.