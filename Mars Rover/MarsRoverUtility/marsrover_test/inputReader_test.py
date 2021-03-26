from mock import patch, mock_open
from marsrover.input_reader import InputReader
from marsrover.setofinstructions import SetOfInstructions
from marsrover.plateau import Plateau
from marsrover.instruction import RoverInstruction
from marsrover.position import RoverPosition

from customErrors.input_reader_error import InputReaderError
import unittest


class Test_InputReader(unittest.TestCase):
    """This class is used to test InputReader class.
    Unit testing is done for methods like orientation , plateau dimension, instruction """

    # first function to run for initializing data
    def setUp(self):

        self.obj = InputReader()

    def test_shouldParseAValidSetOfInstructions(self):
        # Custom Inputs
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMR\n2 2 N\nRMLM'



        plateau = Plateau(5, 5)
        movement_commands1 = ['M''M''R']
        movement_commands2 = ['R','M','L','M']
        rover_instruction1 = RoverInstruction(RoverPosition(3, 3, 'E'), movement_commands1)
        rover_instruction2 = RoverInstruction(RoverPosition(2, 2, 'N'), movement_commands2)

        expectedSetOfInstructions = SetOfInstructions(plateau, [rover_instruction1, rover_instruction2])

        # mocking is done for  assertion statements
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            result = self.obj.readFile(filePath)

        # result
        self.assertEqual(result.toString(),expectedSetOfInstructions.toString())



    def test_shouldRaiseExceptionWhenPlateauDimensionsAreNotValid(self):
        # custom Input
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = 's 5\n3 3 E\nMMRMMRMRRM'
        expected_error = 'plateau X-Y coordinates should be positive integer'


        # mocking is done for both assertion statements

        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                # check correct error is raised
                self.assertRaises(InputReaderError, self.obj.readFile, filePath)

                try:
                    # check that correct error message is reported
                    self.obj.readFile(filePath)
                except Exception as error:

                    self.assertTrue(expected_error in str(error))


    def test_shouldRaiseExceptionWhenPlateauDimensionsAreNotExactlyTwo(self):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = 'hjhkjj\n3 3 E\nMMRMMRMRRM'
        expected_error = 'plateau dimensions should be in X-Y coordinates'
        # mocking is done for both assertion statements
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            # check correct error is raised
            self.assertRaises(InputReaderError, self.obj.readFile, filePath)

            try:
                # check that correct error message is reported
                self.obj.readFile(filePath)
            except Exception as error:

                self.assertTrue(expected_error in str(error))


    def test_shouldRaiseExceptionWhenInitialPositionIsNotValid(self):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 s E\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        expected_error = 'invalid literal'
        # mocking is done for both assertion statements
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            # check correct error is raised
            self.assertRaises(ValueError, self.obj.readFile, filePath)
            try:
                # check that correct error message is reported
                self.obj.readFile(filePath)
            except Exception as error:
                print(error)
                self.assertTrue(expected_error in str(error))


    
    def test_shouldRaiseExceptionWhenInitialPositionIsNotExactlyThreeValues(self):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        expected_error = "rover position should be in X-Y coordinates and orientation in NSEW"
        # mocking is done for both assertion statements
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            # check correct error is raised
            self.assertRaises(InputReaderError, self.obj.readFile, filePath)
            try:
                # check that correct error message is reported
                self.obj.readFile(filePath)
            except Exception as error:
                print(error)
                self.assertTrue(expected_error in str(error))



    def test_shouldRaiseExceptionIfPlateauDimensionsAreNotExactlyTwo(self):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5\n3 3 E\nMMRMMRMRRM'

        expected_error = "plateau dimensions should be in X-Y coordinates"
        # mocking is done for both assertion statements
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            # check correct error is raised
            self.assertRaises(InputReaderError, self.obj.readFile, filePath)
            try:
                # check that correct error message is reported
                self.obj.readFile(filePath)
            except Exception as error:
                print(error)
                self.assertTrue(expected_error in str(error))


    def test_shouldRaiseExceptionWhenInitialOrientationIsNotValid(self):
        # Given
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 X\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        expected_error = "Orientation should be a single letter in ['N','S','E','W']"
        # mocking is done for both assertion statements
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            # check correct error is raised
            self.assertRaises(InputReaderError, self.obj.readFile, filePath)
            try:
                # check that correct error message is reported
                self.obj.readFile(filePath)
            except Exception as error:
                print(error)
                self.assertTrue(expected_error in str(error))


    def test_shouldRaiseExceptionWhenAnMovementCommandIsNotValid(self):

        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRXMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'
        expected_error = "is not valid Movement Command"
        # mocking is done for both assertion statements
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            # check correct error is raised
            self.assertRaises(InputReaderError, self.obj.readFile, filePath)
            try:
                # check that correct error message is reported
                self.obj.readFile(filePath)
            except Exception as error:
                print(error)
                self.assertTrue(expected_error in str(error))


if __name__ == '__main__':
    print('Testing Input Reader Validation Test')
    unittest.main()
