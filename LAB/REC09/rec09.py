"""

User Name: kpapa01

Programmer: Kostaq Papa

Purpose of this program: Calc thr weighted score.

Constrains: 


"""

STOP = ['z','e','b','r','a','Z','E','B','R','A']

def getUserWords():
    '''This function will get user words.'''

    print "Below you will be requsted to enter your words."
    print "Enter one word per line."
    print "Type zebra when finished entering words."

    getWords = raw_input("Enter words:")

    while (getWords not in STOP):
        getWords = raw_input("Enter words:")

def main():

    getUserWords()
main()
