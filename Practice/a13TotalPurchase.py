''' 
cs1114 

Submission: Total Purchase (Private)

Programmer: Kostaq Papa
Username: kpapa01

Purpose of program: This program will calculate the total amound of products bought by the user.
Assumptions: The user will type what I ask for.
Constraints: I dont know what a f*** this mean.

'''

TAX = 0.06      # Tax is 6%
COFFE = 1.23    # Price of coffe in dollar.
BURGER = 3.12   # Price of burgers in dollar.
DONUTS = 2.55   # Price of donuts is dollar.
MILK = 1.69     # Price of bootles of milks.
PERCENTAGE = 1000


def productBought ():
    '''This function will ask the user to enter the amount of products bought.'''

    coffes = int (raw_input ("Please, enter the amount of coffes bought: "))
    burgers = int (raw_input ("Please, enter the amount of burgers bought: "))
    donuts = int (raw_input ("Please, enter the amount of donuts bought: "))
    milks = int (raw_input ("Please, enter the amount of bottols of milks bought: "))

    return  coffes, burgers, donuts, milks

def subtotalCalcofProducts(coffes, burgers, donuts, milks):
    '''This function will calculate the total of products bought.'''

    totalCoffes = coffes * COFFE        # Total price for coffes bought.
    totalBurgers = burgers * BURGER     # Total price for burgers bought.
    totalDonuts = donuts * DONUTS       # Total price for donuts bought.
    totalMilk = milks * MILK            # Total price for milks bought.

    subtotal = totalCoffes + totalBurgers + totalDonuts + totalMilk + TAX    # Receipe without the Tax.

    print   "The subtotal of you produsts is: %.4f " %(subtotal)

    return totalCoffes, totalBurgers, totalDonuts, totalMilk, subtotal


def percentageRatio(totalCoffes, totalBurgers, totalDonuts, totalMilk, subtotal):
    '''This function will calculate the percantage ration of each products to total products bought.'''

    ratioOfCoffes   = totalCoffes / subtotal 
    ratioOfBurgers  = totalBurgers / subtotal
    ratioOfDonuts   = totalDonuts / subtotal 
    ratioOfMilks    = totalMilk / subtotal

    print   "The ratio of total coffes to total products bought is: % " %(ratioOfCoffes)
    print   "The ratio of total burgers to total products bought is: % " %(ratioOfBurgers)
    print   "The ratio of total donuts to total products bought is: % " %(ratioOfDonuts)
    print   "The ratio of total milks to total products bought is: % " %(ratioOfMilks)

    print   "THANK YOU !!!"

def main ():
    
    noOfCoffes, noOfBurgers, noOfDonuts, noOfMilk = productBought()
    taxTotal = subtotalCalcofProducts (noOfCoffes, noOfBurgers, noOfDonuts, noOfMilk)
    percentageRatio (noOfCoffes, noOfBurgers, noOfDonuts, noOfMilk, taxTotal)

main()
