# vehicleClass.py

class Vehicle:
    '''
    Vehicle Class
    This class models a vehicle on a used car lot
    Change order: we need to add maximum speed to the model
    Change order: we need a way to 'read' the max speed from the model
    Change order: some developers need to use the constructor without having to provide a max speed
    '''
    # constructor is called when you instantiate (create) an object of vehicle type
    def __init__(self, type, max_speed = None):
        '''
        @param type: the kind of vehicle
        @param max_speed: max speed of the vehicle, defaults to none
        '''
        self.type = type;
        self._thisisprivate = 42 # this is the weak attempt to "support" data hiding
        self.max_speed = max_speed # save a copy in the current object
    # instance method. it operates on an instance of the vehicle class which is an object
    def printType(self):
        print(self.type);
        
    def getSpeed(self):
        return self.max_speed

if __name__ == "__main__":
    # Some code to test the class would go here.
    # If there's no code, just pass
    pass
