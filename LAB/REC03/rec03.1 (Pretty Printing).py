def preetyPrinting ():

    snakes = 4

    print "Hello. There are % snakes" % snakes
    '''only for int numbers'''

    average = 23.34
    print "The average is: %.2f" % average
    '''only for floating point'''

    print "% is the number of snakes and %.2f is the average" % (snakes, average)

def pressAnyKeyToExit():

    raw_input ("Please, enter any key to exit....")

    
def main():
    
    preetyPrinting()
    pressAnyKeyToExit()    
    
main ()
