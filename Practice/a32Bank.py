INSUFFICENT_FUNDS = -1
ACCOUNT_NOT_FOUND = -2


class BankAccount( object ):
    '''This is a bank account.'''


    def __init__( self, id, name, balance = 0 ):
        '''This funtion is creates three data members:
          id      -   should be an int
          name    -   should be a string
          balance -   should be a numeric value ( float, 2 decimal places ), if provided
        '''

        self.__id = id
        self.__name = name
        self.__balance = float(balance)

        # to make an acc inactive should be used another data memeber

    
    def addMoney( self, amount ):
        '''This funtion updates balance by adding amount'''

        self.__balance += amount
        

    def withdrawMoney( self, amount ):
        '''This funtion will withdraw money from a account and will return them.
           If not enough money in the account it will return INSUFFICENT_FUNDS.'''

        if ( self.__balance >= amount ):
            self.__balance -= amount
            return amount
        else: #( self.__balance < amount ):
            return INSUFFICENT_FUNDS
        

    def getBalance( self ):
        '''This funtion will return the balance.'''

        return self.__balance
    

    def getName( self ):
        '''This funtion will return the name.'''

        return self.__name
    

    def changeName( self, newName ):
        '''This funtion will set the name to be the new name.'''

        self.__name = newName


    def getID( self ):
        '''This funtion will return the id number of the account so it can be
           used by the programmer.'''

        return self.__id


    def makeAccInactive( self ):
        '''Not yet emplemented.'''
        
        

    def __cmp__( self, other ):
        '''This funtion will be used for sorting purposes. It will compare
           accounts by id number.'''

        if ( self.__id > other.__id ):
            return 1
        elif ( self.__id < other.__id ):
            return -1
        else: # ( self.__id == other.__id ):
            return 0

    def __eq__( self, other ):
        '''This funtion will use id for comparing to bank accounts.'''

        return self.__id == other.__id
    

    def __str__( self ):
        '''pretty printing of bank account.'''

        return 'The id of the account is: %d\nThe name of the account is: %s\nThe balance of the account is: $%.2f' %(  self.__id, self.__name, self.__balance )


class Bank( object ):
    '''Manages BankAccounts.'''

    def __init__( self, nameOfBank, nextIDnumber = 100000 ):
        '''This funtion will create three data members:
           nameOfBank - should be a string
           listOfBankAccs - an empty list that will contain BankAccounts
           nextIDnumber - represent the next id number to be assigned to a BankAccount when it is set up.'''

        self.__nameOfBank = nameOfBank
        self.__listOfBankAccs = [ ]
        self.__nextIDnumber = nextIDnumber
        

    def addBankAcc( self, name, balance = 0 ):
        '''This funtion will create and add a new bank account object useing the nextIDnumber for the id.'''

        newBankAcc = BankAccount ( self.__nextIDnumber, name, balance )
        self.__listOfBankAccs.append( newBankAcc )
        self.__nextIDnumber += 1
        

    def __findInxOfID( self, id ):
        '''This funtion will return the index of account based in it's id when found.
           otherwise returns number of bank accounts.'''

        index = 0
        while ( ( index < len( self.__listOfBankAccs )) and ( id != self.__listOfBankAccs[index].getID() ) ):
            index += 1
        return index

    def depositIntoAcc( self, id, amount ):
        '''This funtion will deposit an amount into a certain account, based on account's ID.
           If account not found will return ACCOUNT_NOT_FOUND.'''

        ndx = self.__findInxOfID(id)
        if ndx == len( self.__listOfBankAccs ):
            return ACCOUNT_NOT_FOUND
        self.__listOfBankAccs[ ndx ].addMoney( amount )

    def withdrawFromAcc( self, id, amount ):
        '''This funtion will withdraw an amount from a certain account, based on account's ID.
           If account not found will return ACCOUNT_NOT_FOUND.
           Note that it is already cheked for INSUFFICENT_FUNDS'''

        ndx = self.__findInxOfID(id)
        if ndx == len( self.__listOfBankAccs ):
            return ACCOUNT_NOT_FOUND
        taken = self.__listOfBankAccs[ ndx ].withdrawMoney( amount )
        return taken

    def transferFunds( self, accFrom_ID, accTO_ID, amount ):
        '''This funtion will transfer funds form a account to another account.
           If the either id doesnt exit then ACCOUNT_NOT_FOUND is returned.
           If in the accFrom are insufficent funds, INSUFFICENT_FUNDS is returned.
        '''

        ndxFrom = __findInxOfID( accFrom_ID )
        if ndxFrom == len( self.__listOfBankAccs ):
            return ACCOUNT_NOT_FOUND

        ndxTo = __findInxOfID( accTO_ID )
        if ndxTo == len( self.__listOfBankAccs ):
            return ACCOUNT_NOT_FOUND

        taken = self.__listOfBankAccs[ ndxFrom ].withdrawMoney( amount )
        if taken == INSUFFICENT_FUNDS:
            return taken
        self.__listOfBankAccs[ ndxTo ].addMoney( amount )

    def closeBankForTheDay( self ):
        '''This funtion will write to a file all BankAccount data. If file could not
           be open or closed we have a serios problem.'''

    def getBankHoldings( self ):
        '''This funtion will calculate and return the holdings of a bank.'''

        sum = 0
        for acc in self.__listOfBankAccs:
            sum += acc.getBalance()
        return sum

        

    def __str__( self ):
        '''This funtion will print something otherwise you tell me what is the purpose.'''

        strgChars = list( self.__nameOfBank )
        strg =  '   ' + '-' * ( 2 * len( self.__nameOfBank ) + 2 ) + '\n'
        strg += '...[' + '|'.join( strgChars ) + ']...\n'
        strg += '   ' + '-' * ( 2 * len( self.__nameOfBank ) + 2 ) + '\n\n'
        strg += 'Bank Accounts (current)' + '\n\n'
        for elem in self.__listOfBankAccs:
            strg += str( elem ) + '\n\n'
        return strg


