def getCostumerSalary():
    '''This funtion will get the costumer annnual salary.'''

    annulalSalary  = float(raw_input("Enter you annual salary: "))
    return annulalSalary

def getNoOfYearsInJob():
    '''This funtion will get the number of customer's years in the current job.'''

    noOfYears = float(raw_input("Enter number of years on your current job: "))

    return noOfYears

def checkIfApplicableForLoan(annulalSalary, noOfYears):
    '''This funtion will check is the customer is eligable for a bank loan.'''

    if ((annulalSalary >= 30000.00) and (noOfYears >= 2)):
            print "You qualify for our bank's loan."
    else:
        print "You do not qualify for this loan."
    


def main():

    salaray = getCostumerSalary()
    workedYears = getNoOfYearsInJob()
    checkIfApplicableForLoan(salaray, workedYears)    

main()
