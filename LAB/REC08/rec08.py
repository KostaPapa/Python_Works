"""

User Name: kpapa01

Programmer: Kostaq Papa

Purpose of this program: Calc thr weighted score.

Constrains: 


"""

PERCENTAGE_OF_EACH_HW = [0.0025, 0.025, 0.015, 0.02, 0.035, 0.045, 0.05]


def studentGrade():
    '''This function will bulid a list of classes.'''

    studentScore = [0] * 7
       
    
    weightedScore = [0] * 7

    for score in range(len(studentScore)):
        studentScore[score] = int(raw_input ("Enter the student score: "))


    for score in range(len(weightedScore)):
        weightedScore[score] = (studentScore[score] * PERCENTAGE_OF_EACH_HW[score])

    return weightedScore
        
def studentInfo(weightedScore):
    '''This function will create a list of student information.'''

    studentInfo = [0] * 2
        
    studentInfo.append(weightedScore)
    studentInfo.remove(0)
    
    studentID = raw_input("Enter the student ID: ")
    studentInfo.insert(2, studentID)
    studentInfo.remove(0)
    

    return studentInfo

def gradClasses(studentInfo):
    '''This function will give information for a class.'''

    studentClassInfo = [0] * 3

    studentName = raw_input("Enter student name: ")
    studentClassInfo.append(studentName)
    studentClassInfo.remove(0)
    
    studentClass = raw_input ("Enter the student class number: ")
    studentClassInfo.insert(0, studentClass)
    studentClassInfo.remove(0)
    
    studentClassName = raw_input ("Enter the student class name: ")
    studentClassInfo.insert(0, studentClassName)
    studentClassInfo.remove(0)
    

    return studentClassInfo

def classNames(studentClassInfo):
    '''This function will build a list of grad classes.'''

    
    gradClasses = [0] * 1
    
    studentClassName = raw_input("Please, enter the class number: ")
    gradClasses.insert(0, studentClassName)
    gradClasses.remove(0)
    print "The list of the grad classes is: "
    print gradClasses

    


def main():

    scoresOfStudent = studentGrade()
    classOfGradStudent = studentInfo(scoresOfStudent)
    nameOfClass = gradClasses(classOfGradStudent)
    classNames(nameOfClass)
    
main()
