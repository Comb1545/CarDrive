angles are mangaged in degrees, if radians is needed for math,
convert to radians, do math, return degrees

Each game loop give a list of moves for that gameloop to the controller.
valid moves in config -> controller{}


CarController:
    getAttributes():
        takes in nothing

        gets self.car relevant attributes
        
        attributes = [speed, angle, gearTopSpeed, each sensor<bool>]
        returns attributes 

    control():
        takes in list of controls with any of the following commands
        "accel", "steerLeft", "steerRight", "gearUP", "gearDown"

        controls car on screen
        returns nothing

Use getAttributes for input layer
Use control for output layer