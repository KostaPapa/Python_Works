import random

def headsORtails():
    '''This funtion with choose randomly 10 time if there is a head or tail when a coin is flipped 10 timw.'''

    for n in range(10):
        if (random.randint(0,1) == 0):
            print "HEADS"
        else:
            print "TAILS"


def main():

    headsORtails()

main()
