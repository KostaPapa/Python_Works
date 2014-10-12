import random

def noOfRowsAndnoOfCols():
    '''This funtion will get the number of rows and columms.'''

    noOfRows = int (raw_input("Enter number of rows: "))
    noOfCols = int (raw_input ("Enter number of columms: "))

    return noOfRows, noOfCols

def randomRectangle(noOfRows, noOfCols):
    '''This funtion will draw a random rectangle.'''

    for row in range(noOfRows):
        print "%3i" %(row + 1),
        for columm in range(noOfCols):
            print random.randint(0,9),
        print

def randomTriangel(width):
    '''This function will draw a random triangle.'''
    print
    
    for row in range (width):
        print "%3i" %(row + 1),
        for column in range(row):
            print random.randint(0,9),
        print
    
def main():
    rows, columms = noOfRowsAndnoOfCols()
    randomRectangle(rows, columms)
    randomTriangel(10)

main()
