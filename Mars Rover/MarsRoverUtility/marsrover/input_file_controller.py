from marsrover.rover import Rover
from typing import List
from marsrover.input_reader import InputReader
from customErrors.input_reader_error import InputReaderError


class InputFileController:

    """Class to run business logic for each rover"""

    def processFile(self, file_path):
        """
            Return an Output file with current Position
        :param str file_path: Folder path of Input File
        :return: Generates Output File with current Position of Rover.
        :raises InputReaderError: if input file instruction is not valid
        :raises Exception: if any error is generated
        """



        rovers_current_poistion= []
        reader = InputReader()

        # Read Input File and create a list of instruction to be executed for each Rover
        # in list of rovers
        set_of_instructions = reader.readFile(file_path)
        for instruction in set_of_instructions.roverInstructions:
            #create rover object for 1 rover
            rover = Rover(set_of_instructions.plateau, instruction.initialPosition)
            # run instruction commands for selected rover
            rover.processCommands(instruction.movementCommands)
            # Append final position of rover in output list
            rovers_current_poistion.append(rover.currentPosition.toString())

        return rovers_current_poistion



