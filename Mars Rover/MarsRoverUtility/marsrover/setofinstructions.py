


class SetOfInstructions:
    '''Class to store plateau dimension and list of rover instructions'''

    def __init__(self, plateau, roverInstructions):
        '''
        Assi plateau dimension and list of intructions given to rovers
        :param plateau: Plateau
        :param roverInstructions: list
        '''
        self.plateau = plateau
        self.roverInstructions = roverInstructions

    def toString(self):
        roverInstructionsAsStrings = []
        for instruction in self.roverInstructions:
            roverInstructionsAsStrings.append(instruction.toString())
        return self.plateau.toString() + '\n' + '\n'.join(roverInstructionsAsStrings)
