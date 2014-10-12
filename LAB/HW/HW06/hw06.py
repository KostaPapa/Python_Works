#!C:\Users\kpapa01\Desktop\Python\hw\hw06.exe

''' 
cs1114 

Submission: hw06

Programmer: Kostaq Papa
Username: kpapa01
ID Number: 0412768

Purpose of program: The purpose of this program is find the average of data the transmitted by a Robot form Neptune.


'''

NUMBERS = "0123456789"      # The data points will be numbers form 0 to 9.
PERCENTAGE = 100            # This constant will be used to calculate the percentage.




def sucesfullyRobotLand():
    '''This funtion will notify the "MAIN CENTER" that the robot has made a successful landing.'''


    print "THIS IS ROBOT SPEAKING."
    print "I SUCCESSFULLY LANDED IN NEPTUNE\n"
    
    

def getRobotWord():
    '''This funtion will get the robot message.'''

    stringTransmited = raw_input("Robot is transmitting this string: ")

    return stringTransmited

def readTheDataPoints(stringTransmited):
    '''This funtion will read and print only the valid data points. They will be in group of three.'''

    
    tempList = []
    validDataList = []
    countOfCorruptData = 0
    
    for char in range(len(stringTransmited)):

        if (stringTransmited[char] in NUMBERS):
            tempList.append(stringTransmited[char])

        elif (len(tempList) != 3):
            if (len(tempList) != 0):
               countOfCorruptData = countOfCorruptData + 1 
            tempList = []
                         

        else: # (len(tempList) == 3)
            validData = ''.join(tempList)
            validDataList.append(validData)
            tempList = []

    print validDataList            

    return validDataList, countOfCorruptData   

def calcAverage(validDataList):
    '''This funtion will calculate the average of valid data trasmitted.'''

    sumOfValidData = 0

    for element in  range(len(validDataList)):
        sumOfValidData = sumOfValidData + int(validDataList[element])

    average = (float(sumOfValidData)) / (float(len(validDataList)))

    print "\nThe average of the data transimitted is: ",average


def calcPercentage(validDataList, countOfCorruptData, stringTransmited):
    '''This funtion will calculate the percentage of the corrupted data.'''

    totalOfCorruptData = 0

    for element in range(len(validDataList)):
        totalOfCorruptData = totalOfCorruptData + countOfCorruptData

    percentage = (float(totalOfCorruptData)/float(len(stringTransmited))) * PERCENTAGE

    print "The percentage of corrupted Data is: %",percentage
    
def main():

    sucesfullyRobotLand()
    robotTransmition = getRobotWord()
    threeDigitIntList, dataCorrupt = readTheDataPoints(robotTransmition)
    calcAverage(threeDigitIntList)
    calcPercentage(threeDigitIntList, dataCorrupt, robotTransmition)

# are we being executed?
if __name__ == '__main__':
    main()
