def aList():
    '''This funtion will return a list of products.'''

    products = ['shampo', 'uje', 'buk', 'vaj', 'miell']

    return products

def getUserSearch():
    '''This funtion will get the user search.'''

    userSearch = raw_input("Enter the name of the prduct you want to search: ")

    return userSearch

def searchProduct(products, userSearch):
    '''This funtion will check if the product is in the products list.'''

    if (userSearch in products):
        print "The product was faound in the list."
    else:
        print "The product was not found in the list."

def main ():

    ushqimet = aList()
    userInterest = getUserSearch()
    searchProduct(ushqimet, userInterest)

main()

        
