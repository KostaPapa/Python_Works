HEADS_WIN = 5   # If the user get a heads, he will win $5.
NO = 'N'        # If the user presses N or n the program will exit.




import random

class Toss ( object ):
    '''This class will write methods that will determine if a toss
       is heads or tails.'''

    def __init__( self, sideUp = 'Heads', sideDown = 'Tails' ):

        self.__coinSideUp = sideUp
        self.__coindSideDown = sideDown

    def getHeadsOrTails( self ):
        '''This funtion will determine if the coin is heads or tail.'''

        if random.randint( 0, 1 ) == 0:
            return self.__coinSideUp
        else: # random.randint( 0, 1 ) == 1
            return self.__coindSideDown



    
def main():

    def testTossClass():
        '''This funtion will test the toss class.'''

        userChoice = raw_input('Press Y to spin the coin or N to exit: ')

        balance = 0

        while ( ( userChoice != NO.upper() ) and ( userChoice != NO.lower() ) ):
            print "The coin is spining...\n"
            print '...\n'

            spining = Toss()
            spinResult = spining.getHeadsOrTails()

            if spinResult == 'Heads':
                print '\n$$$$$$$$$$$$$$$$$$$$$\n'
                print 'CONGRATULATION!!!'
                print 'YOU WON $5'
                print 'MONEY ARE FLYING'
                balance += HEADS_WIN
                print 'Your balance is: ',balance
                print '\n$$$$$$$$$$$$$$$$$$$$$\n'
                                
            else: # spinResult == 'Tails'
                print 'Sorry. It is Tail!'

            
            userChoice = raw_input('Press Y to try again or N to exit: ')

        print "The total winings are: $",balance
            

    testTossClass()

main()
