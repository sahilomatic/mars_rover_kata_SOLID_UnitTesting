class OutputFileController:
    """Class to Output file Handling"""
    def processFile(self, file_path,line_list):
        """
            Return an Output file with current Position
        :param str file_path: Folder path of Input File
        :return: Generates Output File with current Position of Rover.
        :raises InputReaderError: if input file instruction is not valid
        :raises Exception: if any error is generated
        """

        with open(file_path, 'w') as f:
            for item in line_list:
                f.write("%s\n" % item)
