def getANumber():
    '''This funtion will get a number from 1 to 10.'''

    userNumber = int (raw_input("Enter a number(must be 1 to 10): "))

    return userNumber

def assingRomakNumber(userNumber):
    '''This number will give a romak number to the user enterd number.'''

    if (userNumber == 1):
        print "I"
    elif (userNumber == 2):
        print "II"
    elif (userNumber == 3):
        print "III"
    elif (userNumber == 4):
        print "IV"
    elif (userNumber == 5):
        print "V"
    elif (userNumber == 6):
        print "VI"
    elif (userNumber == 7):
        print "VII"
    elif (userNumber == 8):
        print "VIII"
    elif (userNumber == 9):
        print "IX"
    elif (userNumber == 10):
        print "X"
    else:
        print "You number is out of range..."
        
def main():
    number = getANumber()
    assingRomakNumber(number)
main()
