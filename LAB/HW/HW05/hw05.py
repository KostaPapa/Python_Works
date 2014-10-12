#!C:\Users\kpapa01\Desktop\Python\hw\hw05.exe

''' 
cs1114 

Submission: hw05

Programmer: Kostaq Papa
ID number: 0412768
Username: kpapa01
Required FileName: hw05.py


Purpose of program: This program is a game and its name is HIT&PLAY. Based on the numbers that players will type and the numbers that the House will randomly generate, HIT&PLAY program will choose the winners and will give them money.
Assumptions: The player will type an int number when asked to enter number of tries.
             The players will enter something numeric and with only two decimal places when asked to pay.

'''

COST_OF_TRY = 1.25                      # The cost of one try is $1.25
HIT_WINS = 5.00                         # For a hit the player wins $5.00
MATCH_WINS = 2.50                       # For a match the player wins $2.50
MIN_RANDOM_VALUE = 0                    # The minimum random value is 0.
MAX_RANDOM_VALUE = 9                    # The maximum random value is 9.
STOP = 'C'                              # This character will stop running the program.
SEPARATOR_LINE = '$' * 100              # This is a separator line with a length of 100 char long.
MIN_RANDOM_SPECIAL_LINE = 7             # This is the minimum random value for drawing a 'BONUS' line when the player wins 3 hits.
MIN_RANDOM_SPECIAL_LINE = 11            # This is the maximum random value for drawing a 'BONUS' line when the player wins 3 hits.
HOUSE_BONUS_SEPARATOR_LINE = '-' * 31   # This is a seperator line with length 31 char long. It will be used to draw a line in the 'houseSpecialBonusTriangle' function.


import random, math


def sayWelcomeAndGetPlayersName():
    '''The purpose of this function is to make the game more interesting by welcoming each player and asking them to enter their name or nickname.'''

    print SEPARATOR_LINE
    print "\t\t\t\t\tWELCOME TO HIT & PLAY"
    print "TODAY IS YOUR LUCKY DAY!!!\n"

    playerName = raw_input ("Come on and enter your name (or nickname): ")

    print "HELLO",playerName,"\n"

    return playerName

def getPlayerTriesAndPayment():
    '''This function will get the player tries and payment.'''

    print "\nOne try cost $1.25."
    playerTotalNumberOfTries = int(raw_input("How many times do you want to try? "))

    totalRequiredPayment = playerTotalNumberOfTries * COST_OF_TRY    
    print "You should pay $",totalRequiredPayment,"for the required number of tries."

    playerPayment = float(raw_input("Please, enter payment: "))

    return playerTotalNumberOfTries, totalRequiredPayment, playerPayment
    

def testPayment(totalRequiredPayment, playerPayment):
    '''This function will test if the player entered the required amount.'''
    

    while (playerPayment < totalRequiredPayment):

        amountNotPaid = totalRequiredPayment - playerPayment
        print "Sorry not enough. You should add $",amountNotPaid,"(overpayment will not be returned)."
        playerRePayment = float(raw_input("Please, enter payment: "))
        playerPayment = playerPayment + playerRePayment

    if (playerPayment > totalRequiredPayment):
        playerTip = playerPayment - totalRequiredPayment
        print "Thank you for the $",playerTip,"tip!"


def getPlayersThreeGueses():
    '''This function will get the player's three guess digits and will not allow the player to enter similar digits.'''

    guessList = []
    

    guessList.append(int(raw_input("Please, enter digit for left position: ")))
    guessList.append(int(raw_input("Please, enter digit for middle position: ")))
    guessList.append(int(raw_input("Please, enter digit for right position: ")))


    while ((guessList[0] == guessList[1]) or (guessList[1] == guessList[2]) or (guessList[0] == guessList[2])):

        print "Sorry, you must type different digits."
        guessList[0] = (int(raw_input("Please, enter digit for left position: ")))
        guessList[1] = (int(raw_input("Please, enter digit for middle position: ")))
        guessList[2] = (int(raw_input("Please, enter digit for right position: ")))

    print "\n",guessList,"\n"
    return guessList


