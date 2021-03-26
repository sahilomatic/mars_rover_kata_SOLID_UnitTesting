
from marsrover.position import RoverPosition




class Rover:
    """Class to control Rover Movements"""

    def __init__(self, plateau, initialPosition):
        """
        Assign Plateau dimensions and initial position of 1 rover
        :param plateau: Plateau
        :param initialPosition: RoverPosition
        """
        if not plateau.isPositionWithinPlateauArea(initialPosition):
            raise ValueError('rover initial position out of plateau area')
        self.plateau = plateau
        self.currentPosition = initialPosition



    def processCommands(self, commands):
        """
        Change coordinates of Rover and orientation based on instruction
        :param commands: list(MovementCommand)
        :return: None
        """

        for command in commands:

            if command == 'M':
                self.move()
            if command == 'R':
                self.turnRight()
            if command == 'L':
                self.turnLeft()

    def turnLeft(self):
        """
        Change Orientation of rover by 90 degree counter-clockwise
        when instruction is left
        :return: None
        """
        leftOrientationMapping = {
            'N': 'W',
            'W': 'S',
            'S': 'E',
            'E': 'N'
        }

        # if found in dict leftOrientationMapping else 'N'
        newOrientation = leftOrientationMapping.get(self.currentPosition.orientation, 'N')
        # update rover position
        newPosition = RoverPosition(self.currentPosition.coordinateInX,
                                    self.currentPosition.coordinateInY,
                                    newOrientation)
        # assign new position to rover object
        self.currentPosition = newPosition
        return newPosition

    def turnRight(self):
        """
        Change Orientation of rover by 90 degree clockwise
        when instruction is right
        :return: None
        """
        rightOrientationMapping = {
            'N': 'E',
            'W': 'N',
            'S': 'W',
            'E': 'S'
        }
        #if found in dict rightOrientationMapping else 'N'
        newOrientation = rightOrientationMapping.get(self.currentPosition.orientation, 'N')
        #update rover position
        newPosition = RoverPosition(self.currentPosition.coordinateInX,
                                    self.currentPosition.coordinateInY,
                                    newOrientation)
        #assign new position to rover object
        self.currentPosition = newPosition
        return newPosition

    def move(self):
        """
        Change X-Y coordinates of rover on move
        :return: None
        """
        # update x and y coordinates based on orientation
        # (N : y+1) ; (S : y-1)
        # (E : x+1) ; (W : x-1)
        moveMappingTable = {
            'N': lambda: RoverPosition(self.currentPosition.coordinateInX,
                                                     self.currentPosition.coordinateInY + 1,
                                                     self.currentPosition.orientation),
            'S': lambda: RoverPosition(self.currentPosition.coordinateInX,
                                                     self.currentPosition.coordinateInY - 1,
                                                     self.currentPosition.orientation),
            'W': lambda: RoverPosition(self.currentPosition.coordinateInX - 1,
                                                    self.currentPosition.coordinateInY,
                                                    self.currentPosition.orientation),
            'E': lambda: RoverPosition(self.currentPosition.coordinateInX + 1,
                                                    self.currentPosition.coordinateInY,
                                                    self.currentPosition.orientation)
        }
        newRoverPosition = moveMappingTable.get(self.currentPosition.orientation,
                                                lambda: RoverPosition(0, 0, 'S'))()
        if not self.plateau.isPositionWithinPlateauArea(newRoverPosition):
            raise ValueError('rover cannot be driven out of plateau area')
        self.currentPosition = newRoverPosition
        return self.currentPosition
