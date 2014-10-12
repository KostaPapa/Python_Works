import time


STUDENT_CHOICE_1 = '1'       # Will play the Taboo Game when students enter 1.
STUDENT_CHOICE_2 = '2'       # Will show Game Rules when students enter 2.
EXIT             = '3'       # Will exit the program when students enter 3.

TIME_LIST  = [ "\aTime Remaining  02:30", "\aTime Remaining: 02:00", "\aTime Remaining: 01:30", "\aTime Remaining: 01:00", "\aTime Remaining: 00:30", "\a\a\aTIMES UP \aTIMES UP \aTIMES UP \aTIMES UP \aTIMES UP\a\a\a" ]

WRITING_10 = 'wr10'      # Writing category choice. This choice is worth 10 points.

PEOPLE_8   = 'pe8'       # People category choice. This choice is worth 8 points.
PLACE_8    = 'pl8'       # Place category choice. This choice is worth 8 points.
LIFE_8     = 'li8'       # Life category choice. This choice is worth 8 points.

LIFE_6     = 'li6'       # Life category choice. This choice is worth 6 points.
PLACE_6    = 'pl6'       # Place category choice. This choice is worth 6 points.
SPACE_6    = 'sp6'       # Space category choice. This choice is worth 6 points.
PEOPLE_6   = 'pe6'       # People category choice. This choice is worth 6 points.
CURRENCY_6 = 'cu6'       # Currency category choice. This choice is worth 6 points.

CARS_4     = 'ca4'       # Cars category choice. This choice is worth 4 points.
SPACE_4    = 'sp4'       # Space category choice. This choice is worth 4 points.
MUSIC_4    = 'mu4'       # Music category choice. This choice is worth 4 points.
PLACE_4    = 'pl4'       # Place category choice. This choice is worth 4 points.
COMPANIES_4= 'co4'       # Companies category choice. This choice is worth 4 points.
HEALTH_4   = 'he4'       # Health category choice. This choice is worth 4 points.
INVENTION_4= 'in4'       # Invention category choice. This choice is worth 4 points.



######################################################################################


# The following is the PeopleWord class.

class PeopleWord( object ):
    '''will create words only for people's category.'''

    def __init__( self, peopleWord ):
        '''peopleWord   -->     will handle a word for the people's category.
        '''
        
        self.__peopleWord = peopleWord

    def getPeopleWord( self ):
        '''will return peopleWord.'''

        return self.__peopleWord

    def __str__( self ):
        '''pritty printing.'''

        return '%s\n'%self.__peopleWord


######################################################################################


# The following is the PlaceWord class.

class PlaceWord( object ):
    '''will create words only for place's category.'''

    def __init__( self, placeWord ):
        '''placeWord   -->     will handle a word for the place's category.
        '''
        
        self.__placeWord = placeWord

    def getPlaceWord( self ):
        '''will return placeWord.'''

        return self.__placeWord

    def __str__( self ):
        '''pritty printing.'''

        return '%s\n'%self.__placeWord


######################################################################################

    
# The following is the SpaceWord class.

class SpaceWord( object ):
    '''will create words only for space's category.'''

    def __init__( self, spaceWord ):
        '''spaceWord   -->     will handle a word for the space's category.
        '''
        
        self.__spaceWord = spaceWord

    def getSpaceWord( self ):
        '''will return spaceWord.'''

        return  self.__spaceWord

    def __str__( self ):
        '''pritty printing.'''

        return '%s\n'% self.__spaceWord


######################################################################################


# The following is the LifeWord class.

class LifeWord( object ):
    '''will create words only for life's category.'''

    def __init__( self, lifeWord ):
        '''lifeWord   -->     will handle a word for the life's category.
        '''
        
        self.__lifeWord = lifeWord

    def getLifeWord( self ):
        '''will return lifeWord.'''

        return  self.__lifeWord

    def __str__( self ):
        '''pritty printing.'''

        return '%s\n'% self.__lifeWord


######################################################################################


# The following is the CurrencyWord class.

