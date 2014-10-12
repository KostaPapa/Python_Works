"""

User Name: kpapa01

Programmer: Kostaq Papa

Rec#: rec13

Course No: CS 1114
Section: C

"""



from classesRec13 import PointData, Quadrants, Segments, DistanceFromOrigin
import math

def createFirstPoint():
    '''This funtion will create a point from a file.'''

    # Point from pts001.pts filename.

    pts001FileName = open( 'pts001.pts.txt','r' )
    xPos001 = 0
    yPos001 = 0

    for coordinates001 in pts001FileName:
        xyPos001 = coordinates001.split( )
        xCoordinate001 = float(xyPos001[ 0 ])
        yCoordinate001 = float(xyPos001[ 1 ])
        xPos001 += xCoordinate001
        yPos001 += yCoordinate001
    point001 = PointData( xPos001, yPos001 )
    pts001FileName.close()
    print "The point from pts001.pts filename is: ", point001
    file001Point( xPos001 , yPos001 )
    return xPos001,yPos001,point001


def createSecondPoint():
    '''This funtion will create a point from a file.'''
    
    # Point from pts003.pts filename.
    
    pts003FileName = open( 'pts003.pts.txt','r' )
    xPos003 = 0
    yPos003 = 0

    for coordinates003 in pts003FileName:
        xyPos003 = coordinates003.split( )
        xCoordinate003 = float(xyPos003[ 0 ])
        yCoordinate003 = float(xyPos003[ 1 ])
        xPos003 += xCoordinate003
        yPos003 += yCoordinate003
    point003 = PointData( xPos003, yPos003 )
    pts003FileName.close()
    print "The point from pts003.pts filename is: ", point003
    file003Point( xPos003 , yPos003 )
    return xPos003,yPos003,point003

    
def file001Point( xPos001, yPos001 ):
    '''This funtion will put x and y points of the pts001.pts filename in right quadrants.'''

    # Testing Coordinates for the pts000.pts filename.

    
    if (( xPos001 >= 0 ) and ( yPos001 >= 0 )):            
        print "This point is in the I Quadrant."
            
    elif (( xPos001 <= 0 ) and ( yPos001 >= 0 )):
        print "This point is in the II Quadrant."

    elif (( xPos001 <= 0) and ( yPos001 <= 0 )):
        print "This point is in the III Quadrant."
            
    else: # ((xPos001 >= 0) and (yPos001 <= 0 )):
        print "This point is in the IV Quadrant."

    point001 = Quadrants(file001Point)

def file003Point( xPos003 , yPos003 ):
    '''This funtion will put x and y points of the pts003.pts filename in right quadrants.'''

    # Testing Coordinates for the pts000.pts filename.

    
    if (( xPos003 >= 0 ) and ( yPos003 >= 0 )):            
        print "This point is in the I Quadrant."
            
    elif (( xPos003 <= 0 ) and ( yPos003 >= 0 )):
        print "This point is in the II Quadrant."

    elif (( xPos003 <= 0) and ( yPos003 <= 0 )):
        print "This point is in the III Quadrant."
            
    else: # ((xPos003 >= 0) and (yPos003 <= 0 )):
        print "This point is in the IV Quadrant."

    point003 = Quadrants(file003Point) 
    
def lineSegment( point001 , point003 ):
    '''This funtion will display the starting and ending point of the segment.'''

    line = Segments( point001 , point003 )
    print line
    return line

def calcDistance( xPos001 , yPos001, xPos003 , yPos003 ):
    '''This function will calculate the distance of each point form origin.'''

    point001 = math.sqrt( math.pow( xPos001 , 2 ) + math.pow( yPos001 , 2 ) )
    point003 = math.sqrt( math.pow( xPos003 , 2 ) + math.pow( yPos003 , 2 ) )

    distance = DistanceFromOrigin( point001, point003 )
    print distance

def createSegmentFile( line ):
    '''This function will create a file that will contain data for segments.'''

    segmentFileName = open('segmentData.txt','w')
    segmentFileName.write( 'Below you will find information about a line.\n\n' )
    segmentFileName.write( str(line) )
    segmentFileName.close()

                
def main():

    x001,y001,pointFile001 = createFirstPoint( )
    x003,y003,pointFile003 = createSecondPoint( )
    lineInfo = lineSegment( pointFile001 , pointFile003)
    calcDistance( x001 , y001 , x003 , y003 )
    createSegmentFile(lineInfo)
    
    
main()
