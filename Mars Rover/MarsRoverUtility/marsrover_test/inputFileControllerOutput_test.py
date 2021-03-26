from marsrover.input_file_controller import InputFileController

import unittest
from configparser import ConfigParser

class Test_InputFileController(unittest.TestCase):
    # first function to run for initializing data
    def setUp(self):
        # Fetch input file path from config.ini file and assign it to variable input_file
        #config = ConfigParser()
        #config.read('../config.ini')

        self.input_file_path = 'testFiles/inputFile.txt'
        self.input_file_controller_obj = InputFileController()


    def test_calculateFinalPosition(self):





        printedOutput = self.input_file_controller_obj.processFile(self.input_file_path)
        print(printedOutput)

        # Assertion Statement
        expectedOutput= ['1 3 N', '5 1 E']
        self.assertEqual(expectedOutput,printedOutput)


if __name__ == '__main__':
    print('Testing Input File Controller Output Test')
    unittest.main()