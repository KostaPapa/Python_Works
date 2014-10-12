class TypeName( object ):
    '''This class will contain the general form of a class.'''


    def __init__( self, dataMember_1, dataMember_2, dataMember_3 = 3 ): # defaultValue
        '''This function will initialize the variables needed to be used during class design. Notice that other variables may be needed
           and they can be created without being passed as arguments.'''


        self.__dataMember_1 = dataMember_1
        self.__dataMember_2 = dataMember_2
        self.__dataMember_3 = dataMember_3
        self.__dataMember_4 = 4
        self.__dataMember_5 = None

        
    def getDataMemember_1( self, newDataMember_1 ):
        '''This funtion will return the newValueOfDataMemember_1 so it can be use by the programmer.'''

        self.__dataMember_1 = newDataMember_1

        return self.__dataMember_1

    def getDataMemember_2( self, newDataMember_2 ):
        '''This function will return a newDataMember_2 so it cab be used by the programmer.'''

        self.__dataMember_2 = newDataMember_2

        return  self.__dataMember_2

    def calcValue( self ):
        '''This funtion will make calculations.'''

        self.__totalValue = self.__dataMember_1 + self.__dataMember_2 + self.__dataMember_3 + self.__dataMember_4
        self.__average = self.__totalValue / 4
        self.__percentage = self.__average * 100

    def __str__( self ):
        '''This funtion will print the data memebrs.'''

        return 'The total value is: %s\nThe average is: %s\nThe percentage is: %s' %( self.__totalValue, self.__average, self.__percentage )
    

def main():


    def TestingClass():
        '''This funtion will test the class.'''

        var1 = TypeName(1,2)
        var1.calcValue()

        var2 = TypeName(1,2)
        var2.getDataMemember_1(1.11)
        var2.calcValue()

        var3 = TypeName(1,2)
        var3.getDataMemember_2(2.22)
        var3.calcValue()

        var4 = TypeName(1,2)
        var4.getDataMemember_1(1.11)
        var4.getDataMemember_2(2.22)
        var4.calcValue()

        print "The first variable is holding this information:\n",var1
        print '\n'
        print "The second variable is holding this information:\n",var2
        print '\n'
        print "The third variable is holding this information:\n",var3
        print '\n'
        print "The fourth variable is holding this information:\n",var4
        print '\n'
        
        # Putting in a list
        
        print "Here Begins the list thing...( # _ # )\n"
        listOfVar = []
        listOfVar.append(var1)
        listOfVar.append(var2)
        listOfVar.append(var3)
        listOfVar.append(var4)
        for variables in listOfVar:
            print variables
            print "\n"

                
    TestingClass()


main()




















