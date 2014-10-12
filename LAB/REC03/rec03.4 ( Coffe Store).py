"""

User Name: kpapa01

Programmer: Kostaq Papa

Purpose of this program: Based on what a customer buys, this program will calculate the receip.

Constrains: 

"""


COFFE = 2.79
DONUTS = 0.39
TAX = 1.0448629374
PERCENTAGE = 100



def welcome_customers ():
    ''' This function will say 'welcome' to the costumers and will orinet them for the next stpes. '''

    print "WELCOME TO OUR RESTORANT"
    print "Please, proceed as requsted below. \n\n\n"



def  number_of_coffes_and_donuts ():
    ''' This function will ask the client to enter the number of coffes and donuts bought'''

    number_of_coffes_bought  = int (raw_input ("Please, enter the number of coffes that you bought: "))
    number_of_donuts_bought  = int (raw_input ("Please, enter the number of donuts that you bought: "))

    return number_of_coffes_bought, number_of_donuts_bought



def total_calculation_of_products_bought (number_of_coffes_bought, number_of_donuts_bought):
    ''' This function will calculate the total of coffes and burgers bought.'''

    total_coffes = COFFE * number_of_coffes_bought
    total_donuts = DONUTS * number_of_donuts_bought
    total_products_bought = total_coffes + total_donuts + TAX

    print "\nThe price of total products bought is: %.2f \n "  %total_products_bought
    
    return total_coffes, total_donuts, total_products_bought




def the_percentage_ratio_of_total_coffe_and_donuts_to_total_products (total_coffes, total_donuts, total_products_bought):
    '''This function will calculate the ratio of total coffe to total products and the ratio of total donuts to total products and will express it in percentage.'''

    percentage_of_coffe_to_total_products  = (total_coffes / total_products_bought) * PERCENTAGE
    percentage_of_donuts_to_total_products = (total_donuts / total_products_bought) * PERCENTAGE


    print "The percentage of total coffes to total meal is: %.3f"     %percentage_of_coffe_to_total_products
    print "The percentage of total donuts to total meal is: %.3f\n\n" %percentage_of_donuts_to_total_products



def goodbye_costumers ():
    "This function will say goodbye to customers"

    print "GOOD-BYE AND HAVE A NICE DAY"
    

def main ():
        
    welcome_customers ()
    noOfCoffes, noOfDonuts = number_of_coffes_and_donuts ()
    totalCoffe, totalDonuts, totalProducts = total_calculation_of_products_bought (noOfCoffes,noOfDonuts)
    the_percentage_ratio_of_total_coffe_and_donuts_to_total_products (totalCoffe, totalDonuts, totalProducts)
    goodbye_costumers ()
    
main ()
