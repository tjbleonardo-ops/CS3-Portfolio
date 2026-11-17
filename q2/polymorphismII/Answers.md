1. Answer the following questions:

a. What is duck typing, as explained in the video?
The philosophy of duck typing, is that if it quacks like a duck and walks like a duck, then it is a duck means that in polymorphism, an object is treated as something if it acts like
that thing.

b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
The speak() method.

2. Create the Python code that:
a. Creates three classes: Car, Boat, and Drone with a method move().
move() in the Car class prints "The car drives on the road."
move() in the Boat class prints "The boat sails on water."
move() in the Drone class prints "The drone flies in the sky."

b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the
move() method: vehicle.move().

c. Creates one object of each class.

d. Calls the start_trip() method for each object.

3. How does the code in 2.2 demonstrate polymorphism?
The code demonstrates polymorphism since every class that had the method move() could be called even if the function that calls them does not directly call the class. If the class can move like a vehicle, then it is a vehicle.