class CurrencyWord( object ):
    '''will create words only for currency's category.'''

    def __init__( self, currencyWord ):
        '''currencyWord   -->     will handle a word for the currency's category.
        '''
        
        self.__currencyWord = currencyWord

    def getCurrencyWord( self ):
        '''will return currencyWord.'''

        return  self.__currencyWord

    def __str__( self ):
        '''pritty printing.'''

        return '%s\n'% self.__currencyWord


######################################################################################


# The following is the CarWord class.

class CarWord( object ):
    '''will create words only for car's category.'''

    def __init__( self, carWord ):
        '''carWord   -->     will handle a word for the car's category.
        '''
        
        self.__carWord = carWord

    def getCarWord( self ):
        '''will return carWord.'''

        return  self.__carWord

    def __str__( self ):
        '''pritty printing.'''

        return '%s\n'% self.__carWord
    

######################################################################################


# The following is the MusicWord class.

class MusicWord( object ):
    '''will create words only for music's category.'''

    def __init__( self, musicWord ):
        '''musicWord   -->     will handle a word for the music's category.
        '''
        
        self.__musicWord = musicWord

    def getMusicWord( self ):
        '''will return musicWord.'''

        return  self.__musicWord

    def __str__( self ):
        '''pritty printing.'''

        return '%s\n'% self.__musicWord


######################################################################################


# The following is the CompanyWord class.

class CompanyWord( object ):
    '''will create words only for company's category.'''

    def __init__( self, companyWord ):
        '''companyWord   -->     will handle a word for the company's category.
        '''
        
        self.__companyWord = companyWord

    def getCompanyWord( self ):
        '''will return companyWord.'''

        return  self.__companyWord

    def __str__( self ):
        '''pritty printing.'''

        return '%s\n'% self.__companyWord


######################################################################################


# The following is the HealthWord class.

class HealthWord( object ):
    '''will create words only for health's category.'''

    def __init__( self, healthWord ):
        '''healthWord   -->     will handle a word for the health's category.
        '''
        
        self.__healthWord = healthWord

    def getHealthWord( self ):
        '''will return healthWord.'''

        return  self.__healthWord

    def __str__( self ):
        '''pritty printing.'''

        return '%s\n'% self.__healthWord


######################################################################################


# The following is the InventionWord class.

class InventionWord( object ):
    '''will create words only for invention's category.'''

    def __init__( self, inventionWord ):
        '''inventionWord   -->     will handle a word for the invention's category.
        '''
        
        self.__inventionWord = inventionWord

    def getInventionWord( self ):
        '''will return inventionWord.'''

        return  self.__inventionWord

    def __str__( self ):
        '''pritty printing.'''

        return '%s\n'% self.__inventionWord

    
######################################################################################


# The following is the WritingWord class.

class WritingWord( object ):
    '''will create words only for writing's category.'''

    def __init__( self, writingWord ):
        '''writingWord   -->     will handle a word for the writing's category.
        '''
        
        self.__writingWord = writingWord

    def getLifeWord( self ):
        '''will return writingWord.'''

        return  self.__writingWord

    def __str__( self ):
        '''pritty printing.'''

        return '%s\n'% self.__writingWord


######################################################################################


# The following is the PeopleCategory8Points class.

class PeopleCategory8Points( object ):
    '''will create a list with words only from people category.
       This category is worth 8 points.'''

    def __init__( self, peopleWordsList = [ ] ):
        '''peopleWordsList    -->     will contain people's category words.'''
        
        self.__peopleWordsList = peopleWordsList

    def addPeopleWords( self, word ):
        '''will add words to peopleWordsList.'''

        peopleWord = PeopleWord( word )
        self.__peopleWordsList.append( str( peopleWord ))

    def getPeopleList( self ):
        '''will return the peopleQustionList.'''

        return self.__peopleWordsList

    def __str__( self ):
        '''pritty printing.'''

        strgPeopleWord = ''
        for peopleWord in self.__peopleWordsList:
            strgPeopleWord += peopleWord
        return strgPeopleWord


######################################################################################


# The following is the PeopleCategory6Points class.

