#!C:\Users\kpapa01\Desktop\Python\hw\hw02.exe

''' 
cs1114 

Submission: hw02

Programmer: Kostaq Papa
Student ID: 0412768
Username:   kpapa01

Purpose of program: This program will calculate the tuition and the university fees that an undergraduate student has to pay each semester at Builtin Research Institute of NYU (BRINY-U).

Assumptions:    The user will enter only one name when prompted for a name.
                The user will not enter any leading zeros when prompted for ID.
                The user will enter only M for male or F for female when prompted for gender.
                The user will enter only Y for yes or N for no when prompted for "any remedial courses?".
                The user will enter only positive integer values when prompted for the number of credits being taken.
                The user will not include any remedial courses when they enter the number of credits being taken.

'''




MIN_FULLTIME_CREDITS = 12                       # The minimum inclusive number of credits for a full time student.
MAX_FULLTIME_CREDITS = 20                       # The maximum inclusive number of credits for a full time student.
MAX_NUMBER_OF_CREDITS = 30                      # The maximum number of credit that a student can take.
FULL_TIME_TUITION = 14000.00                    # The regular tuition, per semester, for a student taking 12 to 20 (inclusive) credits.   
EXTRA_TUITION_PER_CREDIT_IN_EXCESS = 800.00     # The extra tuition, per credit, for a student taking more than 20 credits, for each credit in excess of 20.
PART_TIME_TUITION = 900.00                      # The part time student tuition.
REMEDIAL_COURSE_TUITION = 3000.00               # The tuition for each remedial course.
UNIVERSITY_FEE = 100.00                         # The university fee.
UNIVERSITY_FEE_PER_CREDIT = 30.00               # The university fee per each credit taken.
EXIT_PROGRAM = 'END OF PROCESSING'              # The name used to stop processing students and exit the program.
MALE_GENDER = 'M'                               # Referes to male gender when the user is asked to enter his gender.
FEMALE_GENDER = 'F'                             # Referes to female gender when the user is asked enter her gender.
PERCENTAGE = 100                                # Is used to calculate the percentage of certain mathematical expressions.


def drawBRINYU():
    '''This function will draw WELCOME TO BRINY-U.'''

    print "\nBRBRBR------------------------BRBRBR \nBRBRBR   WELCOME TO BRINY-U   BRBRBR \nBRBRBR------------------------BRBRBR \n"

def getLastName ():
    '''This function will get the last name of the student.'''

    lastName = raw_input ("Please, enter your last name: ")

    return lastName

def getFirstName():
    '''This function will get the student first name.'''
    
    firstName = raw_input("Please, enter your first name: ")

    return firstName

def getStudentBrinyUid ():
    '''This function will get the student BRINY-U ID number.'''

    idNumber = raw_input ( "Please, enter your BRINY-U ID number (without any leading zeros): ")

    return idNumber

def getUserGender ():
    '''This function will get the user gender.'''

    gender = raw_input ("Please, enter your gender (enter M for male and F for female): ")

    return gender        
           
def userRemedialCourses ():
    '''This function will ask the student if he/she is taking remedial courses.'''

    remedialCourses = raw_input ("Are you taking any remedial courses (enter Y for yes or N for no)? ")

    return remedialCourses

def testForRemedialCourses (remedialCourses):
    '''This function will get the number of remedial courses to only those students who attend remedial courses.'''

    if ( remedialCourses == 'Y' ) :

        numberOfRemedialCourses = int (raw_input ("Please, enter the number of remedial courses: "))

        return numberOfRemedialCourses
    
def getAndTestNumberOfCredits():
    '''This function will get the number of credits and will test if that number is correct.'''

    numberOfCredits = int (raw_input("Please, enter the number of credits: "))

    while (numberOfCredits > MAX_NUMBER_OF_CREDITS):

        print "You entered an incorrect number of credits. Students are not allowed to take more than %i credits" %(MAX_NUMBER_OF_CREDITS)

        numberOfCredits = int (raw_input ("Please, enter again your number of credits: "))

    return numberOfCredits
    

