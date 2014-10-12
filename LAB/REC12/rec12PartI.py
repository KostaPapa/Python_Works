"""

User Name: kpapa01

Programmer: Kostaq Papa

Purpose of this program: Create a class module.

"""


class HydroCarbyMolly:
    '''Creates a molecule of Carbon and Hydrogen.'''

    def __init__(self, nOofCarbon, nOofHydrogen, moleculeName):

        self.__carbonAtoms = nOofCarbon
        self.__hydrogenAtoms = nOofHydrogen
        self.__hydroCarbonName = moleculeName

    def __str__(self):
        '''Will print in a nice format the name and formula of the molecule.'''

        return '\nFormula - ' + 'C' + self.__carbonAtoms + 'H' + self.__hydrogenAtoms + '\nName - ' + self.__hydroCarbonName



    
