"""

User Name: kpapa01

Programmer: Kostaq Papa

Purpose of this program: Calc thr weighted score.

Constrains: 


"""
PERCENTAGE_OF_EACH_HW = [0.0025, 0.025, 0.015, 0.02, 0.035, 0.045, 0.05, 0.06, 0.08, 0.18, 0.20, 0.30]


    

def getStudentScore():
    '''Will the student score.'''
    studentScore = [0] * 12

    for item in range(len(studentScore)):
        studentScore[item] = int (raw_input("Enter the score: "))

    return studentScore

def calcWeightedScore(studentScore):
    '''Will calc the weighted score.'''

    weightedScore = [0] * 12


    for item in range(len(weightedScore)):
        weightedScore[item] = (studentScore[item] * PERCENTAGE_OF_EACH_HW[item])
    print "\nThe weighted score are: "    
    print weightedScore

    total = 0
    for item in range (len(weightedScore)):
        total += weightedScore[item]
    print "The total is: " , total
    
    return total
    
def calcLetterGrade(total):
    '''Will calc the letter grade.'''

    if float(100 >= total >= 90):
        print 'The student grade is A'
    elif float(89 >= total >=80):
        print 'The student grade is B'
    elif float(79 >= total >= 70):
        print 'The student grade is C'
    elif float(69 >= total >= 60):
        print 'The studetn grade is D'
    else:
        print "STUDENT FAILED THE COURSE..."

        

def displayResult():
    '''Will display the result.'''

def main():

    scoreOfStudent = getStudentScore()
    totalGrade = calcWeightedScore(scoreOfStudent)
    calcLetterGrade(totalGrade)
    displayResult()

main()
