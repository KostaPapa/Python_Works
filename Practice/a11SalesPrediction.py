''' 
cs1114 

Submission: Sales Prediction (Private)

Programmer: Kostaq Papa
Username: kpapa01

Purpose of program: This program will predict the profit of the projected amount of total sales that a user enters.
Assumptions: The user will type what I ask for.
Constraints: I dont know what a f*** this mean.

'''

Annual_Profit = 0.23    # 23%

def enterTheProjectedAmount ():
    '''This function will ask the user to enter the projected amount of total sales.'''


    projectedAmount = float (raw_input ("Please, enter the projected amount of total sales: "))

    return projectedAmount

def predictTheProfit (projectedAmount):
    '''This function will predict the profit of the amount entered.'''

    profit = (projectedAmount * Annual_Profit) + projectedAmount

    print "The predicted profit for the projected amount of total slaes entered will be: %.3f" %(profit)

    print "THANK YOU FOR USING THIS PROGRAM!!!."

def main ():

    amount = enterTheProjectedAmount ()
    predictTheProfit (amount)

main()
