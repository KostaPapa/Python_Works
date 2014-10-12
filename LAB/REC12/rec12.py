'''

User Name: kpapa01

Programmer: Kostaq Papa

Purpose of this program: Will print the molecules in the format defined in molecule class.
Assumption : There will be at least one Carbon atom and 1 Hydrogen atom in a molecule.
             The max number of atoms that a Carbon or Hydrogen can have is a 3 digit number

'''

NUMBERS = "0,1,2,3,4,5,6,7,8,9"     # Will be used to locate the digits (# of atoms) in the molecule formula.


import rec12PartI

def displayMolecules():
    '''This function will use the imported HydroCarbyMolly class to display the molecules.'''

    moleculesFilename = open('moleculesFile.txt','r')
    
    for lines in moleculesFilename:

        splitedLineLists = lines.split()
        moleculeName = splitedLineLists[0]
        moleculeFormula = splitedLineLists[1]

        
        if ((moleculeFormula[1] in NUMBERS) and (moleculeFormula[2] in NUMBERS) and (moleculeFormula[3] in NUMBERS)):
            if ((len(moleculeFormula)) == 8):
                threeDigitCarbonAndHydro = rec12PartI.HydroCarbyMolly((moleculeFormula[1] + moleculeFormula[2] + moleculeFormula[3]), (moleculeFormula[-3] + moleculeFormula[-2] + moleculeFormula[-1]), moleculeName)
                print threeDigitCarbonAndHydro
                
            elif ((len(moleculeFormula)) == 7):
                threeDigitCarbonAndTwoDigitHydro = rec12PartI.HydroCarbyMolly((moleculeFormula[1] + moleculeFormula[2] + moleculeFormula[3]), (moleculeFormula[-2] + moleculeFormula[-1]), moleculeName)
                print threeDigitCarbonAndTwoDigitHydro

            else: # ((len(moleculeFormula)) == 6)
                threeDigitCarbonAndOneDigitHydro = rec12PartI.HydroCarbyMolly((moleculeFormula[1] + moleculeFormula[2] + moleculeFormula[3]), moleculeFormula[-1], moleculeName)
                print threeDigitCarbonAndOneDigitHydro
                
        elif ((moleculeFormula[1] in NUMBERS) and (moleculeFormula[2] in NUMBERS)):
            if ((len(moleculeFormula)) == 7):
                twoDigitCarbonAndThreeDigitHydro = rec12PartI.HydroCarbyMolly((moleculeFormula[1] + moleculeFormula[2]), (moleculeFormula[-3] + moleculeFormula[-2] + moleculeFormula[-1]), moleculeName)
                print twoDigitCarbonAndThreeDigitHydro

            elif ((len(moleculeFormula)) == 6):
                twoDigitCarbonAndHydro = rec12PartI.HydroCarbyMolly((moleculeFormula[1] + moleculeFormula[2]), (moleculeFormula[-2] + moleculeFormula[-1]), moleculeName)
                print twoDigitCarbonAndHydro

            else: # ((len(moleculeFormula)) == 5):
                twoDigitCarbonAndOneDigitHydro  = rec12PartI.HydroCarbyMolly((moleculeFormula[1] + moleculeFormula[2]), moleculeFormula[-1], moleculeName)
                print twoDigitCarbonAndOneDigitHydro
                
        else : #(moleculeFormula[1] in NUMBERS)
            if ((len(moleculeFormula)) == 6):
                oneDigitCarbonAndThreeDigitHydro  = rec12PartI.HydroCarbyMolly(moleculeFormula[1], (moleculeFormula[-3] + moleculeFormula[-2] + moleculeFormula[-1]), moleculeName)
                print oneDigitCarbonAndThreeDigitHydro

            elif ((len(moleculeFormula)) == 5):
                oneDigitCarbonAndTwoDigitHydro = rec12PartI.HydroCarbyMolly(moleculeFormula[1], (moleculeFormula[-2] + moleculeFormula[-1]), moleculeName)
                print oneDigitCarbonAndTwoDigitHydro

            else : #((len(moleculeFormula)) == 5)
                oneDigitCarbonAndHydro = rec12PartI.HydroCarbyMolly(moleculeFormula[1], moleculeFormula[-1], moleculeName)
                print oneDigitCarbonAndHydro

        
    moleculesFilename.close()

    
            
def main():

    displayMolecules()
    
main()
    
    

    
