def getUserString():

    enterStr = raw_input("Enter a string: ")

    return enterStr

def infoAboutUserStr(enterStr):

    if enterStr.isalnum():
        print 'Your string is alphanumeric.'
    if enterStr.isalpha():
        print 'Yor string is only characters.'
    if enterStr.isdigit():
        print 'Your string is only numbers.'
    if enterStr.islower():
        print 'Your string is lower case.'
    if enterStr.isupper():
        print 'Your string is upper case.'
    if enterStr.isspace():
        print 'your string has space.'

def main():

    userStr = getUserString()
    infoAboutUserStr(userStr)

main()
    