class PeopleCategory6Points( object ):
    '''will create a list with words only from people category.
       This category is worth 6 points.'''

    def __init__( self, peopleWordsList = [ ] ):
        '''peopleWordsList    -->     will contain people's category words.'''
        
        self.__peopleWordsList = peopleWordsList

    def addPeopleWords( self, word ):
        '''will add words to peopleWordsList.'''

        peopleWord = PeopleWord( word )
        self.__peopleWordsList.append( str( peopleWord ))

    def getPeopleList( self ):
        '''will return the peopleQustionList.'''

        return self.__peopleWordsList

    def __str__( self ):
        '''pritty printing.'''

        strgPeopleWord = ''
        for peopleWord in self.__peopleWordsList:
            strgPeopleWord += peopleWord
        return strgPeopleWord


######################################################################################


# The following is the PlaceCategory8Points class.

class PlaceCategory8Points( object ):
    '''will create a list with words only from place category.
       This category is worth 8 points.'''

    def __init__( self, placeWordList = [ ] ):
        '''placeWordList    -->     will contain place's category words.'''
        
        self.__placeWordList = placeWordList

    def addPlaceWords( self, word ):
        '''will add words to placeWordList.'''

        placeWord = PlaceWord( word )
        self.__placeWordList.append( str( placeWord ))

    def getPlaceList( self ):
        '''will return the placeWordList.'''

        return self.__placeWordList

    def __str__( self ):
        '''pritty printing.'''

        strgPlaceWord = ''
        for placeWord in self.__placeWordList:
            strgPlaceWord += placeWord
        return strgPlaceWord


######################################################################################


# The following is the PlaceCategory6Points class.

class PlaceCategory6Points( object ):
    '''will create a list with words only from place category.
       This category is worth 6 points.'''

    def __init__( self, placeWordList = [ ] ):
        '''placeWordList    -->     will contain place's category words.'''
        
        self.__placeWordList = placeWordList

    def addPlaceWords( self, word ):
        '''will add words to placeWordList.'''

        placeWord = PlaceWord( word )
        self.__placeWordList.append( str( placeWord ))

    def getPlaceList( self ):
        '''will return the placeWordList.'''

        return self.__placeWordList

    def __str__( self ):
        '''pritty printing.'''

        strgPlaceWord = ''
        for placeWord in self.__placeWordList:
            strgPlaceWord += placeWord
        return strgPlaceWord


######################################################################################


# The following is the PlaceCategory4Points class.

class PlaceCategory4Points( object ):
    '''will create a list with words only from place category.
       This category is worth 4 points.'''

    def __init__( self, placeWordList = [ ] ):
        '''placeWordList    -->     will contain place's category words.'''
        
        self.__placeWordList = placeWordList

    def addPlaceWords( self, word ):
        '''will add words to placeWordList.'''

        placeWord = PlaceWord( word )
        self.__placeWordList.append( str( placeWord ))

    def getPlaceList( self ):
        '''will return the placeWordList.'''

        return self.__placeWordList

    def __str__( self ):
        '''pritty printing.'''

        strgPlaceWord = ''
        for placeWord in self.__placeWordList:
            strgPlaceWord += placeWord
        return strgPlaceWord


######################################################################################


# The following is the SpaceCategory6Points class.

class SpaceCategory6Points( object ):
    '''will create a list with words only from space category.
       This category is worth 6 points.'''

    def __init__( self, spaceWordList = [ ] ):
        '''spaceWordList    -->     will contain space's category words.'''
        
        self.__spaceWordList = spaceWordList

    def addSpaceWords( self, word ):
        '''will add words to spaceWordList.'''

        spaceWord = SpaceWord( word )
        self.__spaceWordList.append( str( spaceWord ))

    def getSpaceList( self ):
        '''will return the spaceWordList.'''

        return self.__spaceWordList

    def __str__( self ):
        '''pritty printing.'''

        strgSpaceWord = ''
        for spaceWord in self.__spaceWordList:
            strgSpaceWord += spaceWord
        return strgSpaceWord


######################################################################################


# The following is the SpaceCategory4Points class.

class SpaceCategory4Points( object ):
    '''will create a list with words only from space category.
       This category is worth 4 points.'''

    def __init__( self, spaceWordList = [ ] ):
        '''spaceWordList    -->     will contain space's category words.'''
        
        self.__spaceWordList = spaceWordList

    def addSpaceWords( self, word ):
        '''will add words to spaceWordList.'''

        spaceWord = SpaceWord( word )
        self.__spaceWordList.append( str( spaceWord ))

    def getSpaceList( self ):
        '''will return the spaceWordList.'''

        return self.__spaceWordList

    def __str__( self ):
        '''pritty printing.'''

        strgSpaceWord = ''
        for spaceWord in self.__spaceWordList:
            strgSpaceWord += spaceWord
        return strgSpaceWord


