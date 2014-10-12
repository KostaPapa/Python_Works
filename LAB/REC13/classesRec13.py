"""

User Name: kpapa01

Programmer: Kostaq Papa

Rec#: rec13

Course No: CS 1114
Section: C

"""


class PointData( object ):
    '''This class will change create points.'''


    def __init__( self, xPos = 0, yPos = 0 ):
        '''This funtion will show initialize the coordinates of x and y.'''

        if (type(xPos) is float and type(yPos)):
            self.__xCoordinate = (xPos)
            self.__yCoordinate = (yPos)

    def expandCoordinate( self ):
        
        return self.__xCoordinate
        
    
    def expandXYCoordinates ( self, expandValue ):
        '''This funtion will expand the x and y coordinate with the same value.'''

        self.__xCoordinate += expandValue
        self.__yCoordinate += expandValue

    def __str__( self ):
        '''This funtion will print the coordinates.'''
        
        expandedCoordinates = "( %.5f , %.5f )" %(self.__xCoordinate, self.__yCoordinate)
        return expandedCoordinates
    
class Quadrants( object ):
    '''This class will put the points in the right quadrants.'''

    def __init__ ( self, newValue ):
        '''This funtion will initialize the points with a new value. '''
        self.__allXYPoints = newValue

    def __str__ ( self ):
        '''This funtion will print the point.'''
        return "Quadrant: %s" %self.__allXYPoints

class Segments( object ):
    '''This class will create a segments.'''

    def __init__( self, firstPoint, secondPoint ):
        '''This funtion will initialize the starting and ending points of a segment.'''

        self.__startingPoint = firstPoint
        self.__endingPoint = secondPoint        

    def __str__( self ):
        '''This funtion will print the starting and ending point.'''
        return "Starting Point of the segment is: %s \nEnding Point of the segment is: %s"%( self.__startingPoint, self.__endingPoint )

class DistanceFromOrigin ( object ):
    '''This class will be used to calc the distance of a point from origin. '''

    def __init__( self, firstPoint, secondPoint ):
        '''This funtion will initialize two (x,y) points '''

        self.__firstPointDistance = firstPoint
        self.__secondPointDistance = secondPoint
        

    def __str__( self ):
        '''This funtion will print the distance.'''

        return "The distance form origin of the first point is: %s \nThe distance from origin of the second point is: %s"%( self.__firstPointDistance , self.__secondPointDistance )





