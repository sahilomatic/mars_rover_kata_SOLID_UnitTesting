

class RoverInstruction:
    """Class to Store Initial Position and Commands of Individual Rover"""
    def __init__(self, initialPosition, movementCommands):
        """
        Create Object with position and and list of commands given to Rover
        :param initialPosition: RoverPosition
        :param movementCommands: list
        """

        print(movementCommands)
        self.initialPosition = initialPosition
        print(initialPosition.orientation)
        self.movementCommands= movementCommands


    def toString(self):
        movementCommandsAsString = ''.join([command for command in self.movementCommands])
        return self.initialPosition.toString() + '\n' + movementCommandsAsString


