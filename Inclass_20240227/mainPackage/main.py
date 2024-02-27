# main.py
# add import statement 
from vehiclePackage.vehicleClass import *

if __name__ == "__main__":
    # instanatiate an object of type Vehicle
    
    myCorvette = Vehicle("Car", 120) # will trigger a call to the constructor
    myCorvette.printType() # invoking the method on the object
    
    # invoke the getter for max speed and store the return value in a variable
    # print that out
    
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed:", maximum_speed)
    
    # instantiate another vehicle object
    
    myChevrolet = Vehicle("SUV") #myChevrolet is an object of type Vehicle
    myChevrolet.printType()
    
    # i want a list of 3 vehicle: car, boat, space ship
    # you can pick the names and properties
    # i want some friendly output to demo your work
    
    myVehicles =[Vehicle("toyota camry", 150),
                Vehicle("sailboat", 20),
                Vehicle("Falcon Heavy", 4000)]
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())