def threeRandomDigits():
    '''This function will choose three different random digits.'''

    randomList = []

    randomList.append(random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE))
    randomList.append(random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE))
    randomList.append(random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE))

    while ((randomList[0] == randomList[1]) or (randomList[1] == randomList[2]) or (randomList[0] == randomList[2])):

        randomList[0] = random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
        randomList[1] = random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
        randomList[2] = random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
            
    print randomList,"\n"
    return randomList
    
def houseSpecialBonusTriangle():
    '''This function will draw the house special bonus triangle.'''

    print HOUSE_BONUS_SEPARATOR_LINE + "THREE HITS"
    for bonus in range(1, 8, 1):
        print ("BONUS " * (bonus-1))        
    print ("BONUS " * (random.randint(MIN_RANDOM_SPECIAL_LINE,MIN_RANDOM_SPECIAL_LINE
                                      ) - 2)) + "MOMUS " + "BONUS"
    for bonus in range(7, 0, -1):
        print ("BONUS " * (bonus-1))    
    print HOUSE_BONUS_SEPARATOR_LINE + "THREE HITS"
    
def testTheWinOfHits(guessList, randomList):
    '''This function will test all the possibilities when a Hit occur.'''

    # Possibilities of a Hit


    if ((guessList[0] == randomList[0]) and (guessList[1] ==  randomList[1]) and (guessList[2] ==  randomList[2])):
        houseSpecialBonus = (100 + ( guessList[0] * ((math.pow(math.e, math.sin(guessList[1]))) - guessList[2] )))
        numberOfHits = 3
        hitEarnings = (numberOfHits * HIT_WINS) + houseSpecialBonus
        for hits in range(numberOfHits):
            hits = '\a$$$$$$ CONGRATULATION - ' + 'YOU ARE VERY LUCKY - ' + 'MONEY ARE FLYING $$$$$$'
            print "\n",hits,"\n"

        print "YOU WIN THE HOUSE SPECIAL BONUS!!!"
        houseSpecialBonusTriangle()
        print "YOU WIN THE HOUSE SPECIAL BONUS!!!"
        print "YOU WIN: $",houseSpecialBonus
        print "Number of hits: ",numberOfHits
        
    elif ((guessList[0] == randomList[0]) and (guessList[1] == randomList[1])):
        numberOfHits = 2
        hitEarnings = numberOfHits * HIT_WINS
        print "Number of hits: ",numberOfHits
    elif ((guessList[1] == randomList[1]) and (guessList[2] == randomList[2])):
        numberOfHits = 2
        hitEarnings = numberOfHits * HIT_WINS
        print "Number of hits: ",numberOfHits
    elif ((guessList[0] == randomList[0]) and (guessList[2] == randomList[2] )):
        numberOfHits = 2
        hitEarnings = numberOfHits * HIT_WINS
        print "Number of hits: ",numberOfHits
        
    elif (guessList[1] == randomList[1]):
        numberOfHits = 1
        hitEarnings = numberOfHits * HIT_WINS
        print "Number of hits: ",numberOfHits
    elif (guessList[2] == randomList[2]):
        numberOfHits = 1
        hitEarnings = numberOfHits * HIT_WINS
        print "Number of hits: ",numberOfHits
    elif (guessList[0] == randomList[0]):
        numberOfHits = 1
        hitEarnings = numberOfHits * HIT_WINS
        print "Number of hits: ",numberOfHits
    else:
        numberOfHits = 0
        hitEarnings = numberOfHits * HIT_WINS
        print "Number of hits: ",numberOfHits

    return numberOfHits, hitEarnings


