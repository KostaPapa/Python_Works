EXIT = 'n'                  # Exit the program.
CHANGE_BOOK_TITLE = '1'     # This choice will change the book title.
CHANGE_AUTHOR_NAME = '2'    # This choice will change the author's name.
CHANGE_PUB_NAME = '3'       # This choice will change the publisher's name.


class Book( object ):
    '''This class will provide book information.'''

    def __init__( self, bookTitle, authorName, publisherName ):
        '''In this method will be used three data members:
           self.__bookTitle
           self.__authorName
           self.__publisherName
        '''
           

        self.__bookTitle = bookTitle
        self.__authorName = authorName
        self.__publisherName = publisherName

    def changeBookTitle( self, newBookTitle ):
        '''This method is a mutator. It will change the title of the book.'''

        self.__bookTitle = newBookTitle

    def changeAuthorName ( self, newAuthorName ):
        '''This method is a mutator. It will change the author's name.'''
        
        self.__authorName = newAuthorName

    def changePublisherName( self, newPublisherName ):
        '''This method is a mutator. It will change the publisher's name.'''
        
        self.__publisherName = newPublisherName

    def getBookInfo():
        '''This method is a accesor. It will return the data members.'''

        return self.__bookTitle, self.__authorName, self.__publisherName

    def __str__( self ):
        '''This method will return a pretty printing version of the data memebers.'''

        return "The book title is: %s\nThe author's name is: %s\nThe publisher's name is: %s " %( self.__bookTitle, self.__authorName, self.__publisherName )


def welcomeUser():
    '''This funtion will welcome the users.'''

    print '\n\t\t\tDDDDDDDDDDDDDDDDDDDDDDDD\t\t\t'
    print '\t\t\tDDDDDDDDDDDDDDDDDDDDDDDD'
    print '\t\t\tDDDD DIBNER LIBRARY DDDD'
    print '\t\t\tDDDDDDDDDDDDDDDDDDDDDDDD'
    print '\t\t\tDDDDDDDDDDDDDDDDDDDDDDDD\n'

def displayBookInfo():
    '''This funtion will get the user info.'''

    userChoice = raw_input( 'Enter |y| to continue or |n| to exit: ' )

    while (( userChoice != EXIT.lower() and userChoice != EXIT.upper() )):

        print '\nPlease, enter the requred information.\n'

        getBookTitle = raw_input( 'Enter Book Title: ' )
        getAuthorName = raw_input( 'Enter Author Name: ' )
        getPubName = raw_input ( 'Enter Publisher Name: ' )

        bookInfo = Book( getBookTitle, getAuthorName, getPubName )

        print '\n'
        changeInfo = raw_input( 'If you want to change your information press |y|, otherwise press |n|: ' )
        
        if (( changeInfo == EXIT.lower() ) or ( changeInfo == EXIT.upper() )):
            print '\n'
            print bookInfo
            print '\n'
            
        else: #(( changeInfo != EXIT.lower() ) or ( changeInfo != EXIT.upper() ))
            
            print '\nTo change Book Title press 1.'
            print 'To change Author Name press 2.'
            print 'To change Publisher Name press 3.\n'

            changeInfoChoice = raw_input( 'Enter your choice: ' )

            if ( changeInfoChoice == CHANGE_BOOK_TITLE ):
                getBookTitle = raw_input( 'Enter Book Title: ' )
                bookInfo.changeBookTitle( getBookTitle )
                print bookInfo

            elif ( changeInfoChoice == CHANGE_AUTHOR_NAME ):
                getAuthorName = raw_input( 'Enter Author Name: ' )
                bookInfo.changeAuthorName( getAuthorName )
                print bookInfo

            elif ( changeInfoChoice == CHANGE_PUB_NAME ):
                getPubName = raw_input ( 'Enter Publisher Name: ' )
                print bookInfo
                
        print '\n'
        userChoice = raw_input( 'Enter |y| to get info for another book, or |n| to exit: ' )
        

def main():

    welcomeUser()
    displayBookInfo()

main()


















    
