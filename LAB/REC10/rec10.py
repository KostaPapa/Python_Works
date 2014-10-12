"""

User Name: kpapa01

Programmer: Kostaq Papa

Rec#: rec10

Purpose of this program: The purpose of this program is to read the information of the user and produce two files, pianoPlayers.txt and poets.txt .

Assumption: The user will type what will be asked for.

"""

def getUserInputData():
    '''This function will get the user input data for authors or musicians.'''

    stringAuthor = 'author'
    exitProgram = 'stop'
    countPianoPlayers = 0
    

    poetsInfo = [] # The purpose of this empty list is to store the names and birthdays of all poets entered by the user.
    musicianName = [] # The purpose of this empty list is to store the names of all musicians entered by the user.
    musicianInstruments = [] # The purpose of this empty list is to store the instruments that a musician playes.

    
    stopEnteringData = raw_input("Type stop to exit program or press enter to continue...")
    
    while ((stopEnteringData != exitProgram.lower())):
        getAuthorOrMusician = raw_input ("Would you like to type data for author or musician? ")
        
        if ((getAuthorOrMusician == stringAuthor.upper()) or (getAuthorOrMusician == stringAuthor.lower())):
            getAuthorNameAndBirthday = raw_input("Type author's name and date of birth separated by comma(example: mark huddon, 1970): ")
            namesAndBirthday = getAuthorNameAndBirthday.split()
            poetsInfo.append(namesAndBirthday)
            poetsInfo.sort()
            
            getTypeOfAuthor = raw_input("Type of the author: ")
            getFileNameSapmleWriting = raw_input("Type the filename that contains a sample of author's writing: ")

            
        else: #(getFirstLineData.isupper('MUSICIAN') or getFirstLineData.islower('musician')):
            getMusicianName = raw_input("Type musician's name: ")
            getInstrumentsPlayed = raw_input ("Type the instruments that this musician playes: ")
            if 'piano' in getInstrumentsPlayed:
                musicianName.append(getMusicianName)
                musicianName.sort()
                countPianoPlayers = countPianoPlayers + 1

            musicianInstruments.append(getInstrumentsPlayed)            

        stopEnteringData = raw_input("Type stop to exit program or press enter to continue...")

    return poetsInfo, countPianoPlayers, musicianName

def writeAuthorData(poetsInfo):
    '''This funtion will create the poets.txt filename and will write the names and birthdays of authors entered by the user.'''

    poetsFile = open('poets.txt','w')
    for poets in range(len(poetsInfo)):
        poetsFile.write("Poet: " + str(poetsInfo[poets]) + '\n')

def writeMusicianData(countPianoPlayers, musicianName):
    '''This funtion will create the pianoPlayer.txt file name and will write the number of musicians who plays piano and their names in alphabetical order.'''

    pianoPlayersFile = open('pianoPlayers.txt','w')
    pianoPlayersFile.write("The number of musician who play piano is: " + str(countPianoPlayers) + "\n")
    for pianoPlayers in range(len(musicianName)):
        pianoPlayersFile.write(musicianName[pianoPlayers].capitalize() + '\n')
        

def main():

    nameAndBirthdayOfPoet, noOfPianoPlayers, nameOfMusician = getUserInputData()
    writeAuthorData(nameAndBirthdayOfPoet)
    writeMusicianData(noOfPianoPlayers, nameOfMusician)
    
    
main()