def testTheWinOfMatches(guessList, randomList):
    '''This function will test all the possibilities when a Match wins.'''

    # Possibilities of a Match

    if ((guessList[0] == randomList[2]) and (guessList[1] == randomList[0]) and (guessList[2] == randomList[1])):
        numberOfMatches = 3
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif ((guessList[0] == randomList[1]) and (guessList[1] ==  randomList[2]) and (guessList[2] == randomList[0])):
        numberOfMatches = 3
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches

    elif ((guessList[0] == randomList[1]) and (guessList[1] == randomList[2])):
        numberOfMatches = 2
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif ((guessList[0] == randomList[1]) and (guessList[1] == randomList[0])):
        numberOfMatches = 2
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif ((guessList[0] == randomList[2]) and (guessList[1] == randomList[0])):
        numberOfMatches = 2
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif ((guessList[1] == randomList[2]) and (guessList[2] == randomList[1])):
        numberOfMatches = 2
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif ((guessList[1] == randomList[2]) and (guessList[2] == randomList[0])):
        numberOfMatches = 2
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif ((guessList[1] == randomList[0]) and (guessList[2] == randomList[1])):
        numberOfMatches = 2
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif ((guessList[2] == randomList[0]) and (guessList[0] == randomList[2])):
        numberOfMatches = 2
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif ((guessList[2] == randomList[0]) and (guessList[0] == randomList[1])):
        numberOfMatches = 2
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif ((guessList[2] == randomList[1]) and (guessList[0] == randomList[2])):
        numberOfMatches = 2
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
        
    
    elif (guessList[0] == randomList[1]):
        numberOfMatches = 1
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches    
    elif (guessList[0] == randomList[2]):
        numberOfMatches = 1
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif (guessList[1] == randomList[0]):        
        numberOfMatches = 1
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif (guessList[1] == randomList[2]):
        numberOfMatches = 1
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif (guessList[2] == randomList[0]):
        numberOfMatches = 1
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
    elif (guessList[2] == randomList[1]):
        numberOfMatches = 1
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches
        
    else:
        numberOfMatches = 0
        matchEarnings = numberOfMatches * MATCH_WINS
        print "Number of matches: ",numberOfMatches


    return numberOfMatches, matchEarnings


def currentStatusOfPlayer():
    '''This funtion will show the current status of the player for each try.'''
        
    countTries = 0
    countNumberOfHits = 0
    countNumberOfMatches = 0
    countHitEarnings = 0
    countMatchEarnings = 0
    houseSpecialBonus = 0
    
    totalTries, totalPay, payEntered = getPlayerTriesAndPayment()
    testPayment(totalPay, payEntered)

    for tries in range(totalTries):

        countTries = tries + 1
        numberOfTriesLeft = totalTries - countTries
        print "\nThis is try number:", countTries
        print "You have", numberOfTriesLeft ,"tries left."

        totalWin = countHitEarnings + countMatchEarnings
        print "Currently, your earnings are: $",totalWin,"[ hits:",countNumberOfHits,"matches:",countNumberOfMatches,"]"
        
        playerListDigits = getPlayersThreeGueses()
        randomListDigit = threeRandomDigits()

        noOfHits, singleHitsMoney = testTheWinOfHits(playerListDigits, randomListDigit)
        countNumberOfHits = countNumberOfHits + noOfHits
        countHitEarnings = countHitEarnings + singleHitsMoney
        
        noOfMatches, singleMatchsMoney = testTheWinOfMatches(playerListDigits, randomListDigit)
        countNumberOfMatches = countNumberOfMatches + noOfMatches
        countMatchEarnings = countMatchEarnings + singleMatchsMoney

    return totalWin

def displayPlayerFinalWinnings(totalWin):
    '''This function will display the player's final winnings.'''

    print "You win: $",totalWin,"\n"

    return totalWin

def playHitAndMatch():
    '''This function will play the game.'''

    playerWinnings = currentStatusOfPlayer()
    displayPlayerFinalWinnings(playerWinnings)
    
def main():

    while ((sayWelcomeAndGetPlayersName()) != STOP):
        playHitAndMatch()
    print "FINALLY SOME REST. I HAVE BEEN RUNNING FOREVER!!!"
    
# are we being executed?
if __name__ == '__main__':
    main()