######################################################################################


# The following is the LifeCategory8Points class.

class LifeCategory8Points( object ):
    '''will create a list with words only from life category.
       This category is worth 8 points.'''

    def __init__( self, lifeWordList = [ ] ):
        '''lifeWordList    -->     will contain life's category words.'''
        
        self.__lifeWordList = lifeWordList

    def addLifeWords( self, word ):
        '''will add words to spaceWordList.'''

        lifeWord = LifeWord( word )
        self.__lifeWordList.append( str( lifeWord ))

    def getLifeList( self ):
        '''will return the lifeWordList.'''

        return self.__lifeWordList

    def __str__( self ):
        '''pritty printing.'''

        strgLifeWord = ''
        for lifeWord in self.__lifeWordList:
            strgLifeWord += lifeWord
        return strgLifeWord


######################################################################################
    

# The following is the LifeCategory6Points class.

class LifeCategory6Points( object ):
    '''will create a list with words only from life category.
       This category is worth 6 points.'''

    def __init__( self, lifeWordList = [ ] ):
        '''lifeWordList    -->     will contain life's category words.'''
        
        self.__lifeWordList = lifeWordList

    def addLifeWords( self, word ):
        '''will add words to spaceWordList.'''

        lifeWord = LifeWord( word )
        self.__lifeWordList.append( str( lifeWord ))

    def getLifeList( self ):
        '''will return the lifeWordList.'''

        return self.__lifeWordList

    def __str__( self ):
        '''pritty printing.'''

        strgLifeWord = ''
        for lifeWord in self.__lifeWordList:
            strgLifeWord += lifeWord
        return strgLifeWord


######################################################################################


# The following is the CurrencyCategory6Points class.

class CurrencyCategory6Points( object ):
    '''will create a list with words only from currency category.
       This category is worth 6 points.'''

    def __init__( self, currencyWordList = [ ] ):
        '''currencyWordList    -->     will contain currency's category words.'''
        
        self.__currencyWordList = currencyWordList

    def addCurrencyWords( self, word ):
        '''will add words to currencyWordList.'''

        currencyWord = CurrencyWord( word )
        self.__currencyWordList.append( str( currencyWord ))

    def getCurrencyList( self ):
        '''will return the currencyWordList.'''

        return self.__currencyWordList

    def __str__( self ):
        '''pritty printing.'''

        strgCurrencyWord = ''
        for currencyWord in self.__currencyWordList:
            strgCurrencyWord += currencyWord
        return strgCurrencyWord


######################################################################################


# The following is the CarCategory4Points class.

class CarCategory4Points( object ):
    '''will create a list with words only from car category.
       This category is worth 4 points.'''

    def __init__( self, carWordList = [ ] ):
        '''carWordList    -->     will contain car's category words.'''
        
        self.__carWordList = carWordList

    def addCarWords( self, word ):
        '''will add words to carWordList.'''

        carWord = CarWord( word )
        self.__carWordList.append( str( carWord ))

    def getCarList( self ):
        '''will return the carWordList.'''

        return self.__carWordList

    def __str__( self ):
        '''pritty printing.'''

        strgCarWord = ''
        for carWord in self.__carWordList:
            strgCarWord += carWord
        return strgCarWord
    

######################################################################################


# The following is the MusicCategory4Points class.

class MusicCategory4Points( object ):
    '''will create a list with words only from music category.
       This category is worth 4 points.'''

    def __init__( self, musicWordList = [ ] ):
        '''musicWordList    -->     will contain music's category words.'''
        
        self.__musicWordList = musicWordList

    def addMusicWords( self, word ):
        '''will add words to musicWordList.'''

        musicWord = MusicWord( word )
        self.__musicWordList.append( str( musicWord ))

    def getMusicList( self ):
        '''will return the musicWordList.'''

        return self.__musicWordList

    def __str__( self ):
        '''pritty printing.'''

        strgMusicWord = ''
        for musicWord in self.__musicWordList:
            strgMusicWord += musicWord
        return strgMusicWord
    

