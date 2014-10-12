def getStudentScore():
    '''This funtion will get the studetn scores.'''

    score = float(raw_input("Enter studetn score: "))

    return score

def calcLetterGrade(score):
    '''This function will calc the letter grade.'''

    if (81 <= score <= 90):
        print "A"

    elif (71 <= score <= 80):
        print "B"

    elif (61 <= score <= 70):
        print "C"

    elif (51 <= score <= 60) :
        print "D"
    else:
        print "F"

    
def main():
    
    studentScore = getStudentScore()
    calcLetterGrade(studentScore)

main()
