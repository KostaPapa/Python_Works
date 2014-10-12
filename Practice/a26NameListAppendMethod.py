CONTINUE_PROG = 'Y'


def emptyList():
    '''This funtion will create an empty list.'''

    nameList = []

    return nameList

def addUserNames(nameList):
    '''This funtion will add the user name to the list.'''


    
    CONTINUE_PROG = raw_input("If u want to countinue type Y otherwise type n:")
    
    while CONTINUE_PROG == 'Y':

        name = str(raw_input("Enter name: "))
        
        nameList.append(name)

        CONTINUE_PROG = raw_input("If u want to countinue type Y otherwise type n:")

    return nameList

def displayNames(nameList):
    '''This funtion will return the names written by the user.'''

    for names in nameList:
        print names

def main():
    
    emptyNameList = emptyList()
    fullNameList = addUserNames(emptyNameList)  
    displayNames(fullNameList)

main()