def main():

    def KpMandDELLComp():
        '''This funtion will create bank accounts for the KpM Electronics Company and will add them in their private Bank.'''

        # create a bank
        # could create as many as we need

        bank0 = Bank( 'BANK OF KpM ELECTRONICS COMPANY' )
        bank0.addBankAcc( 'Kostaq Papa', 100 )
        bank0.addBankAcc ( 'Mario Papa', 200 )
        bank0.addBankAcc ( 'Xhoxhi Papa', 300 )
        bank0.addBankAcc ( 'Zheti Papa', 400 )
        bank0.addBankAcc ( 'KpM ELECTRONICS', 5000 )
        
        # deposit 400 to account 100000
        bank0.depositIntoAcc( 100000, 400 )
        
        # deposit 300 to account 100001
        bank0.depositIntoAcc( 100001, 300 )
        
        # deposit 190.45 to account 100003
        bank0.depositIntoAcc( 100002, 190.45 )

        # deposit to an account that doest exists (1234342)
        bank0.depositIntoAcc( 1234342, 190.45 )
        # nothing will happen, unless the programmer who deal with user handle it will scary, freaky messages for users.
        print bank0,
        print 'Bank Holdings: $%.2f' %( bank0.getBankHoldings() )
        print '\n'
        
        

        

        








        #userAcc1 = BankAccount( 57913, 'Kostaq Papa' )
        #userAcc2 = BankAccount( 46802, 'Mario Papa' )
        #userAcc4 = BankAccount( 35791, 'Lizheta Papa' )
        #userAcc0 = BankAccount( 24680, 'Xhoxhi Papa' )
        #userAcc3 = BankAccount( 13579, 'KpM Electronics' )

        #userAcc1.addMoney( 100.12 )
        #userAcc2.addMoney( 200.1 )
        #userAcc4.addMoney( 300.9 )
        #userAcc0.addMoney( 400.765 )
        #userAcc3.addMoney( 500.323 )

        #bank0 = Bank( 'BANK OF KpM ELECTRONICS COMPANY' )
        #bank0.addBankAcc( userAcc1 )
        #bank0.addBankAcc( userAcc2 )
        #bank0.addBankAcc( userAcc4 )
        #bank0.addBankAcc( userAcc0 )
        #bank0.addBankAcc( userAcc3 )
        #print bank0
        #print "Bank holdings are: $%.2f" %( bank0.getBankHoldings() )

        #bank0.depositIntoAcc( 57913, 500 )
        #print bank0
        #print "Bank holdings are: $%.2f" %( bank0.getBankHoldings() )
        
        
        #print '\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n\n'

    
        #userAcc1 = BankAccount( 57913, 'John Bayer' )
        #userAcc2 = BankAccount( 46802, 'Rakinur Alam' )
        #userAcc4 = BankAccount( 35791, 'Jose Colindres' )
        #userAcc0 = BankAccount( 24680, 'Gideon Adaremi' )
        #userAcc3 = BankAccount( 13579, 'Dell Computers' )

        #userAcc1.addMoney( 100 )
        #userAcc2.addMoney( 200 )
        #userAcc4.addMoney( 300 )
        #userAcc0.addMoney( 400 )
        #userAcc3.addMoney( 500 )

        #bank1 = Bank( 'BANK OF DELL COMPUTERS COMPANY' )
        #bank1.addBankAcc( userAcc1 )
        #bank1.addBankAcc( userAcc2 )
        #bank1.addBankAcc( userAcc4 )
        #bank1.addBankAcc( userAcc0 )
        #bank1.addBankAcc( userAcc3 )
        #print bank1
        #print "Bank holdings are: $%.2f" %( bank1.getBankHoldings() )

        #print '\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n\n'

    KpMandDELLComp()
        
main()


