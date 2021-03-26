


class RoverPosition:
    """Class to store Rover Positions"""
    def __init__(self, coordinateInX, coordinateInY, orientation):
        """

        :param coordinateInX: int
        :param coordinateInY: int
        :param orientation: str
        """
        self.coordinateInX= coordinateInX
        self.coordinateInY = coordinateInY
        self.orientation= orientation


    def toString(self):
        return str(self.coordinateInX) + " " + str(self.coordinateInY) + " " + str(self.orientation)