######################################################################################


# The following is the CompanyCategory4Points class.

class CompanyCategory4Points( object ):
    '''will create a list with words only from company category.
       This category is worth 4 points.'''

    def __init__( self, companyWordList = [ ] ):
        '''companyWordList    -->     will contain company's category words.'''
        
        self.__companyWordList = companyWordList

    def addCompanyWords( self, word ):
        '''will add words to companyWordList.'''

        companyWord = CompanyWord( word )
        self.__companyWordList.append( str( companyWord ))

    def getCompanyList( self ):
        '''will return the companyWordList.'''

        return self.__companyWordList

    def __str__( self ):
        '''pritty printing.'''

        strgCompanyWord = ''
        for companyWord in self.__companyWordList:
            strgCompanyWord += companyWord
        return strgCompanyWord


######################################################################################


# The following is the HealthCategory4Points class.

class HealthCategory4Points( object ):
    '''will create a list with words only from health category.
       This category is worth 4 points.'''

    def __init__( self, healthWordList = [ ] ):
        '''healthWordList    -->     will contain health's category words.'''
        
        self.__healthWordList = healthWordList

    def addHealthWords( self, word ):
        '''will add words to healthWordList.'''

        healthWord = HealthWord( word )
        self.__healthWordList.append( str( healthWord ))

    def getHealthList( self ):
        '''will return the healthWordList.'''

        return self.__healthWordList

    def __str__( self ):
        '''pritty printing.'''

        strgHealthWord = ''
        for healthWord in self.__healthWordList:
            strgHealthWord += healthWord
        return strgHealthWord


######################################################################################


# The following is the InventionCategory4Points class.

class InventionCategory4Points( object ):
    '''will create a list with words only from invention category.
       This category is worth 4 points.'''

    def __init__( self, inventionWordList = [ ] ):
        '''inventionWordList    -->     will contain invention's category words.'''
        
        self.__inventionWordList = inventionWordList

    def addInventionWords( self, word ):
        '''will add words to inventionWordList.'''

        inventionWord = InventionWord( word )
        self.__inventionWordList.append( str( inventionWord ))

    def getInventionList( self ):
        '''will return the inventionWordList.'''

        return self.__inventionWordList

    def __str__( self ):
        '''pritty printing.'''

        strgInventionWord = ''
        for inventionWord in self.__inventionWordList:
            strgInventionWord += inventionWord
        return strgInventionWord
    

######################################################################################


# The following is the WritingCategory10Points class.

class WritingCategory10Points( object ):
    '''will create a list with words only from writing category.
       This category is worth 10 points.'''

    def __init__( self, writingWordList = [ ] ):
        '''writingWordList    -->     will contain writing's category words.'''
        
        self.__writingWordList = writingWordList

    def addWritingWords( self, word ):
        '''will add words to writingWordList.'''

        writingWord = WritingWord( word )
        self.__writingWordList.append( str( writingWord ))

    def getWritingList( self ):
        '''will return the writingWordList.'''

        return self.__writingWordList

    def __str__( self ):
        '''pritty printing.'''

        strgWritingWord = ''
        for writingWord in self.__writingWordList:
            strgWritingWord += writingWord
        return strgWritingWord


######################################################################################


# DEFINING MAIN FUNCTIONS


def createPeopleWords8Points():
    '''will create words for the people's category.
       This funtion is worth 8 points.'''

    peopleWord = PeopleCategory8Points()
    
    peopleWord.addPeopleWords( '8 POINT PEOPLE WORD' )
    peopleWord.addPeopleWords( '8 POINT PEOPLE WORD ' )
    peopleWord.addPeopleWords( '8 POINT PEOPLE WORD' )

    print peopleWord


def createPeopleWords6Points():
    '''will create words for the people's category.
       This funtion is worth 6 points.'''

    peopleWord = PeopleCategory6Points()
    
    peopleWord.addPeopleWords( '6 POINT PEOPLE WORD' )
    peopleWord.addPeopleWords( '6 POINT PEOPLE WORD' )
    peopleWord.addPeopleWords( '6 POINT PEOPLE WORD' )

    print peopleWord


