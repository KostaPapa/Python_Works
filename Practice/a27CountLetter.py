def getUserInput():

    userString = raw_input("Write a name: ")

    return userString

def countLetterA(userString):

    countLetter = 0

    for char in userString:
        if ((char == 'A') or (char == 'a')):
            countLetter += 1

    print "The letter A or a appears " + str(countLetter) + " times"

def main():

    string = getUserInput()
    countLetterA(string)
    
main()
