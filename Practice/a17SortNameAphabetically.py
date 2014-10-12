def getNames():
    '''This funtion will ask the user to enter the names.'''

    nameOne = raw_input ("Enter name(last name than first name): ")
    nameTwo = raw_input ("Enter name(last name than first name): ")

    return nameOne, nameTwo

def printApfabetically(nameOne, nameTwo):
    '''This funtion will ptint the names Apabetically.'''

    if (nameOne < nameTwo):
        print nameOne
        print nameTwo
    else:
        print nameTwo
        print nameOne


def main():

    first, second = getNames()
    printApfabetically(first, second)

main()