def createPlaceWords8Points():
    '''will create words for the place's category.
       This funtion is worth 8 points'''

    placeWord = PlaceCategory8Points()
    
    placeWord.addPlaceWords( '8 POINT PLACE WORD' )
    placeWord.addPlaceWords( '8 POINT PLACE WORD' )
    placeWord.addPlaceWords( '8 POINT PLACE WORD' )

    print placeWord


def createPlaceWords6Points():
    '''will create words for the place's category.
       This funtion is worth 6 points'''

    placeWord = PlaceCategory6Points()
    
    placeWord.addPlaceWords( '6 POINT PLACE WORD' )
    placeWord.addPlaceWords( '6 POINT PLACE WORD' )
    placeWord.addPlaceWords( '6 POINT PLACE WORD' )

    print placeWord

def createPlaceWords4Points():
    '''will create words for the place's category.
       This funtion is worth 4 points'''

    placeWord = PlaceCategory4Points()
    
    placeWord.addPlaceWords( '4 POINT PLACE WORD' )
    placeWord.addPlaceWords( '4 POINT PLACE WORD' )
    placeWord.addPlaceWords( '4 POINT PLACE WORD' )

    print placeWord


def createSpaceWords8Points():
    '''will create words for the space's category.
       This funtion is worth 8 points'''

    spaceWord = SpaceCategory8Points()
    
    spaceWord.addSpaceWords( '8 POINT SPACE WORD' )
    spaceWord.addSpaceWords( '8 POINT SPACE WORD' )
    spaceWord.addSpaceWords( '8 POINT SPACE WORD' )

    return spaceWord


def createSpaceWords6Points():
    '''will create words for the space's category.
       This funtion is worth 6 points'''

    spaceWord = SpaceCategory6Points()
    
    spaceWord.addSpaceWords( '6 POINT SPACE WORD' )
    spaceWord.addSpaceWords( '6 POINT SPACE WORD' )
    spaceWord.addSpaceWords( '6 POINT SPACE WORD' )

    print spaceWord


def createSpaceWords4Points():
    '''will create words for the space's category.
       This funtion is worth 4 points'''

    spaceWord = SpaceCategory4Points()
    
    spaceWord.addSpaceWords( '4 POINT SPACE WORD' )
    spaceWord.addSpaceWords( '4 POINT SPACE WORD' )
    spaceWord.addSpaceWords( '4 POINT SPACE WORD' )

    print spaceWord

def createLifeWords8Points():
    '''will create words for the life's category.
       This funtion is worth 8 points'''

    lifeWord = LifeCategory8Points()
    
    lifeWord.addLifeWords( '8 POINT LIFE WORD' )
    lifeWord.addLifeWords( '8 POINT LIFE WORD' )
    lifeWord.addLifeWords( '8 POINT LIFE WORD' )

    print lifeWord


def createLifeWords6Points():
    '''will create words for the life's category.
       This funtion is worth 6 points'''

    lifeWord = LifeCategory6Points()
    
    lifeWord.addLifeWords( '6 POINT LIFE WORD' )
    lifeWord.addLifeWords( '6 POINT LIFE WORD' )
    lifeWord.addLifeWords( '6 POINT LIFE WORD' )

    print lifeWord


def createLifeWords4Points():
    '''will create words for the life's category.
       This funtion is worth 4 points'''

    lifeWord = LifeCategory4Points()
    
    lifeWord.addLifeWords( '4 POINT LIFE WORD' )
    lifeWord.addLifeWords( '4 POINT LIFE WORD' )
    lifeWord.addLifeWords( '4 POINT LIFE WORD' )

    return lifeWord


def createCurrencyWords6Points():
    '''will create words for the currency's category.
       This funtion is worth 6 points'''

    currencyWord = CurrencyCategory6Points()
    
    currencyWord.addCurrencyWords( '6 POINT CURRENCY WORD' )
    currencyWord.addCurrencyWords( '6 POINT CURRENCY WORD' )
    currencyWord.addCurrencyWords( '6 POINT CURRENCY WORD' )

    print currencyWord


