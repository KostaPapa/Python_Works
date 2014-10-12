NUM_OF_DAY = 5

def initializeList():
    '''This funtion will initialize a list creating 5 free places to enter the sales for 5 days.'''

    sales = [0] * NUM_OF_DAY

    return sales

def fillThelist(sales):
    '''This funtion will as the user to enter the sales.'''

    index = 0
    while index<len(sales):
        sales[index] = raw_input("Sales for day"+str(index+1)+"is: ")
        index = index + 1

    return sales

def displaySales(sales):
    '''This funtion will display sales.'''

    for index in sales:
        print index

    
def main():

    listOfSales = initializeList()
    salesDisplyed = fillThelist(listOfSales)
    displaySales(salesDisplyed)
    
main()
