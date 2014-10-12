"""

User Name: kpapa01

Programmer: Kostaq Papa

Purpose of this program: Choose a winner, based an the amount of mouney entered.

Constrains: 

"""

import random


def prizeWin(dollar, quarters, dime, nickles, pennies):
    '''This function will ask the users to enter the amount of money.'''


    if (dollar == 1 and quarters == 0 and dime == 1 and nickles and pennies == 3):
        print "CONGRATULATION. You won the GRAND of $4,200,447.28"

    elif ( dollar == 2 and quarters == 2 and dime == 0 and nickles == 0 and pennies == 4) or ( dollar == 3 and halfdollar == 0 and quarters == 1 and dime == 0 and nickles == 0 and pennies == 2):
            print "You won the second prize."

            chooseTshirt()

    elif ( dollar == 0 and quarters == 1 and dime == 0 and nickles == 0 and pennies == 1) or ( dollar == 0 and quarters == 0 and 3<= dime <=7 and nickles == 0 and pennies == 0):
            print "You won 10$."
    else :
            print "You only won 2 cents this time."

def chooseTshirt():
    '''This function will chosse a random T-shirt for the sendon prize'''

    
    randomTshirt = random.randint (1, 9)
    if (randomTshirt == 1):
         print "RED"

    elif (randomTshirt == 2):
        print "Orange"

    elif (randomTshirt == 3):
          print "YELLOW"
    elif (randomTshirt == 4):
          print "GREEN"
    elif (randomTshirt == 5):
          print "BLUE"
    elif (randomTshirt == 6):
          print "INDIGO"
    elif (randomTshirt == 7):
          print "VIOLET"
    elif (randomTshirt == 8):
          print "BLACK"


                

