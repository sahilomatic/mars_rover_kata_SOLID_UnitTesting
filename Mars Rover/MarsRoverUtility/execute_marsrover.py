from marsrover.input_file_controller import InputFileController
from configparser import ConfigParser
from marsrover.output_file_controller import OutputFileController
from customErrors.input_reader_error import InputReaderError


def main():
    """
    This function serves as starting point of rover project
        """
    input_file_controller = InputFileController()

    # Fetch input file path from config.ini file and assign it to variable input_file
    config = ConfigParser()
    config.read('config.ini')
    try:
        input_file = config.get('input', 'input_path')
        rovers_current_position  = input_file_controller.processFile(input_file)

        outut_file = config.get('output', 'output_path')
        OutputFileController().processFile(outut_file,rovers_current_position)
        print('Please check Output Folder for Results')
    except InputReaderError as error:
        print("Error", error)
    except ValueError as error:

        print("Error", error)
    except Exception as error:

        print("Error", error)


if __name__ == '__main__':
    main()