def createCarWords4Points():
    '''will create words for the car's category.
       This funtion is worth 4 points'''

    carWord = CarCategory4Points()
    
    carWord.addCarWords( '4 POINT CAR WORD' )
    carWord.addCarWords( '4 POINT CAR WORD' )
    carWord.addCarWords( '4 POINT CAR WORD' )

    print carWord


def createMusicWords4Points():
    '''will create words for the music's category.
       This funtion is worth 4 points'''

    musicWord = MusicCategory4Points()
    
    musicWord.addMusicWords( '4 POINT MUSIC WORD' )
    musicWord.addMusicWords( '4 POINT MUSIC WORD' )
    musicWord.addMusicWords( '4 POINT MUSIC WORD' )

    print musicWord


def createCompanyWords4Points():
    '''will create words for the company's category.
       This funtion is worth 4 points'''

    companyWord = CompanyCategory4Points()
    
    companyWord.addCompanyWords( '4 POINT COMPANY WORD' )
    companyWord.addCompanyWords( '4 POINT COMPANY WORD' )
    companyWord.addCompanyWords( '4 POINT COMPANY WORD' )

    print companyWord


def createHealthWords4Points():
    '''will create words for the health's category.
       This funtion is worth 4 points'''

    healthWord = HealthCategory4Points()
    
    healthWord.addHealthWords( '4 POINT HEALTH WORD' )
    healthWord.addHealthWords( '4 POINT HEALTH WORD' )
    healthWord.addHealthWords( '4 POINT HEALTH WORD' )

    print healthWord


def createInventionWords4Points():
    '''will create words for the invention's category.
       This funtion is worth 4 points'''

    inventionWord = InventionCategory4Points()
    
    inventionWord.addInventionWords( '4 POINT INVENTION WORD' )
    inventionWord.addInventionWords( '4 POINT INVENTION WORD' )
    inventionWord.addInventionWords( '4 POINT INVENTION WORD' )

    print inventionWord

    
def createWritingCategory10Points():
    '''will create words for the writing's category.
       This funtion is worth 10 points'''

    writingWord = WritingCategory10Points()
    
    writingWord.addWritingWords( '10 POINT WRITING WORD' )
    writingWord.addWritingWords( '10 POINT WRITING WORD' )
    writingWord.addWritingWords( '10 POINT WRITING WORD' )

    print writingWord


def gameRules():
    '''will introduce students with the game rules.'''

    print 'RULES:'
    print '*******************************************************'
    print '--> 1. PLAYER WILL CHOSE A CATAGORY'
    print '--> 2. EACH CATAGORY WILL HAVE THREE WORD'
    print '--> 3. DIFFERENT CATAGORY HOLDS DIFFERENT AMOUNT OF POINTS'
    print '--> 4. YOU MUST GET ALL THREE ANSWER RIGHT TO CLAIM ALL POINTS'
    print '--> 5. YOU WILL GET THREE MINUTES TO ANSWER ALL THREE ITEM'
    print '--> 6. IF YOU GO OVER TIME, NEXT TEAM GET TO TAKE A SHOT AT GETTING FULL POINTS FOR ONE MINUTE. IF THEY FAIL, FIRST TEAM CONTAIN THE POINTS'
    print '--> 7. YOU MUST NOT USE BANNED CLUES TO EXLPAIN THE WORDS'
    print '********************************************************'

   
