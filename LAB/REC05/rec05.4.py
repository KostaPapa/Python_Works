def EnterNumberandCharacter():
    '''This function will draw a tringle.'''

    userNumber = int(raw_input ("Please, enter a number:"))
    userCharacter = raw_input ("Please, enter a character:")


    return userNumber, userCharacter


def drawTriangle (userNumber, userCharacter):
    
    for n in range(0, (userNumber/2), 1):

        print userCharacter * (n + 1)

    for n in range((userNumber/2), 0, -1):

        print userCharacter * (n - 1)



def main():

    Number, Character = EnterNumberandCharacter()
    drawTriangle(Number, Character)

main()
