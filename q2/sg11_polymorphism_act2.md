
1. Answer the following questions:
    
    a. What is duck typing, as explained in the video?

    - Duck typing merely cares about what the object does (methods) rather than what class the object is in. As long as they have the same method, despite being in completely unrelated classes, the object will function.

    b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

    - The Car class needed the same method names as the other Animal classes for duck typing and polymorphism to work.

2. Create the Python code that:
    
    a. Creates three classes: Car, Boat, and Drone with a method move().
        
        move() in the Car class prints "The car drives on the road."
    
        move() in the Boat class prints "The boat sails on water."
    
        move() in the Drone class prints "The drone flies in the sky."
    
    b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the move() method: vehicle.move().
    
    c. Creates one object of each class.
    
    d. Calls the start_trip() method for each object.

    - [Code for #2](q2/sg11_polymorphism_act2.py)

3. How does the code in 2.2 demonstrate polymorphism?

- The three classes used above (Car, Boat, and Drone) are unrelated and not subclasses of one another. However, they are all defined by the method move(). The function start_trip() doesn't care about the type of vehicle (car, boat or drone) as long as it has the move() method.
