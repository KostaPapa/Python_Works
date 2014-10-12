#!C:\Users\kpapa01\Desktop\Python\hw\hw08.exe

''' 

cs1114 

Submission: hw08

Programmer: Kostaq Papa
Username: kpapa01
ID Number: 0412768

Purpose of program: The purpose of this program is to write classes that will hold employees datat.


'''

MIN_WORK_HOURS = 3.5    # The min hours to get a bonus.
MIN_BONUS_EARN = 0.01   # The min bonus ( 1% ).
PERCENTAGE = 100        # Will be used to calc persentage.




class EmployeeData ( object ):
    '''This class will contain data for a employee and will make them usable for other programmers.'''
    

    def __init__( self, ssn, name, hourlyPay, hoursWorked = 0, bonus = 0 ):
        '''This funtion will initialize the data members.'''

        self.__workerIdentifier = ssn
        self.__name = name
        self.__hourlyPay = hourlyPay
        self.__workedHours = hoursWorked
        self.__workerBonus = bonus

    def getSSN( self ):
        '''This function will return the SSN, so it can be used in the Company class.'''
        return (self.__workerIdentifier)

    def getName( self ):
        '''This function will return the name of employee, so it can be used in the Company class.'''
        return self.__name

    def getHourlyPayRate( self , rate ):
        '''This function will return the hourly employee pay, so it can be used in the Company class.'''
        self.__hourlyPay += rate
        
    def getPayment( self ):
        '''This function will calculate and return the payment of an employee, so it can be used in the Company class.'''

        self.__payment = self.__hourlyPay * self.__workedHours
        return self.__payment

    def getHoursWorked( self, hours ):
        '''This function will return the add hours worked, so it can be used in the Company class.'''
        self.__workedHours += hours

    def calcBonus( self ):
        '''This funtion will calc the bonus. An employee has to work a min of 3.5 hour to have a min bonus of 1%.'''
        if self.__workedHours >= MIN_WORK_HOURS:
            self.__workerBonus = ((self.__workedHours * MIN_BONUS_EARN)/MIN_WORK_HOURS) * PERCENTAGE
            return self.__workerBonus

    def __cmp__( self, other ):
        '''This function will sort the data of the employees in ascending order of amount owed.
           if two workers have the same amount owed, then the order is ascending SSN.'''
        
        self.__payment = self.__hourlyPay * self.__workedHours
        other.__payment = other.__hourlyPay * other.__workedHours
        
        if self.__payment > other.__payment:
            return 1
        
        elif self.__payment < other.__payment:
            return -1
        
        else: # self.__payment == other.__payment
            if self.__workerIdentifier > other.__workerIdentifier:
                return 1
            elif self.__workerIdentifier < other.__workerIdentifier:
                return -1
            else: # self.__workerIdentifier == other.__workerIdentifier
                return 0
            
    def __str__( self ):
        '''This funtion will return a printing version of the data members.'''

        employeeData =  "%s, %i, is hired.\n%s's hourly rate will be: $%s\n%s clocks %s hours " %( self.__name, self.__workerIdentifier, self.__name, self.__hourlyPay, self.__name, self.__workedHours)

        return str(employeeData)

        

# import EmployeeData


class CompanyClass( object ):
    '''This class will hire a worker,
       will pay all workers,
       will add to the hours worked for any worker,
       will give a bonus to any worker,
       will change the hourly rate for any worker.'''


    def __init__( self, employeesList = [ ] ):
        '''This funtion inititalize the needed class variables.'''

        self.__allWorkersDataList = employeesList
        

    def hireNewWorker( self, newWorker ):
        '''This funtion will hire a new worker.'''
        
        for EmployeeData in self.__allWorkersDataList:
            if EmployeeData.getSSN() == newWorker.getSSN():
                return # nothing
            
        self.__allWorkersDataList.append(newWorker)
        

    def payAllWorkers ( self ):
        '''This funtion will hire a new worker.'''

        workersPaidFilename = open('workersPaid.txt','w')
        self.__allWorkersDataList.sort()
        
        for EmployeeData in self.__allWorkersDataList:
            paidWorker = '\n' + str(EmployeeData.getPayment()) + "\n" + 'Name: ' +str(EmployeeData.getName()) + "\n" + 'Amount Paid: ' + "$" + str(EmployeeData.getPayment()) + '\n' + 'Bonus: ' + str(EmployeeData.calcBonus()) + "\n\n"
            separatorLine = '\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'
            workersPaidFilename.write(paidWorker)
            workersPaidFilename.write(separatorLine)       
            
    def addHoursWorked( self, hours, worker ):
        '''This funtion will add or remove hours worked to a worker.'''
        for EmployeeData in self.__allWorkersDataList:
            if (EmployeeData.getSSN()) == (worker.getSSN()):
                EmployeeData.getHoursWorked(hours)
       
    def changeRate( self, rate, worker ):
        '''This funtion will add hours worked to a worker.'''

        for EmployeeData in self.__allWorkersDataList:
            if EmployeeData.getSSN() == worker.getSSN():
                EmployeeData.getHourlyPayRate(rate)

