'''

Programmer: Kostaq Papa

Level: Private

Type: Lab Work

'''

EXIT = 'STOP PROCESSING STUDENTS'

PERCENTAGE_OF_EACH_HW = [0.0025, 0.025, 0.015, 0.02, 0.035, 0.045, 0.05, 0.06, 0.08, 0.18, 0.20, 0.30]
ABSENT = 0



def getStudentInfo():
    '''This function will get last and first name of the student and their id.'''
    
    studentLastName = raw_input("Please, enter the student's last name: ")
    studentFirstName = raw_input("Please, enter the student's first name: ")
    studentID = int(raw_input("Please, enter the student's ID: "))
    print "The ID you entered, matched with the student last name and first name."

    return studentLastName, studentFirstName, studentID

def testInfoWorng(studentLastName,studentFirstName,studentID):
    '''This function will test if the information is entered correctly.'''

    while (studentLastName == studentFirstName):

        print "The name of the student is entered correctly."
        studentLastName = raw_input("Please, enter the correct student's last name: ")
        studentFirstName = raw_input("Please, enter the correct student's first name: ")

    while (firstNumber != 0):
        print "You entered a worng ID numeber."
        print "The student's ID should begin with the number 0."
        studentID = int(raw_input("Please, enter the correct student's ID: "))

    while (len(studentID) !=7):
        print "You entered a worng ID number."
        print "The student's ID should be 7 number."

        studentID = int(raw_input("Please, enter the correct student's ID: "))
    

    
def getStudentScore():
    '''This function will get the student scores.'''

    studentScore = [0] * len(PERCENTAGE_OF_EACH_HW)

    for item in range(len(studentScore)):
        if (studentScore[item] == 'absent'):
            studentScore = 0
        else:
            studentScore[item] = int (raw_input ("Please, enter the student scores: "))

    return studentScore

def calcScore(studentScore):

    weightedScore = [0] * len(PERCENTAGE_OF_EACH_HW)

    for item in range (len(weightedScore)):

        weightedScore[item] = (studentScore[item] * PERCENTAGE_OF_EACH_HW[item])

        print weightedScore 
    
    

def main():

    surName, name, ID = getStudentInfo()
    testInfoWorng(surName, name, ID)
    scoreOfStudent = getStudentScore()
    calcScore(scoreOfStudent)

main()
