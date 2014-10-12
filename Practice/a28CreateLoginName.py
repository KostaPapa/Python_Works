def getStudentFirstName():

    firstName = raw_input("Enter first name: ")

    return firstName

def getStudentLastName():

    lastName = raw_input ("Enter last name: ")

    return lastName

def getStudentIDnum():

    idNum = raw_input("Enter id num: ")

    return idNum

def createLoginName(firstName, lastName, idNum):

    threeFirstNameLetter = firstName[0:3]
    threeLastNameLetter = lastName[0:3]
    threeIDnoDigits = idNum[0:3]

    print "Your login name is: " + threeFirstNameLetter + threeLastNameLetter + threeIDnoDigits

def main():

    name = getStudentFirstName()
    surname = getStudentLastName()
    idNumber = getStudentIDnum()
    createLoginName(name, surname, idNumber)

main()

    
