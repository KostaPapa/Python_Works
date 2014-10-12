DONUTS = 0.75
MILK = 1.25
JUICY = 1.35
OMLETS = 3.35
BURGER = 3.59
STOP_ORDERING = 'S'


def welcomeCostumers():
    '''Will say HI'''

    print "WELCOME TO OUR RESTORANT"
    print '''Today's MENU is:
             DONUTS = $ 0.75
             MILK   = $ 1.25
             JUICY  = $ 1.35
             OMLETS = $ 3.35
             BURGER = $ 3.59
          '''

def takeCostumerOrder():
    '''This function will take the constumer order.'''

    donuts = "donuts"
    milk = "milk"
    juicy = "juicy"
    omlets = "omlets"
    burger = "burger"

    order == raw_input ("What would you like to order: ")
    
    return order

def funtionCall():

    while True:
        print "Thank you for comming."
        name = raw_input ("Please, enter yout name: ")
        if (name == STOP_ORDERING):
            exit
        print "What would you like to order? "        

        costumerOrder = takeCostumerOrder()


funtionCall()







