"""

User Name: kpapa01

Programmer: Kostaq Papa

Rec#: rec10

Purpose of this program: The purpose of this program is to read HTML code.

Assumption: The user will type what will be asked for.

"""

STOP_ENTER_WORD = 'STOP'
EXIT_PROGRAM = 'EXIT'

ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'


def dispalyMenu():
    '''This funtion will dispay menu.'''

    print "THIS IS MENU"

    print "Press 1 to add a word."
    print "Press 2 to remove the entered word"
    print "Press 3 to save the current list and exit."
    print "Press 4 to save print an HTML version of word entered."
    print "Press 5 to exit."

    userChoice = raw_input ("Enter your choice: ")

    while (userChoice != EXIT_PROGRAM):
        

        if (userChoice == ONE):
            listOfWord = []
            userWord = raw_input("Enter a word: ")
            
            while (userWord != STOP_ENTER_WORD):
                
                listOfWord.append(userWord)
                userWord = raw_input("Enter another word of press stop to stop entering words: ")

        elif (userChoice == TWO):
            removeWord = raw_input("Enter the name of the word entered: ")
            if removeWord in listOfWord:
                listOfWord.remove(removeWord)
            else:
                print "Word not found!!."

        
        elif (userChoice == THREE):
            wordsFileName = open('wordsWordsWords.txt', 'w')
            for words in listOfWord:                
                wordsFileName.write(words + "\n")

            wordsFileName.close()
            print "List was sucessfully saved."

        elif (userChoice == FOUR):

            rec11HtmlFile = open('rec11HtmlCode.txt','w')
            firstPartHtmlCodeFile = open ('firstPartOfHtmlCode.txt','r')
            for lines in firstPartHtmlCodeFile:
                rec11HtmlFile.write(lines + "\n")
            firstPartHtmlCodeFile.close()
            rec11HtmlFile.close()
                        

            rec11HtmlFile = open('rec11HtmlCode.txt','a')
            wordsFileName = open('wordsWordsWords.txt', 'r')
            for words in wordsFileName:
                rec11HtmlFile.write(words + "\n")
            wordsFileName.close()
            rec11HtmlFile.close()
    

            rec11HtmlFile = open('rec11HtmlCode.txt','a')
            secondPartHtmlCodeFile = open('secondPartOfHtmlCode.txt','r')
            for lines in secondPartHtmlCodeFile:
                rec11HtmlFile.write(lines + "\n")
            secondPartHtmlCodeFile.close()                
            rec11HtmlFile.close()

            
        else:
            print "Invalid Number."
        userChoice = raw_input("Enter another number if you want to enter another choice or press EXIT: ")
            
            

def main():
    
    dispalyMenu()

main()
