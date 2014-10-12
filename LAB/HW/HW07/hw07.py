#!C:\Users\kpapa01\Desktop\Python\hw\hw07.exe

''' 

cs1114 

Submission: hw07

Programmer: Kostaq Papa
Username: kpapa01
ID Number: 0412768

Purpose of program: The purpose of this program is to read the data from a file and produce two files that will hold basic information.


'''

PERIOD_1970_1990 = '1970-1990'  # This would be used to process data only for the period 1970 - 1990.
PERIOD_1990_2007 = '1990-2007'  # This would be used to process data only for the period 1990 - 2007.




import os


def CalcAverageFor1970_1990Period():
    '''This funtion will calculate the average percentage change over all countries for period 1970 - 1990.'''

    
    countNoOfCountries_1970_1990 = 0
    totalPercentChange_1970_1990 = 0
    listOfFloatNumber_1970_1990 = []


    if os.path.exists('WorldPopulationChange.txt'):

        worldPopulationFile = open('WorldPopulationChange.txt','r')
        firstLine = worldPopulationFile.readline()
        
        for lines in worldPopulationFile:
            splitedLine = lines.split()
            if (PERIOD_1970_1990 in splitedLine):
                popLastElement = splitedLine.pop()
                floatNumber = float(popLastElement[:(len(popLastElement) - 1)])
                listOfFloatNumber_1970_1990.append(floatNumber)
                countNoOfCountries_1970_1990 += 1
                totalPercentChange_1970_1990 += floatNumber

        worldPopulationFile.close()

        averagePercentChange_1970_1990 = (totalPercentChange_1970_1990 / countNoOfCountries_1970_1990)
        return averagePercentChange_1970_1990, listOfFloatNumber_1970_1990
    
    
def Max_Min_PercentChangeFor1970_1990Period(averagePercentChange_1970_1990, listOfFloatNumber_1970_1990):
    '''This function will find three countries with the largest and smallest percentage change and will write them into the 1970_1990_summary.txt filename. The data are processed only for 1970 - 1990 period.'''
    
    # The calculation of three countries with the largest percentage change.

    higherMaxNo = 0
    mediumMaxNo = 0    
    lowerMaxNo = 0

    firstNo = -1
    secondNo = -1
    thirdNo = -1
            
    for index in range(len(listOfFloatNumber_1970_1990)):
        positiveFloat = abs(listOfFloatNumber_1970_1990[index])

        if (positiveFloat > firstNo):
            thirdNo = secondNo
            lowerMaxNo = mediumMaxNo
            secondNo = firstNo
            mediumMaxNo = higherMaxNo
            firstNo = positiveFloat
            higherMaxNo = firstNo
            
        elif (positiveFloat > secondNo):
            thirdNo = secondNo
            lowerMaxNo = mediumMaxNo
            secondNo = positiveFloat
            mediumMaxNo = secondNo

        elif (positiveFloat > thirdNo):
            thirdNo = positiveFloat
            lowerMaxNo = thirdNo

    if os.path.exists('WorldPopulationChange.txt'):
        
        worldPopulationFile = open('WorldPopulationChange.txt','r')
        firstLine = worldPopulationFile.readline()

        summary1970_1990File = open('1970_1990_summary.txt','w')
        if os.path.exists( '1970_1990_summary.txt' ):

            summary1970_1990File.write("1970 - 1990 Summary Report\n\n") 
            summary1970_1990File.write("The average percent change over all countries: " + str(averagePercentChange_1970_1990) + " %\n\n")
            summary1970_1990File.write("The countries with the three largest percentage change are: \n")
            
            for lines in worldPopulationFile:
                splitedLine = lines.split()
                if (PERIOD_1970_1990 in splitedLine):
                    stripPercent = abs(float(splitedLine[len(splitedLine) - 1].strip("%")))
                    if (stripPercent == higherMaxNo) or (stripPercent == mediumMaxNo) or (stripPercent == lowerMaxNo):
                        summary1970_1990File.write(lines)

            summary1970_1990File.close()
               

    # The calculation of three countries with the smallest percentage change.

    lowerMinNo = 0
    mediumMinNo = 0
    higherMinNo = 0

    firstNo = 99
    secondNo = 99
    thirdNo = 99
    
    for index in range(len(listOfFloatNumber_1970_1990)):
        positiveFloat = abs(listOfFloatNumber_1970_1990[index])

        if (positiveFloat < firstNo):
            thirdNo = secondNo
            higherMinNo = mediumMinNo
            secondNo = firstNo
            mediumMinNo = lowerMinNo
            firstNo = positiveFloat
            lowerMinNo = firstNo
            
        
        elif (positiveFloat < secondNo):
            thirdNo = secondNo
            higherMinNo = mediumMinNo
            secondNo = positiveFloat
            mediumMinNo = secondNo
            

        elif (positiveFloat < thirdNo):
            thirdNo = positiveFloat
            higherMinNo = thirdNo

    if os.path.exists('WorldPopulationChange.txt'):

        worldPopulationFile = open('WorldPopulationChange.txt','r')
        firstLine = worldPopulationFile.readline()

        summary1970_1990File = open('1970_1990_summary.txt','a')
        summary1970_1990File.write("\nThe countries with the three smallest percentage change are: \n")
            
        for lines in worldPopulationFile:
            splitedLine = lines.split()
            if (PERIOD_1970_1990 in splitedLine):
                stripPercent = abs(float(splitedLine[len(splitedLine) - 1].strip("%")))
                if (stripPercent == lowerMinNo) or (stripPercent == mediumMinNo) or (stripPercent == higherMinNo):
                    summary1970_1990File.write(lines)

        summary1970_1990File.close()
            
    
