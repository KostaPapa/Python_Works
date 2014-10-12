#pos of coins

DOLLAR_COINS = 0
QUARTERS = 1
DIMES = 2
NICKLES = 3
PENNIES = 4

def getUserCoins():
    '''This funtion will get the user coins and will return it as a list.'''

    coins = [0] * 5

    coins[DOLLAR_COINS] = int(raw_input("How many dollar coins: "))
    coins[QUARTERS] = int(raw_input("How many quarters: "))
    coins[DIMES] = int(raw_input("How many dimes: "))
    coins[NICKLES] = int(raw_input("How many nickles: "))
    coins[PENNIES] = int(raw_input("How many pennies: "))

    return coins

def moneyFromCoins( coins ):
    ''' return money amount of coins '''
    return coins[ DOLLAR_COINS ]    + \
           coins[ QUARTERS ] * 0.25 + \
           coins[ DIMES ]    * 0.10 + \
           coins[ NICKLES ]  * 0.05 + \
           coins[ PENNIES ]  * 0.01

def normalizeCoins( coins ):
    ''' fixes all coin amounts that are larger than thier denomination '''

    # NOTE THAT WE ARE CHANGING THE CALLER'S LIST DIRECTLY

    coins[ NICKLES ] += coins[ PENNIES ] // 5
    coins[ PENNIES ] %= 5
    
    coins[ DIMES ] += coins[ NICKLES ] // 2
    coins[ NICKLES ] %= 2

    coins[ QUARTERS ] += coins[ DIMES ]*10 // 25
    left = coins[ DIMES ]*10 % 25
    coins[ DIMES ] = left // 10
    coins[ NICKLES ] += left % 10 // 5   

    coins[ DOLLAR_COINS ] += coins[ QUARTERS ] // 4
    coins[ QUARTERS ] %=  4

    # NOTE THAT WE DO NOT RETURN coins
    # BECAUSE WE DIRECLY CHANGED EACH OF THE
    # ELEMENTS IN THE LIST


def main():

    coins = getUserCoins()
    print "$" + str( moneyFromCoins( coins ) )

    normalizeCoins( coins )
    print "$" + str( moneyFromCoins( coins ) )
    



main()
 
