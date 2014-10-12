#!C:\Users\kpapa01\Desktop\Python\lab\rec04.exe

''' 
cs1114 

Submission: hw01

Programmer: Kostaq Papa
Username: kpapa01

Purpose of program: Will show the astornaut that what moneys will be getting anf not getting form their time aloft.

'''

import math

TAX = 1.0714
PAY_SCALE_FOR_A_WEEK = 1434.23
LEFT_OVER_DAY = 200
DAY_IN_A_WEEK = 7
POWER = 23


def getNameandnumberOfweekandDays ():
    '''This function will get the number of days aloft'''

    name_of_day_aloft = raw_input ("Please, enter the name:")
    days_aloft = int (raw_input ("Please, enter the number of days aloft: "))

    return weeks_aloft, days_aloft


def calc ():

    weeks_aloft = days_aloft/DAY_IN_A_WEEK
    #rdays = weeks

def payForweekAndday (weeks_aloft, days_aloft):
    '''This function will caluilate the salary for weeks and ays aloft'''
    
    pay_for_each_week_aloft = PAY_SCALE_FOR_A_WEEK * weeks_aloft
    pay_for_each_day_aloft = days_aloft * LEFT_OVER_DAY    

    print "The gross pay for each week left: %.4f" %pay_for_each_week_aloft
    print "The gross pay for each day left: %.4f" %pay_for_each_day_aloft


    return pay_for_each_week_aloft, pay_for_each_day_aloft

def total_pay_with_tax (pay_for_each_week_aloft, pay_for_each_day_aloft):
    '''This function will calute the total salary'''

    total_salary = (pay_for_each_week_aloft + pay_for_each_day_aloft) / TAX
    
    print "Total salary is: %.4f " %total_salary

def total_pay_without_tax (pay_for_each_week_aloft, pay_for_each_day_aloft):
    '''This function will calculate only the total pay, without tax'''

    total_salary_no_tax = pay_for_each_week_aloft + pay_for_each_day_aloft
    return total_salary_no_tax
    print "Total salary wihtout tax: %.4f" %total_salary_no_tax

def theContribution (total_salary):
    '''This function will the contribution retirement fund'''
    print "the contibution is:", total_salary
    the_contribution = math.cos(float(total_salary))
    the_contribution_in_power = math.pow(the_contribution, POWER)
    absolute_value = abs (the_contribution_in_power)

    print "the power %.4f" %the_contribution_in_power
    print "the absolute value %.4f"%absolute_value




def main ():
    

    daysAloft, weeksAloft = getNameandnumberOfweekandDays ()
    calc ()
    totalWeekpay, totalDaypay = payForweekAndday(daysAloft, weeksAloft)
    total_pay_with_tax(totalWeekpay, totalDaypay)
    totalSalary = total_pay_without_tax (totalWeekpay, totalDaypay)
    theContribution(totalSalary)

    # are we being executed?
if __name__ == '__main__':

    main()

    