def calcOfTuitionFeeAndOwe (numberOfCredits, firstName, lastName, numberOfRemedialCourses, remedialCourses, idNumber):
    '''This function will calculate the tutition of the student.'''

    
    
    if ( (numberOfCredits < MIN_FULLTIME_CREDITS) and (remedialCourses == 'Y')):

        remedialcoursefee = numberOfRemedialCourses * REMEDIAL_COURSE_TUITION
        tuition = (numberOfCredits * PART_TIME_TUITION) + remedialcoursefee
        fee = UNIVERSITY_FEE + (UNIVERSITY_FEE_PER_CREDIT * numberOfCredits)
        owe = tuition + fee

        print "Mr." + firstName + " " + lastName + "(" + idNumber + ")"
        print "Your tuition is: $ %.4f"   %(tuition)
        print "Your fee is: $ %.4f"        %(fee)
        print "You have to pay a total of: $ %.4f" %(owe)

    elif ((numberOfCredits < MIN_FULLTIME_CREDITS) and (remedialCourses != 'Y')):

        tuition = numberOfCredits * PART_TIME_TUITION
        fee = UNIVERSITY_FEE + (UNIVERSITY_FEE_PER_CREDIT * numberOfCredits)
        owe = tuition + fee

        print "Mr." + firstName + " " + lastName + "(" + idNumber + ")"
        print "Your tuition is: $ %.4f"   %(tuition)
        print "Your fee is: $ %.4f"        %(fee)
        print "You owe is: $ %.4f" %(owe)

    elif ((MIN_FULLTIME_CREDITS <= numberOfCredits <= MAX_FULLTIME_CREDITS) and (remedialCourses == 'Y')):

        remedialcoursefee = numberOfRemedialCourses * REMEDIAL_COURSE_TUITION
        tuition = FULL_TIME_TUITION + remedialcoursefee
        fee = UNIVERSITY_FEE + (UNIVERSITY_FEE_PER_CREDIT * numberOfCredits)
        owe = tuition + fee

        print "Mr." + firstName + " " + lastName + "(" + idNumber + ")"
        print "Your tuition is: $ %.4f"   %(tuition)
        print "Your fee is: $ %.4f"        %(fee)
        print "You owe is: $ %.4f" %(owe)

    elif ((MIN_FULLTIME_CREDITS <= numberOfCredits <= MAX_FULLTIME_CREDITS) and (remedialCourses != 'Y')):

        tuition = FULL_TIME_TUITION
        fee = UNIVERSITY_FEE + (UNIVERSITY_FEE_PER_CREDIT * numberOfCredits)
        owe = tuition + fee

        print "Mr." + firstName + " " + lastName + "(" + idNumber + ")"
        print "Your tuition is: $ %.4f"   %(tuition)
        print "Your fee is: $ %.4f"        %(fee)
        print "You owe is: $ %.4f" %(owe)

    elif ((MAX_FULLTIME_CREDITS <= numberOfCredits <= MAX_NUMBER_OF_CREDITS) and (remedialCourses == 'Y')):

        creditInExcess = numberOfCredits - MAX_FULLTIME_CREDITS
        remedialcoursefee = numberOfRemedialCourses * REMEDIAL_COURSE_TUITION
        tuition = FULL_TIME_TUITION + (creditInExcess * EXTRA_TUITION_PER_CREDIT_IN_EXCESS) + remedialcoursefee
        fee = UNIVERSITY_FEE + (UNIVERSITY_FEE_PER_CREDIT * numberOfCredits)
        owe = tuition + fee

        print "Mr." + firstName + " " + lastName + "(" + idNumber + ")"
        print "Your tuition is: $ %.4f"   %(tuition)
        print "Your fee is: $ %.4f"        %(fee)
        print "You owe is: $ %.4f" %(owe)

    else:

        creditInExcess = numberOfCredits - MAX_FULLTIME_CREDITS
        tuition = FULL_TIME_TUITION + (creditInExcess * EXTRA_TUITION_PER_CREDIT_IN_EXCESS)
        fee = UNIVERSITY_FEE + (UNIVERSITY_FEE_PER_CREDIT * numberOfCredits)    
        owe = tuition + fee

        print "Mr." + firstName + " " + lastName + "(" + idNumber + ")"
        print "Your tuition is: $ %.4f"   %(tuition)
        print "Your fee is: $ %.4f"        %(fee)
        print "You owe is: $ %.4f" %(owe)

    return owe



def main ():
   
    print "Enter the next last name of a student, or type, END OF PROCESSING, to stop process students. \n"

    drawBRINYU()
    surname = getLastName()

    totalUsersRegistered = 0
    countMaleUsers = 0
    countFemaleUsers = 0
    totalAmountOwed = 0
    
        
    while (surname != EXIT_PROGRAM):     

        name = getFirstName ()
        totalUsersRegistered = totalUsersRegistered + 1
        
        brinyID = getStudentBrinyUid ()
        
        theEnteredGender = getUserGender()
        if (theEnteredGender == MALE_GENDER):
            countMaleUsers = countMaleUsers + 1           
           
        else:
            countFemaleUsers = countFemaleUsers + 1

        totalMaleAndFemaleUsers = countMaleUsers + countFemaleUsers
        malePercentage = (countMaleUsers /float(totalMaleAndFemaleUsers)) * PERCENTAGE
        femalePercentage = (countFemaleUsers /float(totalMaleAndFemaleUsers)) * PERCENTAGE
                                               
        courseRemedials = userRemedialCourses ()
        noOfRemedialCourse = testForRemedialCourses (courseRemedials)
        creditsTaken = getAndTestNumberOfCredits ()

        usersOwe = calcOfTuitionFeeAndOwe (creditsTaken, name, surname, noOfRemedialCourse, courseRemedials, brinyID)
        totalAmountOwed = totalAmountOwed + usersOwe
        averageAmountOwed = totalAmountOwed / totalUsersRegistered        

        print "Enter the next last name of a student, or type, END OF PROCESSING, to stop process students. \n"
        drawBRINYU()
        surname = getLastName()


    print "Number of users registered is: " , totalUsersRegistered
    print "The percentage of male is: %.4f"  %(malePercentage)
    print "The percentage of female is %.4f: " %(femalePercentage)
    print "The total amount owed is: $ %.4f"  %(totalAmountOwed)
    print "The average amount owed is: $ %.4f" %(averageAmountOwed)
    
       
if __name__ == '__main__':

    main()
