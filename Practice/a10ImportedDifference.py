''' 
cs1114 

Submission: Assignment (Private)

Programmer: Kostaq Papa
Username: kpapa01

Purpose of program: This program will calculate the differenc of two numbers. One will be imported and one will be asked the user to enter.
Assumptions: The user will type what I ask for.
Constraints: I dont know what a f*** this mean.

'''


def enterbelowPayement():
    '''This function will ask the user to enter the below payment number.'''

    downPayement = float (raw_input ("Please, enter the below payment number: "))

    return downPayement

def calcTheSubstruction(total, downPayement):

    due = total - downPayement

    print "Did you know that the differenc between %.2f and %.2f is %.2f. " %(total, downPayement, due)

def main():

    importedTotal, underPayement = enterbelowPayement()
    calcTheSubstruction (importedTotal, underPayement)

main ()
    
