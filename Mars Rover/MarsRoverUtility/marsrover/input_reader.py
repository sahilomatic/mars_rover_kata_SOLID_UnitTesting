from marsrover.rover import RoverPosition, Rover
from marsrover.plateau import Plateau
from marsrover.instruction import RoverInstruction
from marsrover.setofinstructions import SetOfInstructions

from customErrors.input_reader_error import InputReaderError





class InputReader:
    """Class to read Input Files and Perform Validations"""



    def readFile(self, file_path):
        """
            1)Function to read input file
            2) Read input file and assign plateau size
            3) Read input file and assign starting position of rover
            4) Read input file and assign instruction for rover
        :param str file_path: Folder path of Input File
        :return: Return object of type SetOfInstructions containing info regarding
         plateau dimension and list of all instructions given to rover
        :rtype:  SetOfInstructions
        :raises InputReaderError: if input file instruction is not valid
        :raises Exception: if any error is generated
        """

        # with context is used so file is closed after scope
        with open(file_path, 'r') as inputFile:
            plateau_input_line = inputFile.readline()
            plateau = self.readPlateauInput(plateau_input_line)

            rover_instructions = []
            # As 1st line is Plateau dimesnion , start from index 1
            for line_count, line in enumerate(inputFile, start = 1):

                # starting from row 2 of input file(index 1) ; odd lines contain initial poistion
                # and even lines contain infor regarding movement
                if line_count % 2 != 0:
                    # read initial position and set
                    rover_initial_position = self.readInitialPosition(line)

                else:
                    # and even lines contain info  regarding movement and store it in Rover Instruction list
                    rover_instruction = RoverInstruction(rover_initial_position, self.readMovementCommands(line))

                    rover_instructions.append(rover_instruction)
        # return list of instruction of all rovers ; will run 1 by 1 in parent function
        return SetOfInstructions(plateau, rover_instructions)

    def validateMovementCommands(self,command):
        allowed_commands  = 'LRM'
        if(not command in allowed_commands):
            raise InputReaderError(str(command)+" is not valid Movement Command")

    def readMovementCommands(self, line):

        # line is split into a list of char; representing each command
        commands_to_move_rover = []
        # strip new line char from each line
        for command in list(line.strip('\n')):
            self.validateMovementCommands(command)
            commands_to_move_rover.append(command)

        return commands_to_move_rover


    def validateRoverPosition(self,start_poistion):
        """
                Validate start position
                :param str start_poistion: Start Position of Rover
                :return: Return list of starting position of rover and it's orientation
                :rtype:  list
                :raises InputReaderError: if input is not valid

                """

        input_string_as_list = start_poistion.split()
        orientation = None
        # check if length is 3
        if (len(input_string_as_list) == 3):
            # run for all element except last, which is for orientation
            for i in input_string_as_list[0:1]:
                # check if both element in string are digits

                if (not i.isdigit()):

                    raise InputReaderError("X-Y coordinates should be positive integer")


            orientation = input_string_as_list[2]
            if(not (len(orientation)==1 and  orientation in 'NSEW')):
                raise InputReaderError("Orientation should be a single letter in ['N','S','E','W']")
        else:
            raise InputReaderError("rover position should be in X-Y coordinates and orientation in NSEW")
        return (input_string_as_list[0] ,input_string_as_list[1] ,orientation)

    def readInitialPosition(self, line):
        """
        Validate line and return Initial position
        :param line:
        :return: Initial RoverPosition
        :rtype : RoverPosition
        """

        x_axis ,y_axis , orientation = self.validateRoverPosition(line)


        return RoverPosition(int(x_axis),
                             int(y_axis),
                             orientation)


    def validatePlateauInput(self, plateau_dimension):
        """
        Validate Plateau dimension
        :param str plateau_dimension: First Line of Input File
        :return: Return list of digits containing info regarding
         dimension of plateau
        :rtype:  list
        :raises InputReaderError: if input plateau dimension is not valid

        """

        input_string_as_list = plateau_dimension.split()
        # check if length is 2
        if(len(input_string_as_list)==2):
            for i in input_string_as_list:
                #check if both element in string are digits
                if(not i.isdigit()):
                    raise InputReaderError("plateau X-Y coordinates should be positive integer")
        else:
            raise InputReaderError("plateau dimensions should be in X-Y coordinates")
        return input_string_as_list


    def readPlateauInput(self, plateau_dimension):
        """
        Calls Validate Plateau dimension fnction
        :param str plateau_dimension: First Line of Input File
        :return: Return object of type Plateau containing info regarding
         dimension of plateau
        :rtype:  Plateau
        :raises InputReaderError: if input file instruction is not valid

        """
        input_string_as_list = self.validatePlateauInput(plateau_dimension)
        return Plateau(int(input_string_as_list[0]), int(input_string_as_list[1]))
