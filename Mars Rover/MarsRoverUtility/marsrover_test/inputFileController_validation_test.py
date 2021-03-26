from mock import patch, mock_open
from marsrover.input_file_controller  import InputFileController
from marsrover.input_reader import InputReader
import unittest
from customErrors.input_reader_error import InputReaderError

class Test_InputFileController(unittest.TestCase):
    # first function to run for initializing data
    def setUp(self):


        self.input_file_path = 'testFiles/inputFile.txt'
        self.input_file_controller_obj = InputFileController()



    def test_shouldCalculateFinalPositionForOneRover(self):
        """
        Test when 1 rover details are given in input file
        :return:
        """

        # Custom Input
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRMMRMRRM'


        # mocking is done to avoid time expensive input output operations
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):

            output = self.input_file_controller_obj.processFile(filePath)

        #output is a lsit
        lastPrintedLine = output[0]

        expectedFinalPosition = "5 1 E"
        self.assertEqual(lastPrintedLine,expectedFinalPosition)


    
    def test_shouldCalculateFinalPositionForFourRovers(self):
        """
        Test case to check, when datat related to 4 rovers is given
        :return:
        """
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM\n1 2 N\nLMLMLMLMM'

        inputFileController2 = InputFileController()

        # mocking is done to avoid time expensive input output operations
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            output = inputFileController2.processFile(filePath)


        expectedFinalPosition = ["5 1 E","3 4 N","1 2 N","1 3 N"]
        self.assertEqual( output,expectedFinalPosition)


    def test_shouldPrintAnErrorWhenPlateauDimensionsAreNotValid(self):
        """
        test to check if InputReaderError error is raised when plateau dimension is false
        :return:
        """

        # Custom Input
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = 's 5\n3 3 E\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'
        expected_error = 'plateau X-Y coordinates should be positive integer'

        # check error is raise
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            # check that error type InputReaderError is raised
            self.assertRaises(InputReaderError,self.input_file_controller_obj.processFile,filePath)

            try:
                # check that correct error message is reported when plateau dimension is not correct
                self.input_file_controller_obj.processFile(filePath)
            except Exception as error:

                self.assertTrue(expected_error in str(error))








    def test_shouldPrintAnErrorWhenRoverInitialPositionIsNotValid(self):
        "test if validation works when Initial Position of rover is not valid"
        # Custom Input
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 s E\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        expected_error = 'invalid literal'

        # mocking is done to avoid i/o execution time for  both assertion statemen
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            self.assertRaises(ValueError, self.input_file_controller_obj.processFile, filePath)
            try:
                # check that correct error message is reported when plateau dimension is not correct
                self.input_file_controller_obj.processFile(filePath)
            except ValueError as error:

                self.assertTrue(expected_error in str(error))




    def test_shouldPrintAnErrorWhenRoverInitialOrientationIsNotValid(self):
        "test if validation works when rover initial orientation is not valid"
        # Custom Input
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 X\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        errorMessage = "Orientation should be a single letter in ['N','S','E','W']"

        # mocking is done to avoid i/o execution time for  both assertion statemen
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            self.assertRaises(InputReaderError, self.input_file_controller_obj.processFile, filePath)
            try:
                # check that correct error message is reported when plateau dimension is not correct
                self.input_file_controller_obj.processFile(filePath)
            except InputReaderError as error:

                self.assertTrue(errorMessage in str(error))


def test_shouldPrintAnErrorWhenAnMovementCommandIsNotValid(self):
        "test when movement command is not valid"
        # Custom Input
        filePath = 'somePathToFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRXMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'


        expected_error = "is not valid Movement Command"

        # mocking is done to avoid i/o execution time for  both assertion statemen
        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            self.assertRaises(InputReaderError, self.input_file_controller_obj.processFile, filePath)
            try:
                # check that correct error message is reported when plateau dimension is not correct
                self.input_file_controller_obj.processFile(filePath)
            except InputReaderError as error:

                self.assertTrue(expected_error in str(error))

if __name__ == '__main__':
    print('Testing Input File Controller Validation Test')
    unittest.main()