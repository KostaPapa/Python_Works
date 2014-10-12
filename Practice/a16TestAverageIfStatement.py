TOTAL_TEST_GIVEN = 3.0
CONGRATULATION_AVERAGE = 95

def getStudentScores():
    '''This funtoin will get the student scores.'''

    firstTest = int(raw_input("Enter your first test scores: "))
    secondTest = int(raw_input("Enter your second test scores: "))
    thirdTest = int(raw_input("Enter your third test scores: "))

    return firstTest, secondTest, thirdTest

def calcAverage(firstTest, secondTest, thirdTest):
    '''This function will calc the average of the student.'''

    average = (firstTest + secondTest + thirdTest)/TOTAL_TEST_GIVEN

    print "Your average is: ",average

    return average

def congratulate(average):
    '''This function will congratulate students who have an average over 95.'''

    if (average >= CONGRATULATION_AVERAGE):
        print "WELL DONE!"
    else:
        print "TRY HARDER!"
    
def main():

    firstScores, secondScores, thirdScores = getStudentScores()
    studentAverage = calcAverage(firstScores, secondScores, thirdScores)
    congratulate(studentAverage)

main()
