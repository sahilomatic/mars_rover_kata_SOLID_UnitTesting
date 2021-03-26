from marsrover.rover import Rover
from marsrover.position import RoverPosition

from marsrover.plateau import Plateau

import unittest


class Test_Rover(unittest.TestCase):

    def test_RoverCanMoveToPosition(self):
        """
        test to check X- Y coordinates and Orientation changes when rover is given command to move
        :return:
        """
        # Given
        initialPosition = RoverPosition(2, 2, 'N')
        plateau = Plateau(5, 5)
        movementCommands = ['M','R','M','L','M']
        rover = Rover(plateau, initialPosition)
        # When
        rover.processCommands(movementCommands)
        # Then
        expectedFinalPosition = '3 4 N'
        self.assertEqual(rover.currentPosition.toString() ,expectedFinalPosition)


    def test_CannotCreateRoverIfInitialPositionOutOfPlateauArea(self):
        """
        test to check validation error is raised when initial X- Y coordinates of rover is
        outside plateau dimesnion
        :return:
                """

        # Given
        plateau = Plateau(5, 5)
        initialPosition = RoverPosition(6, 5, 'N')
        # Then
        self.assertRaises(ValueError, Rover,plateau, initialPosition)
        expected_error = 'rover initial position out of plateau area'
        try:
            # check that correct error message is reported when plateau dimension is not correct
            Rover(plateau, initialPosition)
        except Exception as error:

            self.assertTrue(expected_error in str(error))


    def test_CannotMoveRoverOutOfPlateau(self):
        """
        test to check validation error is raised when current X- Y coordinates of rover is
        outside plateau dimesnion
        :return:
                """
        # Given
        initialPosition = RoverPosition(2, 2, 'N')
        plateau = Plateau(3, 3)
        movementCommands = ['M', 'M', 'M']
        rover = Rover(plateau, initialPosition)
        # Then
        self.assertRaises(ValueError, rover.processCommands,  movementCommands)
        expected_error = 'rover cannot be driven out of plateau area'
        try:
            # check that correct error message is reported when plateau dimension is not correct
            rover.processCommands(movementCommands)
        except Exception as error:

            self.assertTrue(expected_error in str(error))



    


if __name__ == '__main__':
    print('Testing Rover Validation Test')
    unittest.main()