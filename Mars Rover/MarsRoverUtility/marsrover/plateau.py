


class Plateau:
    """Class to Store Plateau Dimensions"""
    def __init__(self, dimensionInX, dimensionInY):
        '''

        :param dimensionInX: int
        :param dimensionInY: int
        '''
        self.dimensionInX: int = dimensionInX
        self.dimensionInY: int = dimensionInY

    def isPositionWithinPlateauArea(self, position):
        '''
        check if rover coordinates are withing dimension of plateau
        :param position: RoverPosition
        :return: bool
        '''
        return not (position.coordinateInX > self.dimensionInX or
                position.coordinateInY > self.dimensionInY)

    def toString(self):
        return str(self.dimensionInX) + ' ' + str(self.dimensionInY)