def CalcAverageFor1990_2007Period():
    '''This funtion will calculate the average percentage change over all countries for period 1990 - 2007.'''

    countNoOfCountries_1990_2007 = 0
    totalPercentChange_1990_2007 = 0
    listOfFloatNumber_1990_2007 = []
      
    if os.path.exists('WorldPopulationChange.txt'):
        
        worldPopulationFile = open('WorldPopulationChange.txt','r')
        firstLine = worldPopulationFile.readline()
    
        for lines in worldPopulationFile:
            splitedLine = lines.split()
            if (PERIOD_1990_2007 in splitedLine):
                popLastElement = splitedLine.pop()
                floatNumber = float(popLastElement[:(len(popLastElement) - 1)])
                listOfFloatNumber_1990_2007.append(floatNumber)
                countNoOfCountries_1990_2007 += 1
                totalPercentChange_1990_2007 += floatNumber

        worldPopulationFile.close()    

        averagePercentChange_1990_2007 = (totalPercentChange_1990_2007 / countNoOfCountries_1990_2007)

        return averagePercentChange_1990_2007, listOfFloatNumber_1990_2007
    else:
        print "File does not exist."

def Max_Min_PercentChangeFor1990_2007Period(averagePercentChange_1990_2007, listOfFloatNumber_1990_2007):
    '''This function will find three countries with the largest and smallest change for period 1990 - 2007 and will write them in the 1990_2007_summary.txt filename.'''
    
    # The calculation of the three largest percentage change.

    higherMaxNo = 0
    mediumMaxNo = 0    
    lowerMaxNo = 0

    firstNo = -1
    secondNo = -1
    thirdNo = -1
            
    for index in range(len(listOfFloatNumber_1990_2007)):
        positiveFloat = abs(listOfFloatNumber_1990_2007[index])

        if (positiveFloat > firstNo):
            thirdNo = secondNo
            lowerMaxNo = mediumMaxNo
            secondNo = firstNo
            mediumMaxNo = higherMaxNo
            firstNo = positiveFloat
            higherMaxNo = firstNo
            
        elif (positiveFloat > secondNo):
            thirdNo = secondNo
            lowerMaxNo = mediumMaxNo
            secondNo = positiveFloat
            mediumMaxNo = secondNo

        elif (positiveFloat > thirdNo):
            thirdNo = positiveFloat
            lowerMaxNo = thirdNo
            
    if os.path.exists('WorldPopulationChange.txt'):
        worldPopulationFile = open('WorldPopulationChange.txt','r')
        firstLine = worldPopulationFile.readline()

        summary1990_2007File = open('1990_2007_summary.txt','w')
        if os.path.exists('1990_2007_summary.txt'):
            summary1990_2007File.write("1990 - 2007 Summary Report\n\n") 
            summary1990_2007File.write("The average percent change over all countries: " + str(averagePercentChange_1990_2007) + " %\n\n")
            summary1990_2007File.write("The countries with the three largest percentage change are: \n")
            
            for lines in worldPopulationFile:
                splitedLine = lines.split()
                if (PERIOD_1990_2007 in splitedLine):
                    stripPercent = abs(float(splitedLine[len(splitedLine) - 1].strip("%")))
                    if (stripPercent == higherMaxNo) or (stripPercent == mediumMaxNo) or (stripPercent == lowerMaxNo):
                        summary1990_2007File.write(lines)

            summary1990_2007File.close()
                

    # The calculation of the three smallest percentage change.

    lowerMinNo = 0
    mediumMinNo = 0
    higherMin = 0

    firstNo = 99
    secondNo = 99
    thirdNo = 99
    
    for index in range(len(listOfFloatNumber_1990_2007)):
        positiveFloat = abs(listOfFloatNumber_1990_2007[index])

        if (positiveFloat < firstNo):
            thirdNo = secondNo
            higherMin = mediumMinNo
            secondNo = firstNo
            mediumMinNo = lowerMinNo
            firstNo = positiveFloat
            lowerMinNo = firstNo
            
        
        elif (positiveFloat < secondNo):
            thirdNo = secondNo
            higherMin = mediumMinNo
            secondNo = positiveFloat
            mediumMinNo = secondNo
            

        elif (positiveFloat < thirdNo):
            thirdNo = positiveFloat
            higherMin = thirdNo


    if os.path.exists('WorldPopulationChange.txt'):
        
        worldPopulationFile = open('WorldPopulationChange.txt','r')
        firstLine = worldPopulationFile.readline()

        summary1990_2007File = open('1990_2007_summary.txt','a')
        summary1990_2007File.write("\nThe countries with the three smallest percentage change are: \n")

    
        for lines in worldPopulationFile:
            splitedLine = lines.split()
            if (PERIOD_1990_2007 in splitedLine):
                sripPercent = abs(float(splitedLine[len(splitedLine) - 1].strip("%")))
                if (sripPercent == lowerMinNo) or (sripPercent == mediumMinNo) or (sripPercent == higherMin):
                    summary1990_2007File.write(lines)

        summary1990_2007File.close()

def processForSelectedData():
    
    average1970_1990, floatNoList = CalcAverageFor1970_1990Period()
    Max_Min_PercentChangeFor1970_1990Period(average1970_1990, floatNoList)
            
    average1990_2007, floatNoList = CalcAverageFor1990_2007Period()
    Max_Min_PercentChangeFor1990_2007Period(average1990_2007, floatNoList)   

def main():

    processForSelectedData()

# are we being executed?
if __name__ == '__main__':
    main()