def main():



    def firstDay():
        '''I am supposing that this function represent the first day of a company.'''

        firstEmployee = EmployeeData( 443882354, 'Sally Jones', 35.22 )
        hireFirstEmployee = CompanyClass().hireNewWorker( firstEmployee )
        firstEmployee.getHoursWorked( 11 )
        
        secondEmployee = EmployeeData( 283728992, 'Joe Smith', 25.34 )
        hireSecondEmployee = CompanyClass().hireNewWorker( secondEmployee )
        secondEmployee.getHoursWorked( 9 )

        w = CompanyClass().payAllWorkers()
        
        print 'EMPLOYEE EMPLOYEE EMPLOYEE --- DATA --- EMPLOYEE EMPLOYEE EMPLOYEE\n'
        print firstEmployee
        print '\nEMPLOYEE EMPLOYEE EMPLOYEE --- DATA --- EMPLOYEE EMPLOYEE EMPLOYEE\n'
        print secondEmployee
        print "\nITS PAY DAY!!!\nAll Employees has been paid.\n"

    firstDay()


    def secondDay():
        '''I am supposing that this function represent the second day of the company.'''

        firstEmployee = EmployeeData(  226782354, 'John Smith', 35.22 )
        hireFirstEmployee = CompanyClass().hireNewWorker( firstEmployee )
        firstEmployee.getHoursWorked( 11 )
        
        secondEmployee = EmployeeData( 283728992, 'Ben Boyer', 25.34 )
        hireSecondEmployee = CompanyClass().hireNewWorker( secondEmployee )
        secondEmployee.getHoursWorked( 9 )

        changeHoursWorked = CompanyClass().addHoursWorked( -8, firstEmployee )
        changeRate = CompanyClass().changeRate( -10.19, secondEmployee )

        w = CompanyClass().payAllWorkers()
        
        print '\nEMPLOYEE EMPLOYEE EMPLOYEE --- DATA --- EMPLOYEE EMPLOYEE EMPLOYEE\n'
        print firstEmployee
        print '\nEMPLOYEE EMPLOYEE EMPLOYEE --- DATA --- EMPLOYEE EMPLOYEE EMPLOYEE\n'
        print secondEmployee
        print "\nITS PAY DAY!!!\nAll Employees have been paid.\n"

    secondDay()


    def thirdDay():
        '''I am supposing that this function represent the third day of the company.'''

        firstEmployee = EmployeeData( 443882, 'Kostaq Papa', 55.55 )
        hireFirstEmployee = CompanyClass().hireNewWorker( firstEmployee )
        firstEmployee.getHoursWorked( 12 )
        
        secondEmployee = EmployeeData( 283728, 'Mario Grant', 25.34 )
        hireSecondEmployee = CompanyClass().hireNewWorker( secondEmployee )
        secondEmployee.getHoursWorked( 30 )

        changeHoursWorked = CompanyClass().addHoursWorked( 8, firstEmployee )
        changeRate = CompanyClass().changeRate( -10.19, secondEmployee )

        w = CompanyClass().payAllWorkers()
        
        print '\nEMPLOYEE EMPLOYEE EMPLOYEE --- DATA --- EMPLOYEE EMPLOYEE EMPLOYEE\n'
        print firstEmployee
        print '\nEMPLOYEE EMPLOYEE EMPLOYEE --- DATA --- EMPLOYEE EMPLOYEE EMPLOYEE\n'
        print secondEmployee
        print "\nITS PAY DAY!!!\nAll Employees have been paid.\n"


    thirdDay()
        
# are we being executed?
if __name__ == '__main__':
    main()




    