def userPick():
    '''will get the user category.'''

    print "\nLET'S PLAY AND HAVE FUN!\n\n"

    print '\t\t\tWRITING'
    print '\t\t\t( 10 )\n'

    print '\t\tPEOPLE\tPLACE\tLIFE'
    print '\t\t( 8 )\t( 8 )\t( 8 )\n'

    print '\tLIFE\tPLACE\tSPACE\tPEOPLE\tCURRENCY'
    print '\t( 6 )\t( 6 )\t( 6 )\t( 6 )\t ( 6 )\n'

    print 'CARS\tSPACE\tMUSIC\tPLACE\tCOMPANIES   HEALTH   INVENTION'
    print '( 4 )\t( 4 )\t( 4 )\t( 4 )\t  ( 4 )\t     ( 4 )     ( 4 )\n'

    userChoice = raw_input( 'Please, choose a category, or press 3 to jump back to menu choices: ' )

    while ( userChoice != EXIT ):

        if (( userChoice == WRITING_10.lower() ) or ( userChoice == WRITING_10.upper() )):
            print 'This category is worth 10 points.\n'
            createWritingCategory10Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]


        elif (( userChoice == PEOPLE_8.lower() ) or ( userChoice == PEOPLE_8.upper() )):
            print 'This category is worth 8 points.\n'
            createPeopleWords8Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]

        elif (( userChoice == PLACE_8.lower() ) or ( userChoice == PLACE_8.upper() )):
            print 'This category is worth 8 points.\n'
            createPlaceWords8Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]

        elif (( userChoice == LIFE_8.lower() ) or ( userChoice == LIFE_8.upper() )):
            print 'This category is worth 8 points.\n'
            createLifeWords8Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]

        elif (( userChoice == LIFE_6.lower() ) or ( userChoice == LIFE_6.upper() )):
            print 'This category is worth 6 points.\n'
            createLifeWords6Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]


        elif (( userChoice == PLACE_6.lower() ) or ( userChoice == PLACE_6.upper() )):
            print 'This category is worth 6 points.\n'
            createPlaceWords6Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]

        elif (( userChoice == SPACE_6.lower() ) or ( userChoice == SPACE_6.upper() )):
            print 'This category is worth 6 points.\n'
            createSpaceWords6Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]

        elif (( userChoice == PEOPLE_6.lower() ) or ( userChoice == PEOPLE_6.upper() )):
            print 'This category is worth 6 points.\n'
            createPeopleWords6Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]


        elif (( userChoice == CURRENCY_6.lower() ) or ( userChoice == CURRENCY_6.upper() )):
            print 'This category is worth 6 points.\n'
            createCurrencyWords6Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]


        elif (( userChoice == CARS_4.lower() ) or ( userChoice == CARS_4.upper() )):
            print 'This category is worth 4 points.\n'
            createCarWords4Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]


        elif (( userChoice == SPACE_4.lower() ) or ( userChoice == SPACE_4.upper() )):
            print 'This category is worth 4 points.\n'
            createSpaceWords4Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]

        elif (( userChoice == MUSIC_4.lower() ) or ( userChoice == MUSIC_4.upper() )):
            print 'This category is worth 4 points.\n'
            createMusicWords4Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]

        elif (( userChoice == PLACE_4.lower() ) or ( userChoice == PLACE_4.upper() )):
            print 'This category is worth 4 points.\n'
            createPlaceWords4Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]


        elif (( userChoice == COMPANIES_4.lower() ) or ( userChoice == COMPANIES_4.upper() )):
            print 'This category is worth 4 points.\n'
            createCompanyWords4Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]

        elif (( userChoice == HEALTH_4.lower() ) or ( userChoice == HEALTH_4.upper() )):
            print 'This category is worth 4 points.\n'
            createHealthWords4Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]

        elif (( userChoice == INVENTION_4.lower() ) or ( userChoice == INVENTION_4.upper() )):
            print 'This category is worth 4 points.\n'
            createInventionWords4Points()
            print 'Time is running...'
            print 'Time Remaining: 03:00'
            for times in range(len(TIME_LIST)):
                time.sleep(30)
                print TIME_LIST[times]
                
        else:
            print 'The category entered does not exist.'

        
        userChoice = raw_input( 'Please, choose another category: ' )


def playTabooGame():
    '''will play the game.'''

    print '[ W|E|L|C|O|M|E| |T|O| |T|A|B|O|O| |G||A|M|E| |!|!|!| ]\n'
    print '\a\aGAME MENU\a\a\n'
    print '1\x11 PLAY GAME'
    print '2\x11 GAME RULES'
    print '3\x11 QUIT'

    studentChoice = raw_input( '\nPlease, enter your choice: ')
    while ( studentChoice != EXIT ):

        if (studentChoice == STUDENT_CHOICE_1):
            userPick()
        
        elif (studentChoice == STUDENT_CHOICE_2):
            gameRules()

        else:
            print 'The choice entered is not ofered in the menu.'
        
        studentChoice = raw_input( '\nPlease, enter one of the choices shown in the menu: ' )
        

def main():
    
    playTabooGame()
            
main()
